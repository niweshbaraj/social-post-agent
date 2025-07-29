import requests
from together import Together
from agent.states.agent_state import PostState
from models.models import image_model
from langsmith import traceable


@traceable(name="generate_ai_image", run_type="tool")
def generate_ai_image(state: PostState) -> dict:
    """Generate an AI image based on the post topic"""
    topic = state['topic']
    output = image_model(topic)
    img_url = output.data[0].url
    response = requests.get(img_url)
    image_path = "generated_image.png"
    with open(image_path, 'wb') as f:
        f.write(response.content)

    return {"image_path": image_path}