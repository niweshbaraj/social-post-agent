from agent.states.agent_state import PostState
from agent.social_media.x_twitter_poster import text_post_on_x_twitter, media_post_on_x_twitter
from agent.social_media.linkedin_poster import text_post_on_linkedin, media_post_on_linkedin
from agent.social_media.instagram_poster import text_post_on_instagram, media_post_on_instagram
from langsmith import traceable


@traceable(name="text_post", run_type="tool")
def text_post(state: PostState) -> PostState:
    """Post text content to the specified social media platform"""
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        print("Posting text on X (Twitter)")
        response = text_post_on_x_twitter(state)
    elif platform == 'linkedin':
        print("Posting text on LinkedIn")
        response = text_post_on_linkedin(state)
    elif platform == 'instagram':
        print("Posting text on Instagram")
        response = text_post_on_instagram(state)
    else:
        print(f"Unknown platform: {platform}")
        response = {"status_code": 400, "response": f"Unsupported platform: {platform}"}
    
    state['response'] = response.get('response', '')
    state['status_code'] = response.get('status_code', 0)
    return state


@traceable(name="media_post", run_type="tool")
def media_post(state: PostState) -> PostState:
    """Post media content (text + image) to the specified social media platform"""
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        print("Posting media on X (Twitter)")
        response = media_post_on_x_twitter(state)
    elif platform == 'linkedin':
        print("Posting media on LinkedIn")
        response = media_post_on_linkedin(state)
    elif platform == 'instagram':
        print("Posting media on Instagram")
        response = media_post_on_instagram(state)
    else:
        print(f"Unknown platform: {platform}")
        response = {"status_code": 400, "response": f"Unsupported platform: {platform}"}
    
    state['response'] = response.get('response', '')
    state['status_code'] = response.get('status_code', 0)
    return state
