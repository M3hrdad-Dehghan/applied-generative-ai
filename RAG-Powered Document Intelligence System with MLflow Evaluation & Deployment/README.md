<div align="center">
  <h1>
    RAG-Powered Document Intelligence System with MLflow Evaluation & Cloud Deployment
  </h1>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Retrieval--Augmented%20Generation-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Embeddings-ChromaDB%20Vector%20Search-lightblue?style=flat-square"/>
  <img src="https://img.shields.io/badge/LLM-Anthropic%20Claude-purple?style=flat-square"/>
  <img src="https://img.shields.io/badge/Evaluation-MLflow-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Deployment-AWS%20ECS-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/UI-Streamlit-red?style=flat-square"/>
</p>

---

## 🧠 Business Problem

Professionals working with large document corpora — such as medical, legal, or research content — cannot efficiently extract precise answers from hundreds of pages of unstructured text. Traditional keyword search returns raw documents rather than direct, contextually accurate answers, creating significant friction in knowledge retrieval workflows.

---

## 🎯 Objective

The objective of this project was to design and deploy a production-grade Retrieval-Augmented Generation (RAG) system that allows users to ask natural language questions against a private document corpus and receive accurate, source-cited answers — combining the precision of vector search with the reasoning power of a large language model.

---

## 📊 Data & Inputs

- 15 domain-specific medical oncology PDF documents spanning topics including cancer biology, chemotherapy, immunotherapy, surgical oncology, and clinical trials
- Natural language queries submitted through a conversational chat interface
- High-dimensional sentence embeddings generated via `all-MiniLM-L6-v2` (Sentence Transformers)
- Pre-built ChromaDB vector store with cosine similarity indexing, baked into the Docker image for zero-latency startup

---

## ⚙️ Technical Approach

- **Ingestion & Chunking** — Parsed PDFs using LangChain's PyPDFLoader and applied recursive character text splitting with configurable chunk size and overlap to preserve semantic coherence across document boundaries
- **Embedding & Vector Storage** — Generated dense vector embeddings using Sentence Transformers and stored them in a persistent ChromaDB collection configured with cosine similarity distance for accurate semantic retrieval
- **Retrieval Pipeline** — Implemented a scored retrieval module with configurable Top-K and similarity threshold filtering, returning only contextually relevant chunks for augmentation
- **LLM Augmentation** — Augmented user queries with retrieved context and routed them to the Anthropic Claude API, maintaining multi-turn conversation history for coherent dialogue
- **Hyperparameter Evaluation** — Designed a systematic evaluation framework using 20 ground-truth Q&A pairs and three retrieval metrics (Hit Rate@K, Precision@K, Recall@K); ran 216 MLflow-tracked experiments across embedding models, chunk sizes, overlap values, Top-K settings, and score thresholds to identify the optimal configuration
- **Modular Architecture** — Engineered 8 fully decoupled pipeline components (ingestion, splitting, embedding, vector store, retrieval, system prompt, answering, orchestration) enabling independent testing and parameter updates with a single config file
- **Containerization & Deployment** — Containerized the optimized pipeline using Docker with `uv`-based reproducible dependency management, pushed to Docker Hub, and deployed to HuggingFace

---

## 🛠 Key Skills Demonstrated

- Retrieval-Augmented Generation (RAG) system design
- Vector embeddings, cosine similarity search, and semantic retrieval
- LLM API integration (Anthropic Claude) with multi-turn conversation management
- Hyperparameter evaluation and experiment tracking with MLflow
- Modular Python architecture with single-config parameter management
- Docker containerization with reproducible `uv`-based dependency builds
- Cloud deployment on AWS ECS via Docker Hub
- Streamlit application development with dark-themed chat UI

---

## 🎥 YouTube Walkthrough
 
???
