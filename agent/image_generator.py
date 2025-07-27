import requests
from together import Together
from agent.agent_state import PostState
from models.models import image_model


def generate_ai_image(state: PostState) -> dict:
    
    topic = state['topic']
    output = image_model(topic)
    img_url = output.data[0].url
    response = requests.get(img_url)
    image_path = "generated_image.png"
    with open(image_path, 'wb') as f:
        f.write(response.content)

    return {"image_path": image_path}