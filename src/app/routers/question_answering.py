from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()

qa_pipeline = pipeline("question-answering")

class QARequest(BaseModel):
    context: str
    question: str

@router.post("/question-answering")
def question_answering(request: QARequest):
    if not request.context.strip() or not request.question.strip():
        raise HTTPException(status_code=400, detail="context와 question을 모두 입력해주세요.")
    result = qa_pipeline({"context": request.context, "question": request.question})
    return {"answer": result["answer"], "score": result["score"]} 