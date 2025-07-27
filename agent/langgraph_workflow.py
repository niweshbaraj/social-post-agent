from langgraph.graph import StateGraph, END, START
from agent.states.agent_state import PostState
from agent.post_generator import generate_post
from agent.post_evaluator import evaluate_post
from agent.post_optimizer import optimize_post
from agent.image_generator import generate_ai_image
from agent.content_poster import text_post, media_post


def decision_one(state:PostState) -> str:
    if state['status'] == "approve" or state['iteration'] >= state['max_iteration']:
        return "approve"

    elif state['status'] == "need_improvement":
        return "need_improvement"


def decision_two(state: PostState) -> str:
    platform = state.get('platform', 'twitter')
    
    # Instagram always requires an image
    if platform == 'instagram':
        if state.get('image_path') is not None:
            print("Instagram: image_path found, media_post")
            return "media_post"
        else:
            print("Instagram: no image found, generate_ai_image")
            return "generate_ai_image"
    
    # For Twitter and LinkedIn, follow original logic
    if state.get('image_path') is not None:
        print("image_path found, media_post")
        return "media_post"
    
    elif not state.get('generate_image', False):
        print("generate_image is False or missing, text_post")
        return "text_post"

    elif state.get("generate_image") is True:
        print("generate_image is True, generate_ai_image")
        return "generate_ai_image"
    

def post_decision(state:PostState) -> PostState:
    return state


graph = StateGraph(PostState)

graph.add_node("generate_post" , generate_post)
graph.add_node("evaluate_post" , evaluate_post)
graph.add_node("optimize_post" , optimize_post)
graph.add_node("text_post" , text_post)
graph.add_node("media_post" , media_post)
graph.add_node("post_decision" , post_decision)
graph.add_node("generate_ai_image" , generate_ai_image)

# Edges...
graph.add_edge(START , "generate_post")
graph.add_edge("generate_post" , "evaluate_post")
graph.add_conditional_edges("evaluate_post" , decision_one , {"approve":"post_decision" , "need_improvement": "optimize_post"})
graph.add_edge("optimize_post" , "evaluate_post")
graph.add_conditional_edges("post_decision" , decision_two , {"media_post": "media_post" , "text_post":"text_post" , "generate_ai_image" : "generate_ai_image" })
graph.add_edge("generate_ai_image" , "media_post")
graph.add_edge("text_post" , END)
graph.add_edge("media_post" , END)

workflow = graph.compile()