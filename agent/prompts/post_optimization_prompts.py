from langchain_core.messages import HumanMessage , SystemMessage
from agent.states.agent_state import PostState


def get_twitter_optimization_prompt(state: PostState) -> list:
    return [
        SystemMessage(content="You are a top-performing X (Twitter) ghostwriter. You rewrite and enhance posts to maximize professional impact, engagement, and relatability."),

        HumanMessage(content=f"""
            You're given:

            1. An original X (Twitter) post
            2. Feedback on what needs to improve

            Your task is to **rewrite the post** so it:
            - Hooks readers within the **first two lines**
            - Shares a clear **story, insight, or challenge**
            - Includes **one real, helpful takeaway or industry fact**
            - Ends with **a call-to-conversation** (e.g., a question or reflection)
            - Uses a **casual, yet professional tone**
            - Is formatted for readability on mobile (line breaks, short paras)
            - Stays between **50–100 words**
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


def get_linkedin_optimization_prompt(state: PostState) -> list:
    return [
        SystemMessage(content="You are a professional LinkedIn content strategist and ghostwriter. You enhance posts to maximize professional impact, thought leadership, and meaningful business discussions."),

        HumanMessage(content=f"""
            You're given:

            1. An original LinkedIn post
            2. Feedback on what needs to improve

            Your task is to **rewrite the post** so it:
            - Opens with a compelling **professional hook or industry insight**
            - Provides substantial **professional value and expertise**
            - Includes **personal professional experience or credible perspective**
            - Uses **professional yet engaging tone** - not too casual, not too corporate
            - Is structured for professional readability with clear paragraphs and strategic line breaks
            - Incorporates **relevant industry knowledge or data points**
            - Ends with **thought-provoking question or call for professional discussion**
            - Stays between **300-400 words** for substantial LinkedIn content
            - Avoids overly promotional language while maintaining professional authority
            - Uses appropriate **hashtags and professional terminology**
            - Demonstrates thought leadership and industry expertise
            - Encourages meaningful professional engagement

            ---

            **Original Post**:
            \"""{state['post']}\"""

            **Evaluator Feedback**:
            \"""{state['feedback']}\"""

            ---

            **Improved LinkedIn Post**:
            """)
    ]


def get_instagram_optimization_prompt(state: PostState) -> list:
    return [
        SystemMessage(content="You are a creative Instagram content strategist and copywriter. You enhance captions to maximize engagement, community building, and authentic connection with audiences."),

        HumanMessage(content=f"""
            You're given:

            1. An original Instagram caption
            2. Feedback on what needs to improve

            Your task is to **rewrite the caption** so it:
            - Starts with an **attention-grabbing hook** that works with visual content
            - Uses **engaging, conversational tone** that feels authentic and relatable
            - Tells a **story or shares an experience** that connects emotionally
            - Includes **relevant and trending hashtags** (8-15 hashtags)
            - Has **clear visual storytelling potential** (describes or complements imagery)
            - Uses **Instagram-friendly formatting**: short paragraphs, emojis, line breaks
            - Ends with **strong call-to-action** (comment, share, engage)
            - Stays between **100-150 words** for optimal Instagram engagement
            - Incorporates **community-building elements** (questions, relatability)
            - Works perfectly with accompanying visual content
            - Uses emojis strategically for engagement and readability
            - Creates desire to comment, share, and engage with the content

            ---

            **Original Caption**:
            \"""{state['post']}\"""

            **Evaluator Feedback**:
            \"""{state['feedback']}\"""

            ---

            **Improved Instagram Caption**:
            """)
    ]