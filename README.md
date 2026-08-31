# 🎥 AI Video Assistant

An AI-powered video and meeting assistant that converts YouTube videos or local audio/video files into structured meeting insights and enables users to ask questions about the meeting using Retrieval-Augmented Generation (RAG).

## 🚀 Features

- Process YouTube URLs
- Process local audio/video files
- English speech transcription using OpenAI Whisper
- Hinglish / Indian-language speech processing using Sarvam AI
- Automatic meeting title generation
- AI-generated meeting summary
- Action item extraction
- Key decision extraction
- Open question extraction
- Semantic retrieval using embeddings
- Chroma vector database
- RAG-based meeting question answering
- Streamlit UI
- CLI pipeline

## 🏗️ Architecture

```text
                         User
                           │
                           ▼
              YouTube URL / Local File
                           │
                           ▼
                 Audio Processing
                           │
                 ┌─────────┴─────────┐
                 │                   │
          YouTube URL           Local File
                 │                   │
              yt-dlp              pydub
                 │                   │
                 └─────────┬─────────┘
                           ▼
                      WAV Audio
                           │
                           ▼
                  Audio Chunking
                    (10 min)
                           │
                           ▼
                    Transcription
                           │
                ┌──────────┴──────────┐
                │                     │
             English               Hinglish
                │                     │
             Whisper               Sarvam AI
                │                     │
                └──────────┬──────────┘
                           ▼
                    Full Transcript
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           Title        Summary     Meeting Insights
                                        │
                              ┌─────────┼─────────┐
                              │         │         │
                              ▼         ▼         ▼
                           Actions  Decisions  Questions
                              │
                              ▼
                       Transcript Chunks
                              │
                              ▼
                     HuggingFace Embeddings
                    (all-MiniLM-L6-v2)
                              │
                              ▼
                          Chroma DB
                              │
                              ▼
                         Retriever
                           (Top-K)
                              │
                              ▼
                       User Question
                              │
                              ▼
                      Relevant Context
                              │
                              ▼
                         Mistral AI
                              │
                              ▼
                       Grounded Answer
```

## 📂 Project Structure

```text
AI-Video-Assistant/
│
├── core/
│   ├── extractor.py          # Action items, decisions and questions
│   ├── llm.py                # Centralized Mistral LLM configuration
│   ├── rag_engine.py         # RAG pipeline and question answering
│   ├── summarizer.py         # Meeting title and summary
│   ├── transcriber.py        # Whisper and Sarvam transcription
│   └── vector_store.py       # Embeddings and Chroma vector store
│
├── utils/
│   └── audio_processor.py    # Download, conversion and audio chunking
│
├── app.py                    # Streamlit application
├── main.py                   # CLI pipeline
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

## 🔄 How It Works

### 1. Input

The application accepts:

- YouTube URL
- Local audio/video file

### 2. Audio Processing

For YouTube URLs, `yt-dlp` downloads the audio.

For local files, `pydub` converts the media to WAV, mono, 16 kHz audio.

The audio is then divided into 10-minute chunks.

### 3. Transcription

**English:**

```text
English Audio → Whisper → English Transcript
```

**Hinglish / supported Indian-language speech:**

```text
Hinglish / Indian-language Speech
            ↓
        Sarvam AI
            ↓
     English Transcript
```

### 4. Meeting Intelligence

The transcript is processed by Mistral AI to generate:

- Meeting title
- Meeting summary
- Action items
- Key decisions
- Open questions

### 5. RAG

The transcript is split into smaller chunks and converted into embeddings using `all-MiniLM-L6-v2`.

The embeddings are stored in Chroma.

When a user asks a question:

```text
Question
   ↓
Retriever
   ↓
Top relevant transcript chunks
   ↓
Context
   ↓
Mistral AI
   ↓
Answer
```

The RAG prompt instructs the model to answer only from the retrieved meeting transcript context.

## 🧩 Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| UI | Streamlit |
| LLM | Mistral AI |
| Speech-to-Text | OpenAI Whisper |
| Indian-language Speech | Sarvam AI |
| Framework | LangChain |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector Database | Chroma |
| YouTube Processing | yt-dlp |
| Audio Processing | pydub |

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
```

Optional:

```env
WHISPER_MODEL=small
SARVAM_STT_MODEL=saaras:v2.5
```

Never commit `.env` or expose API keys publicly.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Video-Assistant
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create `.env` and add your Mistral and Sarvam API keys.

## ▶️ Run the Application

### Streamlit

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit.

### CLI

```bash
python main.py
```

Enter the YouTube URL or local file path and select the language.

## ⚠️ Notes

- FFmpeg may be required by `pydub` for audio/video conversion.
- Whisper may show `FP16 is not supported on CPU; using FP32 instead` when running on CPU. This is a warning and Whisper automatically uses FP32.
- Local Whisper processing time depends on video duration and available hardware.
- Sarvam API usage requires a valid API key.

## 🔒 GitHub Security

Recommended `.gitignore` entries:

```gitignore
.env
venv/
__pycache__/
*.pyc
downloads/
vector_db/
.vscode/
```

Generated files such as downloaded audio, local vector databases, Python cache, and virtual environments should not be committed.

## 🔮 Future Improvements

- Better error handling and retry mechanisms
- Meeting-specific vector-store isolation
- Centralized configuration
- Background processing for long videos
- Progress indicators
- Persistent meeting history
- Speaker diarization
- Timestamp-aware retrieval
- Additional language support
- Evaluation of generated summaries and answers
- Production deployment

## 🎯 Project Objective

The AI Video Assistant transforms long-form meeting/video content into searchable and actionable information.

Instead of manually watching an entire meeting, users can:

```text
Video
 ↓
Transcript
 ↓
Summary + Meeting Insights
 ↓
Searchable Knowledge
 ↓
Question Answering
```

## 👨‍💻 Project Highlights

This project demonstrates practical implementation of:

- Large Language Model integration
- Speech-to-Text
- AI API integration
- LangChain LCEL pipelines
- Retrieval-Augmented Generation
- Vector embeddings
- Vector databases
- Prompt engineering
- Modular Python architecture
- Streamlit application development
- Local ML model inference

## 📄 License

This project is intended for educational and portfolio purposes.
