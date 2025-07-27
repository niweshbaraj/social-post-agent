from langchain_together import ChatTogether
from together import Together
from agent.agent_state import GeneratePost, EvaluatePost
from dotenv import load_dotenv

load_dotenv()

model = ChatTogether(model= "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free")

generator_model = model.with_structured_output(GeneratePost)
evaluator_model = model.with_structured_output(EvaluatePost)

optimizer_model = ChatTogether(model= "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free")


def image_model(topic: str) -> dict:
    image_model = Together()
    output = image_model.images.generate(
        prompt=topic,
        model="black-forest-labs/FLUX.1-schnell-Free",
        steps=4,
        n=1
    )
    return output
