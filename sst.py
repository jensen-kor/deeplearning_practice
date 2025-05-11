from transformers import pipeline

# 한국어 음성 인식 파이프라인 (Whisper-base, 토큰 없이 사용 가능)
stt = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=-1)

file_path = input("한국어 음성 파일 경로를 입력하세요 (예: sample.wav): ")

result = stt(file_path, generate_kwargs={"language": "korean"})
text = result["text"]

print("\n[음성 인식 결과]")
print(f"파일: {file_path}")
print(f"텍스트: {text}")
