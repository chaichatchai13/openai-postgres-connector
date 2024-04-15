from pydantic import BaseModel

class OpenAIResultResponse(BaseModel):
    id: int
    prompt: str
    response: str

    class Config:
        orm_mode = True
