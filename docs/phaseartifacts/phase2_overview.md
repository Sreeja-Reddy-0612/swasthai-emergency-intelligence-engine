# Phase 2 — Medical RAG Implementation

Phase 2 introduces Retrieval-Augmented Generation (RAG) to the SwasthAI Emergency Intelligence Engine.

The system now retrieves medical knowledge from a vector database instead of relying on static instructions.

## Key Features

- Medical knowledge ingestion
- Text chunking
- Embedding generation using SentenceTransformers
- FAISS vector database
- Semantic retrieval
- Integration with emergency pipeline

## Pipeline

User Input
↓
Context Extraction
↓
Triage Classification
↓
Vector Search
↓
Medical Evidence Retrieval
↓
Grounded Instructions

## Dataset

Initial knowledge base contains:

- Snake bite first aid
- CPR emergency protocol
- Burn treatment

Sources:

- WHO First Aid Guidelines
- American Heart Association
- Red Cross First Aid Manual

## Vector Database

FAISS index built using:

SentenceTransformer model:

all-MiniLM-L6-v2

Stored in:

backend/data/processed/medical_index.faiss

## Retrieval

Top K = 2

Semantic similarity search is performed between the user query and medical knowledge chunks.

## Output Example

Input:

snake bite happened

Output:

Emergency Level: EMERGENCY

Instructions retrieved from WHO First Aid Guidelines.

## Status

Phase 2 Completed