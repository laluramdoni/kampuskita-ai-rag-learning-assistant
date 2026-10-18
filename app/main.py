"""FastAPI application. Run only on localhost; no accounts or production security."""
from __future__ import annotations
import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from . import store, rag
from .content import SUGGESTIONS, QUIZ_OFFLINE

ROOT=Path(__file__).resolve().parents[1]
app=FastAPI(title='KampusKita AI · Academic RAG Portfolio',version='1.0.0')
store.bootstrap()
app.mount('/static',StaticFiles(directory=ROOT/'static'),name='static')

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str=Field(min_length=1,max_length=1200)
    history: list[Message]=Field(default_factory=list,max_length=12)
    mode: str='auto'

@app.get('/')
def home(): return FileResponse(ROOT/'static'/'index.html')

@app.get('/api/status')
def status():
    d=store.public_docs()
    return {'name':'KampusKita AI','documents':len(d),'chunks':sum(x['chunks_count'] for x in d),
            'paper':True,'ollama':rag.check_models(),'suggestions':SUGGESTIONS}

@app.get('/api/documents')
def documents(): return {'documents':store.public_docs()}

@app.post('/api/documents')
async def upload_document(file: UploadFile=File(...)):
    try:
        raw=await file.read(10*1024*1024+1)
        result=store.add_document(file.filename or 'dokumen.pdf',raw)
        return {'success':True,'document':result}
    except ValueError as exc: raise HTTPException(400,str(exc))

@app.delete('/api/documents/{doc_id}')
def delete_document(doc_id: str):
    try:store.delete_document(doc_id)
    except KeyError as exc:raise HTTPException(404,str(exc))
    except ValueError as exc:raise HTTPException(403,str(exc))
    return {'success':True}

@app.post('/api/chat')
def chat(body: ChatRequest):
    if body.mode not in {'auto','demo','ai'}: raise HTTPException(400,'Mode tidak dikenal.')
    try:return rag.ask(body.message,[x.model_dump() for x in body.history],body.mode)
    except ValueError as exc: raise HTTPException(400,str(exc))

@app.get('/api/quiz')
def quiz():
    return {'questions':QUIZ_OFFLINE,'mode':'curated-paper-quiz',
            'note':'Kuis ini ditulis berdasarkan isi artikel dan bukan dihasilkan AI secara real-time.'}

@app.get('/api/paper')
def paper():return FileResponse(store.PAPER,media_type='application/pdf',filename='JTIKA_2025_RAG_Telegram.pdf')
