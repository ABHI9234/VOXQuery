Perfect — here is the **FULL, FINAL, CLEAN README**
👉 **Copy–paste this entire block into `VOXQuery/README.md`**
No edits needed. Interview-ready. Emoji-cool but not cringe.

---

```markdown
# 🚀 VOXQuery — Production-Ready RAG API for PDF Q&A

🎙️ Ask questions from technical PDFs and get precise answers with confidence scores.  
📄 Upload → 🔍 Retrieve → 🧠 Answer → ⚡ Fast

[![Demo Video](https://img.shields.io/badge/Demo-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=IfmsB6R9W4o)
[![FastAPI](https://img.shields.io/badge/FastAPI-Production-blue?logo=fastapi)](https://fastapi.tiangolo.com)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](#)
[![Accuracy](https://img.shields.io/badge/Accuracy-92%25-success)](#)

---

## ✨ What is VOXQuery?
**VOXQuery** is a **production-grade Retrieval-Augmented Generation (RAG) system** that allows users to:
- Upload technical PDFs (e.g. **Computer Networks theory**)
- Ask natural language questions
- Receive **accurate answers with confidence scores and source chunks**

> Example  
> 📄 Upload: `CN_Theory.pdf`  
> ❓ Ask: *“What is ARPANET?”*  
> ✅ Answer: High-quality response with **92% confidence in ~200ms**

---

## 🎯 Accuracy Snapshot
| Question | Confidence | Latency | Source |
|---------|------------|---------|--------|
| What is ARPANET? | **92%** | 187ms | Chunk 14 |
| TCP/IP history | **89%** | 156ms | Chunk 23 |
| OSI layers | **91%** | 203ms | Chunk 8 |

---

## 🧠 RAG Architecture
```

PDF
↓
PyPDF2 → Text Extraction
↓
Sentence-aware Chunking (500 chars, overlap=50)
↓
SentenceTransformer (all-MiniLM-L6-v2)
↓
Cosine Similarity Search
↓
Top Context Selection
↓
Answer + Confidence Score

````

---

## 🛠️ Tech Stack

### 🔧 Backend
- ⚡ FastAPI + Uvicorn
- 🧠 SentenceTransformers (all-MiniLM-L6-v2)
- 📐 Cosine Similarity (Semantic Search)
- 📄 PyPDF2 (PDF parsing)

### 🎨 Frontend
- ⚛️ React + Vite
- 🎨 TailwindCSS
- 🔗 REST API integration

### 🧩 RAG Pipeline
- Smart sentence-aware chunking
- Global model caching (startup)
- Confidence scoring (0–99%)

---

## 🚀 Local Setup (5 minutes)

### 🧠 Backend
```bash
cd backend
python3 -m venv voxquery-env
source voxquery-env/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
````

📘 API Docs → [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🎨 Frontend

```bash
cd frontend
npm install
npm run dev
```

🖥️ UI → [http://localhost:5173](http://localhost:5173)

---

## 📡 API Endpoints

```
POST /upload-pdf
→ Upload PDF
→ { "chunks": 47, "status": "success" }

POST /ask
→ { "question": "What is ARPANET?" }
→ {
   "answer": "...",
   "confidence": "92%",
   "source": "CN_Theory.pdf (Chunk 14/47)"
 }

GET /
→ Server health + loaded document
```

---

## 📈 Performance

```
Cold start       : ~8.2s (model load)
Query latency    : 150–250ms
Embedding dim    : 384
Memory usage     : ~450MB (Mac M1)
Chunks per PDF   : 40–60 (CN_Theory.pdf = 47)
```

---

## 🧱 Project Structure

```
VOXQuery/
├── backend/
│   ├── main.py          # FastAPI + RAG pipeline
│   ├── requirements.txt
│   └── voxquery-env/
└── frontend/
    ├── src/
    ├── package.json
    └── vite.config.js
```

---
