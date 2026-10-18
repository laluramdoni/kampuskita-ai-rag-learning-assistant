"""A small, transparent, local document library; not intended for multi-user deployment."""
from __future__ import annotations
import json
import re
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader
from pypdf.errors import PdfReadError
from .content import RESEARCH_BRIEF, DEMO_GUIDE

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
UPLOADS = DATA / 'uploads'
INDEX = DATA / 'library.json'
PAPER = DATA / 'source_paper.pdf'
LOCK = threading.RLock()


def safe_title(name: str) -> str:
    name = Path(name.replace('\\', '/')).name
    name = re.sub(r'[^\w\s().\-]', '_', name, flags=re.UNICODE)
    return name[:100] or 'Dokumen'


def split_text(text: str, max_words: int = 125, overlap: int = 24):
    # Token length is approximate: this demo is not the paper's SentenceSplitter.
    words = re.sub(r'\s+', ' ', text).strip().split(' ')
    if not words or words == ['']:
        return []
    result = []
    step = max_words - overlap
    for start in range(0, len(words), step):
        chunk = ' '.join(words[start:start + max_words]).strip()
        if len(chunk) >= 30:
            result.append(chunk)
        if start + max_words >= len(words):
            break
    return result


def extract_pdf(path: Path) -> list[dict]:
    try:
        reader = PdfReader(str(path))
        n_pages = len(reader.pages)
    except (PdfReadError, ValueError, KeyError, TypeError) as exc:
        raise ValueError('PDF rusak, tidak valid, atau dilindungi kata sandi.') from exc
    if n_pages > 150:
        raise ValueError('Batas PDF adalah 150 halaman.')
    pages = []
    try:
        for i, page in enumerate(reader.pages, start=1):
            content = (page.extract_text() or '').strip()
            if content:
                pages.append({'page':i, 'text':content})
    except (PdfReadError, ValueError, TypeError) as exc:
        raise ValueError('Tidak dapat membaca isi PDF. Gunakan PDF teks yang tidak rusak.') from exc
    if not pages:
        raise ValueError('PDF tidak memiliki teks yang dapat diekstrak. PDF scan memerlukan OCR terlebih dahulu.')
    return pages


def make_doc(doc_id: str, name: str, pages: list[dict], kind: str, description: str, filename: str|None=None, locked: bool=False):
    chunks=[]
    for p in pages:
        for index, part in enumerate(split_text(p['text'])):
            chunks.append({'id':f'{doc_id}-{p["page"]}-{index}', 'page':p['page'],'text':part})
    if not chunks:
        raise ValueError('Dokumen tidak mempunyai teks yang cukup untuk diindeks.')
    return {'id':doc_id,'name':name,'kind':kind,'description':description,'filename':filename,'locked':locked,
            'created':datetime.now(timezone.utc).isoformat(), 'pages':len(pages),'chunks':chunks}


def _write(docs: list[dict]):
    INDEX.write_text(json.dumps({'version':1,'documents':docs},ensure_ascii=False,indent=2),encoding='utf8')


def bootstrap():
    with LOCK:
        DATA.mkdir(parents=True,exist_ok=True)
        UPLOADS.mkdir(parents=True,exist_ok=True)
        if INDEX.exists():
            return
        docs=[make_doc('research-brief','Research brief · JTIKA 2025',[{'page':1,'text':RESEARCH_BRIEF}],
                       'research','Ringkasan faktual dari publikasi; bukan kebijakan akademik resmi.',locked=True),
              make_doc('practice-data','Contoh modul pembelajaran (simulasi)',[{'page':1,'text':DEMO_GUIDE}],
                       'sample','Simulasi kegiatan belajar; bukan dokumen resmi.',locked=True)]
        if PAPER.exists():
            docs.insert(0,make_doc('original-paper','Artikel JTIKA 2025 · Paper asli',extract_pdf(PAPER),
                                   'paper','Artikel penelitian 11 halaman; sumber primer.',filename='source_paper.pdf',locked=True))
        _write(docs)


def all_docs() -> list[dict]:
    bootstrap()
    with LOCK:
        try:
            return json.loads(INDEX.read_text(encoding='utf8'))['documents']
        except (ValueError, KeyError):
            raise RuntimeError('Indeks dokumen rusak. Backup data/library.json sebelum reset.')


def public_docs() -> list[dict]:
    return [{k:v for k,v in d.items() if k!='chunks'} | {'chunks_count':len(d['chunks'])} for d in all_docs()]


def add_document(file_name: str, payload: bytes) -> dict:
    title = safe_title(file_name)
    ext = Path(title).suffix.lower()
    if ext not in {'.txt','.md','.pdf'}:
        raise ValueError('Format yang didukung: PDF, TXT, MD.')
    if not payload or len(payload)>10*1024*1024:
        raise ValueError('Ukuran file harus lebih dari 0 dan tidak melebihi 10 MB.')
    doc_id='upload-'+uuid.uuid4().hex[:12]
    path=UPLOADS / (doc_id+ext)
    path.write_bytes(payload)
    try:
        if ext == '.pdf': pages=extract_pdf(path)
        else:
            try: content=payload.decode('utf-8-sig')
            except UnicodeDecodeError: content=payload.decode('latin-1')
            pages=[{'page':1,'text':content}]
        doc=make_doc(doc_id,title,pages,'upload','Dokumen pengguna; pastikan izin penggunaan dan akurasinya.',str(path.relative_to(DATA)))
        with LOCK:
            docs=all_docs();docs.append(doc);_write(docs)
        return {k:v for k,v in doc.items() if k!='chunks'} | {'chunks_count':len(doc['chunks'])}
    except Exception:
        path.unlink(missing_ok=True)
        raise


def delete_document(doc_id: str):
    with LOCK:
        docs=all_docs()
        doc=next((d for d in docs if d['id']==doc_id),None)
        if doc is None: raise KeyError('Dokumen tidak ditemukan.')
        if doc['locked']: raise ValueError('Dokumen bawaan tidak dapat dihapus.')
        _write([d for d in docs if d['id'] != doc_id])
        filename=doc.get('filename')
        if filename:
            p=(DATA / filename).resolve()
            if p.is_relative_to(UPLOADS.resolve()): p.unlink(missing_ok=True)
