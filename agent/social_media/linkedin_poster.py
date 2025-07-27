import os
import requests
from dotenv import load_dotenv
from agent.states.agent_state import PostState


def text_post_on_linkedin(state: PostState) -> dict:
    """
    Post a text-only post to LinkedIn.

    Args:
        state (dict): Must contain key "post" with post text.

    Returns:
        dict: Status code and response message.
    """
    load_dotenv()
    
    access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    person_id = os.getenv("LINKEDIN_PERSON_ID")  # LinkedIn person URN
    
    if not access_token or not person_id:
        return {
            "status_code": 400,
            "response": "LinkedIn credentials not configured. Please set LINKEDIN_ACCESS_TOKEN and LINKEDIN_PERSON_ID in .env file"
        }

    url = "https://api.linkedin.com/v2/ugcPosts"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    payload = {
        "author": f"urn:li:person:{person_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": state["post"]
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 201:
            response_data = response.json()
            post_id = response_data.get("id", "Unknown")
            print(f"LinkedIn post created with ID: {post_id}")
            return {
                "status_code": 201,
                "response": {
                    "id": post_id,
                    "message": f"LinkedIn post created successfully, ID: {post_id}"
                }
            }
        else:
            print(f"LinkedIn API Error: {response.status_code} - {response.text}")
            return {
                "status_code": response.status_code,
                "response": f"LinkedIn API Error: {response.text}"
            }
            
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return {
            "status_code": None,
            "response": f"Request Error: {str(e)}"
        }
    except Exception as e:
        print(f"Error posting to LinkedIn: {e}")
        return {
            "status_code": None,
            "response": f"Error: {str(e)}"
        }


def media_post_on_linkedin(state: PostState) -> dict:
    """
    Post a LinkedIn post with an image.

    Args:
        state (dict): Must contain keys "post" (text) and "image_path" (local path to image file).

    Returns:
        dict: Status code and response message.
    """
    load_dotenv()
    
    access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    person_id = os.getenv("LINKEDIN_PERSON_ID")
    
    if not access_token or not person_id:
        return {
            "status_code": 400,
            "response": "LinkedIn credentials not configured. Please set LINKEDIN_ACCESS_TOKEN and LINKEDIN_PERSON_ID in .env file"
        }

    try:
        # Step 1: Register upload
        register_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        register_payload = {
            "registerUploadRequest": {
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                "owner": f"urn:li:person:{person_id}",
                "serviceRelationships": [{
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }]
            }
        }
        
        register_response = requests.post(register_url, headers=headers, json=register_payload)
        
        if register_response.status_code != 200:
            return {
                "status_code": register_response.status_code,
                "response": f"Failed to register upload: {register_response.text}"
            }
        
        register_data = register_response.json()
        upload_url = register_data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
        asset_id = register_data["value"]["asset"]
        
        # Step 2: Upload the image
        with open(state['image_path'], 'rb') as image_file:
            upload_headers = {"Authorization": f"Bearer {access_token}"}
            upload_response = requests.post(upload_url, headers=upload_headers, data=image_file)
            
            if upload_response.status_code != 201:
                return {
                    "status_code": upload_response.status_code,
                    "response": f"Failed to upload image: {upload_response.text}"
                }
        
        # Step 3: Create the post with media
        post_url = "https://api.linkedin.com/v2/ugcPosts"
        
        post_headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        
        post_payload = {
            "author": f"urn:li:person:{person_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": state["post"]
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [{
                        "status": "READY",
                        "description": {
                            "text": "Posted via Social Post Agent"
                        },
                        "media": asset_id,
                        "title": {
                            "text": "Social Post Agent"
                        }
                    }]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        post_response = requests.post(post_url, headers=post_headers, json=post_payload)
        
        if post_response.status_code == 201:
            response_data = post_response.json()
            post_id = response_data.get("id", "Unknown")
            print(f"LinkedIn post with media created with ID: {post_id}")
            return {
                "status_code": 201,
                "response": {
                    "id": post_id,
                    "message": f"LinkedIn post with image created successfully, ID: {post_id}"
                }
            }
        else:
            return {
                "status_code": post_response.status_code,
                "response": f"Failed to create post: {post_response.text}"
            }
            
    except Exception as e:
        print(f"Error posting media to LinkedIn: {e}")
        return {
            "status_code": None,
            "response": f"Error: {str(e)}"
        }
