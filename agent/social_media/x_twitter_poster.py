import os
import tweepy
from dotenv import load_dotenv
from agent.states.agent_state import PostState


def text_post_on_x_twitter(state: PostState) -> dict:
    """
    Post a text-only tweet to X (Twitter).

    Args:
        state (dict): Must contain key "post" with tweet text.

    Returns:
        dict: Status code and response message.
    """
    load_dotenv()
    
    # bearer_token = os.getenv("X_BEARER_TOKEN")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")

    client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    )
    
    try:
        text = state["post"]
        response = client.create_tweet(text=text)
        print("Tweet posted with ID:", response.data['id'])
        return {
            "status_code": 201,
            "response": response.data
        }
    except tweepy.TweepyException as e:
        print("Tweepy Exception:", e)
        return {
            "status_code": None,
            "response": f"Tweepy Error: {e}"
        }
    except Exception as e:
        print("Error posting tweet:", e)
        return {
            "status_code": None,
            "response": f"Error: {str(e)}"
        }
    

def media_post_on_x_twitter(state) -> dict:
    """
    Post a tweet with an image to X (Twitter).

    Args:
        state (dict): Must contain keys "post" (text) and "image_path" (local path to image file).

    Returns:
        dict: Status code and response message.
    """

    load_dotenv()

    # bearer_token = os.getenv("X_BEARER_TOKEN")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")

    client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    )

    # Set up OAuth1 auth for old and new API access
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

    # Initialize API v1.1 for media upload
    api = tweepy.API(auth)

    try:
        # Step 1: Upload media via API v1.1
        media = api.media_upload(state['image_path'])
        media_id = media.media_id_string
        print(f"Media uploaded with media_id: {media_id}")

        # 2. Create tweet with uploaded media id
        text = state["post"]
        tweet_response = client.create_tweet(text=text, media_ids=[media_id])
        tweet_id = tweet_response.data['id']

        print(f"Tweet with media posted successfully, tweet ID: {tweet_id}")
        return {
            "status_code": 201,
            "response": {
                "id": tweet_id,
                "message": f"Tweet with image posted, ID: {tweet_id}"
            }
        }
    except tweepy.TweepyException as e:
        print("Tweepy Exception:", e)
        return {
            "status_code": None,
            "response": f"Tweepy error: {e}"
        }
    except Exception as e:
        print("General Exception:", repr(e))
        return {
            "status_code": None,
            "response": f"Error: {str(e)}"
        }
