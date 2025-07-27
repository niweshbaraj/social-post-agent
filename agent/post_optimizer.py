from langchain_core.messages import HumanMessage , SystemMessage
from agent.agent_state import PostState
from models.models import optimizer_model


def optimize_post(state:PostState) -> dict:
    prompt = [
    SystemMessage(content="You are a top-performing X (Twitter) ghostwriter. You rewrite and enhance posts to maximize professional impact, engagement, and relatability."),

    HumanMessage(content=f"""
        You’re given:

        1. An original X (Twitter) post
        2. Feedback on what needs to improve

        Your task is to **rewrite the post** so it:
        - Hooks readers within the **first two lines**
        - Shares a clear **story, insight, or challenge**
        - Includes **one real, helpful takeaway or industry fact**
        - Ends with **a call-to-conversation** (e.g., a question or reflection)
        - Uses a **casual, yet professional tone**
        - Is formatted for readability on mobile (line breaks, short paras)
        - Stays under **100 words**
        - Avoids buzzwords and clichés (e.g., "synergy", "disruption")
        - Sounds human, not AI-generated or overly polished
        - Optional: includes 2–4 relevant hashtags and **1–2 emojis max**

        ---

        **Original Post**:
        \"""{state['post']}\"""

        **Evaluator Feedback**:
        \"""{state['feedback']}\"""

        ---

        **Improved Post**:
        """)
    ]

    response = optimizer_model.invoke(prompt).content
    iteration = state['iteration'] + 1


    return {'post':response , 'iteration': iteration, 'post_history':[response]}