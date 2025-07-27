from typing import Annotated, TypedDict, Literal
from pydantic import BaseModel , Field
import operator

class PostState(TypedDict):
    topic: str
    post: str
    evaluate: str
    optimize: str
    title: str
    feedback: str
    status: Literal["approve", "need_improvement"]
    response: str
    status_code: int
    uploadurl: str
    uploadassets: str
    image_path: str
    generate_image: Literal[True, False]
    platform: Literal["twitter", "linkedin", "instagram"]
    next: str
    path_choose: str
    url: str
    score: int
    iteration: int
    max_iteration: int
    post_history: Annotated[list[str], operator.add]
    feedback_history: Annotated[list[str], operator.add]
    

class GeneratePost(BaseModel):
    title : str = Field(... , description="the suitable title for the post")
    post : str


class EvaluatePost(BaseModel):
    status : Literal["approve" , "need_improvement"] = Field(... , description="the final evaluation should be approve or need_improvement")
    feedback : str = Field(... , description="feedback for the tweet ")