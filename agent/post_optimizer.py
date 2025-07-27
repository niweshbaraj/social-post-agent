from langchain_core.messages import HumanMessage , SystemMessage
from agent.states.agent_state import PostState
from models.models import optimizer_model
from agent.prompts.post_optimization_prompts import get_twitter_optimization_prompt, get_linkedin_optimization_prompt, get_instagram_optimization_prompt


def optimize_post(state: PostState) -> dict:
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        prompt = get_twitter_optimization_prompt(state)
    elif platform == 'linkedin':
        prompt = get_linkedin_optimization_prompt(state)
    elif platform == 'instagram':
        prompt = get_instagram_optimization_prompt(state)
    else:
        # Default to Twitter
        prompt = get_twitter_optimization_prompt(state)
    
    response = optimizer_model.invoke(prompt).content
    iteration = state['iteration'] + 1
    
    return {'post': response, 'iteration': iteration, 'post_history': [response]}
