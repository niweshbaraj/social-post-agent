from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from agent.langgraph_workflow import workflow


app = FastAPI()

# Add CORS middleware to handle browser extension requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {'message':'Welcome to the Social Post Agent API!'}


class InitialState(BaseModel):
    topic: str = Field(..., description="The topic for the post")
    max_iteration: int = Field(5, description="Maximum number of iterations for post optimization")
    generate_image: bool = Field(False, description="Whether to generate an image for the post")
    platform: str = Field("twitter", description="Social media platform to post to (X [twitter], linkedin, instagram)")


@app.post("/post_content/")
async def post_content(
    data: InitialState,
) -> dict:
    initial_state = {
        "topic": data.topic,
        "iteration": 1,
        "max_iteration": data.max_iteration,
        "generate_image": data.generate_image,
        "platform": data.platform,
    }
    
    output = workflow.invoke(initial_state)
    
    print(f"Workflow output: {output}")
    
    try:
        # Clean the output to remove problematic fields that might cause serialization issues
        clean_output = {
            "topic": output.get("topic"),
            "post": output.get("post"),
            "status_code": output.get("status_code"),
            "tweet_id": output.get("response", {}).get("id") if isinstance(output.get("response"), dict) else None,
            "generate_image": output.get("generate_image"),
            "iteration": output.get("iteration"),
            "max_iteration": output.get("max_iteration"),
            "status": output.get("status"),
            "feedback": output.get("feedback"),
            "post_history": output.get("post_history", []),
            "feedback_history": output.get("feedback_history", []),
        }
        
        if output.get("status_code") == 201:
            return JSONResponse(status_code=201, content={"message": "Post created successfully", "data": clean_output})
        else:
            return JSONResponse(status_code=400, content={"message": "Post creation failed", "error": output.get("error", "Unknown error")})
    except Exception as e:
        print(f"Error processing workflow output: {e}")
        print(f"Output keys: {list(output.keys()) if isinstance(output, dict) else 'Not a dict'}")
        return JSONResponse(status_code=500, content={"message": "Internal server error", "error": str(e)})                     
