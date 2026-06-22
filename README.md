## RAG Document Assistant
An AI-powered Document Question Answering application that allows users to upload PDF documents and ask natural language questions about their content. 
The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant document sections and generate context-aware answers.

## Features

- Upload and analyze PDF documents through an interactive Streamlit interface
- Automated document ingestion and text extraction
- Intelligent document chunking for efficient retrieval
- Semantic search powered by vector embeddings
- FAISS-based vector database for similarity search
- Retrieval-Augmented Generation (RAG) pipeline for grounded responses
- Context-aware question answering using Phi-3 via Ollama
- Transparent retrieval workflow with retrieved context display
- Local LLM inference without reliance on external APIs
- Modular architecture supporting future enhancements and scalability

## Tech Stack

**Frontend**
- Streamlit

**Backend**
- Python
  
**AI & LLM**
- LangChain
- Ollama
- Phi-3
  
**Vector Database**
- FAISS
  
**Embeddings**
- HuggingFace Embeddings
  
**Document Processing**
- PyPDFLoader

## Project Architecture

```text
PDF Document
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Relevant Context
      │
      ▼
Phi-3 LLM (Ollama)
      │
      ▼
Generated Answer
      │
      ▼
Streamlit Interface
``` 

## How It Works

1. User uploads a PDF document.  
2. The document is loaded and split into manageable chunks.  
3. Embeddings are generated for each chunk.  
4. Embeddings are stored in a FAISS vector database.  
5. When a user asks a question:  
6. The query is converted into embeddings.  
7. Similar document chunks are retrieved.  
8. Retrieved context is passed to the LLM.  
9. The model generates an answer grounded in the document content.  

## Installation

### Clone the Repository

```bash
git clone https://github.com/Darsh0714/rag-document-assistant
cd rag-document-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

Ensure Ollama is installed and the Phi-3 model is available.

```bash
ollama pull phi3
ollama serve
```

### Run the Application

```bash
streamlit run app.py
```

## Sample Use Cases
- Business report analysis
- Research paper summarization
- Policy document Q&A
- Internal knowledge assistant
- Educational content exploration
- Technical documentation search

## Learning Outcomes

- Retrieval-Augmented Generation (RAG)
- LangChain pipelines
- Vector databases (FAISS)
- Embedding models
- Prompt engineering
- Streamlit application development
- Local LLM deployment using Ollama
- Semantic search systems

## Future Enhancements
- Multiple PDF support
- Conversation memory
- Source citations with page numbers
- Hybrid search (keyword + vector search)
- Reranking for improved retrieval quality
- Docker deployment
- Cloud deployment
- User authentication

## Author

_**Darshini R**  
**Gen AI Enthusiast**_
