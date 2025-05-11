from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline, Pipeline

router = APIRouter()

DEFAULT_MODEL = "beomi/KcELECTRA-base-v2022"

SUPPORTED_MODELS = [
    "beomi/KcELECTRA-base-v2022",
    # 필요시 여기에 지원 모델 추가
]

def get_classifier(model_name: str) -> Pipeline:
    return pipeline("sentiment-analysis", model=model_name)

class SentimentRequest(BaseModel):
    text: str
    model: str = DEFAULT_MODEL

@router.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="분석할 문장을 입력해주세요.")
    model_name = request.model or DEFAULT_MODEL
    if model_name not in SUPPORTED_MODELS:
        raise HTTPException(status_code=400, detail=f"지원하지 않는 모델입니다. 지원 모델: {SUPPORTED_MODELS}")
    try:
        classifier = get_classifier(model_name)
        result = classifier(request.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"모델 로딩 또는 분석 중 오류: {str(e)}")
    return {"input": request.text, "model": model_name, "result": result} 