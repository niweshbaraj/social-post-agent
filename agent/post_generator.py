from langchain_core.messages import HumanMessage , SystemMessage
from agent.agent_state import PostState
from models.models import generator_model


def generate_post(state:PostState) -> dict:

    prompt = [
    SystemMessage(content=(
        "You are a thoughtful and engaging X (Twitter) content strategist. "
        "You write posts that spark conversations, demonstrate thought leadership, "
        "and resonate emotionally with a professional audience."
    )),

    HumanMessage(content=(
        f"""
You're given a topic: "{state['topic']}".

Based on this, write a **X (Twitter) post** that is:
- Insightful, emotionally resonant, or thought-provoking  
- Rooted in a personal experience, lesson, or surprising fact  
- Authentic and human—not corporate or robotic  
- Written in a first-person or conversational tone  
- Structured for readability with short paragraphs, line breaks, and/or emojis (optional)  
- Capable of generating engagement (comments, shares, or saves)  

---

**Rules for the post**:
- Word count: 50–100 words (sweet spot for X (Twitter) posts)  
- Must include at least one practical insight, professional lesson, or industry stat/fact  
- Hook readers in the **first 2 lines** (important for 'See More' clicks)  
- Conclude with a question or call-to-engagement (e.g., "What are your thoughts?")  
- Avoid jargon, buzzwords, or generic corporate phrases  
- Authentic storytelling beats polished perfection  

Optional:
- Include 2–4 relevant hashtags at the end  
- Emojis are fine, but use them sparingly and tastefully  

Write the post below:
        """
    ))
]


    
    response = generator_model.invoke(prompt)
    title = response.title
    post = response.post
    return {'post' : post , "title":title , "post_history":[post]}