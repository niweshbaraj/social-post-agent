from langchain_core.messages import HumanMessage , SystemMessage
from agent.states.agent_state import PostState


def get_twitter_generation_prompt(state: PostState) -> list:
    return [
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


def get_linkedin_generation_prompt(state: PostState) -> list:
    return [
        SystemMessage(content=(
            "You are a professional LinkedIn content strategist. "
            "You create posts that provide substantial professional value, demonstrate expertise, "
            "and engage business professionals in meaningful discussions."
        )),

        HumanMessage(content=(
            f"""
                You're given a topic: "{state['topic']}".

                Based on this, write a **LinkedIn post** that is:
                - Professional yet engaging and authentic
                - Provides substantial value to business professionals
                - Demonstrates thought leadership and industry expertise
                - Rooted in professional experience, insights, or industry trends
                - Structured for professional readability with clear paragraphs
                - Encourages meaningful professional discussion

                ---

                **Rules for the LinkedIn post**:
                - Word count: 300–400 words (optimal for LinkedIn engagement)
                - Start with a compelling professional hook or industry insight
                - Include personal professional experience or credible industry perspective
                - Provide actionable insights, lessons learned, or valuable industry information
                - Use professional tone but remain conversational and relatable
                - Include relevant industry data, trends, or professional observations
                - Structure with clear paragraphs and strategic line breaks for readability
                - End with a thought-provoking question to encourage professional discussion
                - Include 3–5 relevant professional hashtags
                - Avoid overly promotional language while maintaining authority

                The post should position you as a knowledgeable professional sharing valuable insights with your network.

                Write the LinkedIn post below:
            """
        ))
    ]


def get_instagram_generation_prompt(state: PostState) -> list:
    return [
        SystemMessage(content=(
            "You are a creative Instagram content strategist. "
            "You create engaging captions that tell stories, build community, "
            "and work perfectly with visual content to maximize engagement."
        )),

        HumanMessage(content=(
            f"""
                You're given a topic: "{state['topic']}".

                Based on this, write an **Instagram caption** that is:
                - Engaging, authentic, and relatable
                - Perfect for pairing with visual content (photo/graphic)
                - Tells a story or shares an experience
                - Builds community and encourages interaction
                - Uses Instagram's conversational, friendly tone
                - Optimized for high engagement (likes, comments, shares)

                ---

                **Rules for the Instagram caption**:
                - Word count: 100–150 words (optimal for Instagram engagement)
                - Start with an attention-grabbing hook that works with visuals
                - Use conversational, authentic tone that feels personal
                - Tell a story or share an experience that creates emotional connection
                - Include relevant and trending hashtags (8-15 hashtags)
                - Use Instagram-friendly formatting: short paragraphs, emojis, line breaks
                - End with a strong call-to-action (ask a question, encourage comments)
                - Include community-building elements (relatability, shared experiences)
                - Remember this will accompany an image - reference or complement visual content
                - Use emojis strategically to enhance readability and engagement

                The caption should make people want to engage, comment, and share with their friends.

                Write the Instagram caption below:
            """
        ))
    ]