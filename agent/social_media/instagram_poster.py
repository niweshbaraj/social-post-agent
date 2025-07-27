import os
import requests
from dotenv import load_dotenv
from agent.states.agent_state import PostState


def text_post_on_instagram(state: PostState) -> dict:
    """
    Instagram doesn't support text-only posts. This function returns an error message.
    
    Args:
        state (dict): Must contain key "post" with post text.

    Returns:
        dict: Status code and response message.
    """
    return {
        "status_code": 400,
        "response": "Instagram requires an image for all posts. Please enable 'Generate AI image' option."
    }


def media_post_on_instagram(state: PostState) -> dict:
    """
    Post an image with caption to Instagram using Instagram Basic Display API.

    Args:
        state (dict): Must contain keys "post" (caption) and "image_path" (local path to image file).

    Returns:
        dict: Status code and response message.
    """
    load_dotenv()
    
    access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
    business_account_id = os.getenv("INSTAGRAM_BUSINESS_ACCOUNT_ID")
    
    if not access_token or not business_account_id:
        return {
            "status_code": 400,
            "response": "Instagram credentials not configured. Please set INSTAGRAM_ACCESS_TOKEN and INSTAGRAM_BUSINESS_ACCOUNT_ID in .env file"
        }

    try:
        # Step 1: Upload image to a publicly accessible URL (you might need to implement this)
        # For now, we'll assume you have a way to upload the image and get a public URL
        # This is a simplified example - in practice, you'd need to upload to your server/CDN first
        
        image_url = upload_image_to_public_url(state['image_path'])  # You need to implement this
        
        if not image_url:
            return {
                "status_code": 400,
                "response": "Failed to upload image to public URL. Instagram requires publicly accessible image URLs."
            }
        
        # Step 2: Create media container
        container_url = f"https://graph.facebook.com/v18.0/{business_account_id}/media"
        
        container_params = {
            "image_url": image_url,
            "caption": state["post"],
            "access_token": access_token
        }
        
        container_response = requests.post(container_url, params=container_params)
        
        if container_response.status_code != 200:
            return {
                "status_code": container_response.status_code,
                "response": f"Failed to create media container: {container_response.text}"
            }
        
        container_data = container_response.json()
        creation_id = container_data.get("id")
        
        if not creation_id:
            return {
                "status_code": 400,
                "response": f"No creation ID returned: {container_data}"
            }
        
        # Step 3: Publish the media
        publish_url = f"https://graph.facebook.com/v18.0/{business_account_id}/media_publish"
        
        publish_params = {
            "creation_id": creation_id,
            "access_token": access_token
        }
        
        publish_response = requests.post(publish_url, params=publish_params)
        
        if publish_response.status_code == 200:
            publish_data = publish_response.json()
            post_id = publish_data.get("id", "Unknown")
            print(f"Instagram post created with ID: {post_id}")
            return {
                "status_code": 201,
                "response": {
                    "id": post_id,
                    "message": f"Instagram post created successfully, ID: {post_id}"
                }
            }
        else:
            return {
                "status_code": publish_response.status_code,
                "response": f"Failed to publish media: {publish_response.text}"
            }
            
    except Exception as e:
        print(f"Error posting to Instagram: {e}")
        return {
            "status_code": None,
            "response": f"Error: {str(e)}"
        }


def upload_image_to_public_url(image_path: str) -> str:
    """
    Upload image to a publicly accessible URL.
    
    This is a placeholder function. You need to implement this based on your infrastructure:
    - Upload to AWS S3, Google Cloud Storage, Cloudinary, etc.
    - Return the public URL of the uploaded image
    
    Args:
        image_path (str): Local path to the image file
        
    Returns:
        str: Public URL of the uploaded image, or None if upload fails
    """
    # TODO: Implement actual image upload to your cloud storage
    # For now, return None to indicate upload failure
    print(f"TODO: Upload {image_path} to public cloud storage and return URL")
    return None


# Alternative implementation for local development/testing
def media_post_on_instagram_local(state: PostState) -> dict:
    """
    Placeholder for Instagram posting in local development.
    Returns success message without actually posting.
    """
    return {
        "status_code": 201,
        "response": {
            "id": "local_test_id",
            "message": "Instagram post simulated successfully (local development mode)"
        }
    }
