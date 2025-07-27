from langchain_core.messages import HumanMessage , SystemMessage
from agent.agent_state import PostState
from models.models import evaluator_model


def evaluate_post(state:PostState) -> dict:
    prompt = [
    SystemMessage(content=(
        "You are an experienced social media strategist for X (Twitter). "
        "You evaluate posts based on their ability to inform, engage, and connect with a professional audience."
    )),

    HumanMessage(content=(
        f"""
            You will be given a X (Twitter) post and its topic.

            Evaluate the post using these **key performance rules**:

            1. Starts with a strong **hook in the first 1–2 lines**  
            2. Includes a clear **personal experience, insight, or industry perspective**  
            3. Shares **one real, credible fact or takeaway**  
            4. Uses **clear and engaging language** (not too formal, not robotic)  
            5. Follows **X (Twitter) post structure**: short paragraphs, clean formatting  
            6. Ends with **a relatable reflection or a call-to-engagement**  
            7. Word count is **between 50–100 words**  
            8. Avoids fluff, cliches, or overly promotional language  

            ---

            **Response format**:
            - If the post meets all the criteria, respond with: `approve`  
            - If anything is missing, respond with: `improvement_required`, followed by 1–2 clear suggestions on what needs to be improved and why  

            ---

            **Topic**: "{state['topic']}"  
            **Post**:
            \"""{state['post']}\"""
                    """
        ))
    ]

    response = evaluator_model.invoke(prompt)
    status = response.status
    feedback = response.feedback

    return {"status":status , "feedback":feedback, 'feedback_history': [feedback]}
