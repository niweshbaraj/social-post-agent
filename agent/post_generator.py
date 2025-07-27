from agent.states.agent_state import PostState
from models.models import generator_model
from agent.prompts.post_generation_prompts import get_twitter_generation_prompt, get_linkedin_generation_prompt, get_instagram_generation_prompt  


def generate_post(state: PostState) -> dict:
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        prompt = get_twitter_generation_prompt(state)
    elif platform == 'linkedin':
        prompt = get_linkedin_generation_prompt(state)
    elif platform == 'instagram':
        prompt = get_instagram_generation_prompt(state)
    else:
        # Default to Twitter
        prompt = get_twitter_generation_prompt(state)
    
    response = generator_model.invoke(prompt)
    title = response.title
    post = response.post
    return {'post': post, "title": title, "post_history": [post]}
