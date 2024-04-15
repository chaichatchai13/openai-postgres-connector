from fastapi import APIRouter, HTTPException
from app.database import create_openai_result, get_openai_result_by_prompt_id
from app.schemas import OpenAIResultResponse
from app.services import query_openai

router = APIRouter()

@router.post("/prompt/", response_model=OpenAIResultResponse)
def create_prompt(prompt: str):
    try:
        response_text = query_openai(prompt)
        result = create_openai_result(prompt, response_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prompt/{prompt_id}", response_model=OpenAIResultResponse)
def get_response(prompt_id: int):
    result = get_openai_result_by_prompt_id(prompt_id)
    if not result:
        raise HTTPException(status_code=404, detail="Response not found")
    return result