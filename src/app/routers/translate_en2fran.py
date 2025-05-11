from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()

translator = pipeline("translation_en_to_ko", model="Helsinki-NLP/opus-mt-en-ROMANCE")

class TranslateRequest(BaseModel):
    text: str

@router.post("/translate-en2ko")
def translate_en2ko(request: TranslateRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="번역할 텍스트를 입력해주세요.")
    result = translator(request.text, max_length=512)
    translation = result[0]['translation_text']
    return {"original": request.text, "translation": translation} 