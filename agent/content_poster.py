from agent.agent_state import PostState
from agent.social_media.x_twitter_poster import text_post_on_x_twitter, media_post_on_x_twitter


def text_post(state: PostState) -> PostState:
    print("Posting text on X (Twitter)")
    response = text_post_on_x_twitter(state)
    state['response'] = response.get('response', '')
    state['status_code'] = response.get('status_code', 0)
    return state


def media_post(state: PostState) -> PostState:
    print("Posting media on X (Twitter)")
    response = media_post_on_x_twitter(state)
    state['response'] = response.get('response', '')
    state['status_code'] = response.get('status_code', 0)
    return state
