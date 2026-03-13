# Phase 2 Architecture

The system now includes a Retrieval-Augmented Generation pipeline.

Architecture:

Frontend (React)
↓
FastAPI Backend
↓
Emergency Pipeline

Modules:

input_processing/context_extractor.py

triage/triage_engine.py

rag/retriever.py

rag/vector_store.py

ingestion/build_vector_index.py

## Retrieval Pipeline

User Query
↓
Embedding Generation
(SentenceTransformer)

↓
FAISS Vector Search

↓
Top K Retrieval

↓
Evidence returned to emergency pipeline