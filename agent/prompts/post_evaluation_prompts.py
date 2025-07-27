from langchain_core.messages import HumanMessage , SystemMessage
from agent.states.agent_state import PostState


def get_twitter_evaluation_prompt(state: PostState) -> list:
    return [
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


def get_linkedin_evaluation_prompt(state: PostState) -> list:
    return [
        SystemMessage(content=(
            "You are an experienced LinkedIn content strategist. "
            "You evaluate posts based on their ability to inform, engage, and provide professional value to a business audience."
        )),

        HumanMessage(content=(
            f"""
                You will be given a LinkedIn post and its topic.

                Evaluate the post using these **key performance rules for LinkedIn**:

                1. Starts with a compelling **professional hook or industry insight**  
                2. Provides **substantial professional value** (insights, lessons, trends, tips)  
                3. Includes **personal experience or professional perspective** that adds credibility  
                4. Uses **professional yet engaging tone** - not too casual, not too corporate  
                5. Follows **LinkedIn structure**: clear paragraphs, strategic line breaks, professional formatting  
                6. Incorporates **relevant industry knowledge or data points**  
                7. Ends with **thought-provoking question or call for professional discussion**  
                8. Word count is **between 300–400 words** for substantial content  
                9. Avoids overly promotional language while maintaining professional authority  
                10. Uses appropriate **hashtags and professional terminology**  

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


def get_instagram_evaluation_prompt(state: PostState) -> list:
    return [
        SystemMessage(content=(
            "You are an experienced Instagram content strategist. "
            "You evaluate posts based on their visual appeal, engagement potential, and ability to connect with audiences through compelling captions."
        )),

        HumanMessage(content=(
            f"""
                You will be given an Instagram post caption and its topic.

                Evaluate the post using these **key performance rules for Instagram**:

                1. Starts with an **attention-grabbing hook** that works with visual content  
                2. Uses **engaging, conversational tone** that feels authentic and relatable  
                3. Tells a **story or shares an experience** that connects emotionally  
                4. Includes **relevant and trending hashtags** (8-15 hashtags)  
                5. Has **clear visual storytelling potential** (describes or complements imagery)  
                6. Uses **Instagram-friendly formatting**: short paragraphs, emojis, line breaks  
                7. Ends with **strong call-to-action** (comment, share, engage)  
                8. Word count is **between 100–150 words** for optimal engagement  
                9. Incorporates **community-building elements** (questions, relatability)  
                10. **Requires visual content** - caption should complement an image  

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