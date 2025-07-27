from agent.agent_state import PostState
from agent.social_media.x_twitter_poster import text_post_on_x_twitter, media_post_on_x_twitter


def text_post(state: PostState) -> PostState:
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        print("Posting text on X (Twitter)")
        response = text_post_on_x_twitter(state)
    elif platform == 'linkedin':
        print("Posting text on LinkedIn")
        # TODO: Implement LinkedIn posting
        response = {"status_code": 400, "response": "LinkedIn posting not yet implemented"}
    elif platform == 'instagram':
        print("Posting text on Instagram")
        # TODO: Implement Instagram posting
        response = {"status_code": 400, "response": "Instagram posting not yet implemented"}
    else:
        print(f"Unknown platform: {platform}")
        response = {"status_code": 400, "response": f"Unsupported platform: {platform}"}
    
    state['response'] = response.get('response', '')
    state['status_code'] = response.get('status_code', 0)
    return state


def media_post(state: PostState) -> PostState:
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        print("Posting media on X (Twitter)")
        response = media_post_on_x_twitter(state)
    elif platform == 'linkedin':
        print("Posting media on LinkedIn")
        # TODO: Implement LinkedIn media posting
        response = {"status_code": 400, "response": "LinkedIn media posting not yet implemented"}
    elif platform == 'instagram':
        print("Posting media on Instagram")
        # TODO: Implement Instagram media posting
        response = {"status_code": 400, "response": "Instagram media posting not yet implemented"}
    else:
        print(f"Unknown platform: {platform}")
        response = {"status_code": 400, "response": f"Unsupported platform: {platform}"}
    
    state['response'] = response.get('response', '')
    state['status_code'] = response.get('status_code', 0)
    return state
