from agent.states.agent_state import PostState
from models.models import evaluator_model
from agent.prompts.post_evaluation_prompts import get_twitter_evaluation_prompt, get_linkedin_evaluation_prompt, get_instagram_evaluation_prompt
from langsmith import traceable


@traceable(name="evaluate_post", run_type="chain")
def evaluate_post(state:PostState) -> dict:
    """Evaluate the generated post for quality and platform compliance"""
    platform = state.get('platform', 'twitter')
    
    if platform == 'twitter':
        prompt = get_twitter_evaluation_prompt(state)
    elif platform == 'linkedin':
        prompt = get_linkedin_evaluation_prompt(state)
    elif platform == 'instagram':
        prompt = get_instagram_evaluation_prompt(state)
    else:
        # Default to Twitter rules
        prompt = get_twitter_evaluation_prompt(state)

    response = evaluator_model.invoke(prompt)
    status = response.status
    feedback = response.feedback

    return {"status":status , "feedback":feedback, 'feedback_history': [feedback]}

