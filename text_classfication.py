from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# klue/bert-base NER 라벨 매핑 (예시)
ENTITY_LABELS = {
    'LABEL_0': '인물(PS)',
    'LABEL_1': '기관(ORG)',
    'LABEL_2': '지명(LOC)',
    'LABEL_3': '작품(WORK)',
    'LABEL_4': '날짜(DAT)',
    'LABEL_5': '시간(TIM)',
    'LABEL_6': '수량(NUM)',
    'LABEL_7': '이벤트(EVT)',
    'LABEL_8': '용어(TERM)'
}

class TextRequest(BaseModel):
    text: str

app = FastAPI()
router = APIRouter()

classifier = pipeline("ner", model="klue/bert-base")

@router.post("/ner")
def ner_classification(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="텍스트를 입력해주세요.")
    result = classifier(request.text)
    entities = [
        {
            "word": entity["word"],
            "label": ENTITY_LABELS.get(entity["entity"], entity["entity"]),
            "score": entity["score"]
        }
        for entity in result
    ]
    return {"entities": entities}

app.include_router(router)