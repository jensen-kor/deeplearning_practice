from fastapi import FastAPI
from .routers import root
from .routers import speech
from .routers import text_classfication
from .routers import translate_en2fran
from .routers import question_answering
from .routers import tc

app = FastAPI()

app.include_router(root.router)
app.include_router(speech.router)
app.include_router(text_classfication.router)
app.include_router(translate_en2fran.router)
app.include_router(question_answering.router)
app.include_router(tc.router) 