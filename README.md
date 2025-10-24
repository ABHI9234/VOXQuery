# VOXQuery - Voice-Enabled Document Q&A Chatbot

Ask questions about your documents and hear the answers! VOXQuery combines powerful AI with voice interaction to create an intelligent document assistant.

## 🌟 Features

- **📄 Document Upload**: Drag & drop PDF files for instant processing
- **🎤 Voice Input**: Ask questions using your voice (like Siri)
- **🔊 Voice Output**: Hear answers spoken aloud automatically
- **🤖 AI-Powered**: Fine-tuned RoBERTa model for accurate question answering
- **🎨 Beautiful UI**: Modern space/aurora themed interface
- **⚡ Fast Processing**: Intelligent chunking and FAISS vector search
- **🌙 Dark Mode**: Eye-friendly dark theme by default

## 🏗️ Tech Stack

**Frontend:** React, TypeScript, Vite, Tailwind CSS, Web Speech API

**Backend:** FastAPI, PyTorch, Transformers (RoBERTa), Sentence-Transformers, FAISS, PyPDF2

## 📋 Prerequisites

- Python 3.9+
- Node.js 16+
- npm or yarn
- 4GB+ RAM
- Modern browser (Chrome, Edge, Safari)

## 🚀 Installation & Setup

### 1. Clone Repositories

```bash
# Frontend
git clone https://github.com/ABHI9234/vox-speak-docs.git
cd vox-speak-docs

# Backend
git clone https://github.com/ABHI9234/voxquery-backend.git backend
cd backend
```

### 2. Download Fine-Tuned Model

The fine-tuned RoBERTa model (1.53GB) is hosted on Google Drive due to GitHub's 100MB file size limit.

**Download:** [Google Drive Link - VOXQuery Model](YOUR_GOOGLE_DRIVE_LINK_HERE)

Extract the downloaded zip file to:
```
backend/models/roberta_finetuned_final/
├── config.json
├── pytorch_model.bin
├── tokenizer_config.json
├── tokenizer.json
├── vocab.txt
└── special_tokens_map.json
```

### 3. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

**requirements.txt:**
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
transformers==4.25.1
sentence-transformers==2.7.0
faiss-cpu
torch
numpy
pydantic
python-multipart
PyPDF2
```

### 4. Frontend Setup

```bash
cd ../frontend
npm install
```

## 🎯 Running Locally

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python main.py
```

Expected output:
```
🔄 Loading AI models...
✅ AI models loaded!
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Expected output:
```
VITE v5.x.x ready in XXX ms
➜  Local:   http://localhost:5173/
```

**Access:** http://localhost:5173

## 📖 Usage Guide

### Upload Document
- Drag & drop PDF onto upload zone or click to browse
- Wait 10-60 seconds for processing
- Success message shows chunk count

### Ask Questions
**Text:** Type question, click Ask or press Enter

**Voice:** Click microphone 🎙️, speak question, watch Siri-style animation, hear answer

### Manage Documents
**Remove:** Click X button on document badge

**Replace:** Upload new document → confirmation modal → click Replace

## 🧪 Testing Backend

```bash
# Health check
curl http://localhost:8000/health

# Upload PDF
curl -X POST http://localhost:8000/upload-pdf -F "file=@document.pdf"

# Ask question
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this about?"}'
```

## 🎨 Customization

**Chunking (backend/main.py):**
```python
def chunk_text(text: str, chunk_size: int = 300, overlap: int = 100):
    # Adjust for precision vs speed
```

**Voice (frontend/src/utils/textToSpeech.ts):**
```typescript
utterance.rate = 1.0;    // Speed (0.1-10)
utterance.pitch = 1.0;   // Pitch (0-2)
utterance.volume = 1.0;  // Volume (0-1)
```

## 🐛 Troubleshooting

**ModuleNotFoundError:** `pip install -r requirements.txt`

**Model not found:** Download from Google Drive and extract to `backend/models/roberta_finetuned_final/`

**Port 8000 in use:** `lsof -ti:8000 | xargs kill -9`

**Backend connection failed:** Ensure backend running at http://localhost:8000

**Voice not working:** Use Chrome/Edge/Safari, allow microphone permissions

## 📊 Performance Tips

- Use PDFs <50 pages for faster processing
- Close other applications to free RAM
- Adjust chunk_size based on document type

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/name`)
5. Open Pull Request

## 📝 License

MIT License - see LICENSE file

## 👤 Author

**Venkata Abhinav Tadiparthi**
- GitHub: [@ABHI9234](https://github.com/ABHI9234)
- Email: venkataabhinavtadiparthi@gmail.com

