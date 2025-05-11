# FastAPI 프로젝트 구조 예시

## 구조

```
project_root/
├── requirements.txt
├── README.md
└── src/
    └── app/
        ├── __init__.py
        ├── main.py
        └── routers/
            ├── __init__.py
            └── root.py
```

## 실행 방법

```bash
uvicorn src.app.main:app --reload
``` 