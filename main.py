from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import PyPDF2
import io
import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import torch

app = FastAPI(title="VOXQuery - Sentence Transformer RAG")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Global state for frontend compatibility
documents = [{"filename": "No document", "chunks": []}]
model = None
chunk_embeddings = None

class Query(BaseModel):
    question: str

# Load model ONCE at startup (384-dim all-MiniLM-L6-v2)
@app.on_event("startup")
async def load_model():
    global model
    print("🔄 Loading SentenceTransformer model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ SentenceTransformer READY")

def extract_pdf(content):
    """Extract clean text from PDF"""
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(content))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return re.sub(r'\s+', ' ', text.strip())
    except:
        return ""

def smart_chunk(text, chunk_size=500, overlap=50):
    """Create sentence-aware chunks"""
    # Split into sentences first
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""
    
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 15: continue
            
        if len(current_chunk) + len(sent) < chunk_size:
            current_chunk += " " + sent
        else:
            if len(current_chunk) > 100:
                chunks.append(current_chunk.strip())
            current_chunk = sent
    
    if len(current_chunk) > 100:
        chunks.append(current_chunk.strip())
    
    return chunks

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global documents, chunk_embeddings
    
    content = await file.read()
    full_text = extract_pdf(content)
    
    if len(full_text) < 50:
        documents[0] = {"filename": file.filename, "chunks": []}
        return {"error": "No text extracted"}
    
    # Create sentence-aware chunks
    chunks = smart_chunk(full_text)
    documents[0] = {
        "filename": file.filename,
        "chunks": chunks
    }
    
    # Generate embeddings for ALL chunks
    if model:
        print(f"🔄 Embedding {len(chunks)} chunks...")
        chunk_embeddings = model.encode(chunks, convert_to_tensor=False, show_progress_bar=True)
        print(f"✅ {len(chunk_embeddings)} embeddings created")
    
    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "status": "success"
    }

@app.post("/ask")
def ask(query: Query):
    global chunk_embeddings
    
    if not documents[0].get("chunks"):
        return {
            "answer": "Upload PDF first to ask questions",
            "confidence": "95%",
            "source": "system"
        }
    
    chunks = documents[0]["chunks"]
    
    # Encode question
    question_embedding = model.encode([query.question], convert_to_tensor=False)
    
    # Semantic similarity search
    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]
    best_idx = np.argmax(similarities)
    best_chunk = chunks[best_idx]
    
    # Extract precise answer (first relevant sentence)
    q_words = re.findall(r'\b[a-zA-Z]{3,}\b', query.question.lower())
    sentences = re.split(r'[.!?]+', best_chunk)
    
    best_sentence = ""
    for sent in sentences:
        sent = sent.strip()
        if len(sent) > 40 and any(word in sent.lower() for word in q_words):
            best_sentence = sent
            break
    
    # Fallback to chunk preview
    answer = best_sentence or best_chunk[:300]
    answer = re.sub(r'\s+', ' ', answer.strip())
    
    confidence = float(similarities[best_idx]) * 100
    
    return {
        "answer": answer[:280] + "..." if len(answer) > 280 else answer,
        "confidence": f"{min(99, confidence):.0f}%",
        "source": f"{documents[0]['filename']} (Chunk {best_idx+1}/{len(chunks)})"
    }

@app.get("/")
def root():
    return {
        "status": "🟢 SentenceTransformer RAG LIVE",
        "model": "all-MiniLM-L6-v2",
        "current_doc": documents[0]["filename"],
        "chunks": len(documents[0]["chunks"])
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
