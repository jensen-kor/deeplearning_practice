from fastapi import APIRouter, UploadFile, File, HTTPException
from transformers import pipeline
import tempfile
import shutil

router = APIRouter()

stt = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=-1)

@router.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".wav", ".mp3", ".m4a")):
        raise HTTPException(status_code=400, detail="지원하지 않는 파일 형식입니다.")
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename[-4:]) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    result = stt(tmp_path, generate_kwargs={"language": "korean"})
    text = result["text"]
    return {"filename": file.filename, "text": text} 