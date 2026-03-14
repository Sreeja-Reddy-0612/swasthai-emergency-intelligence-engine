from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

from ingestion.document_loader import load_documents
from ingestion.chunking import chunk_documents


_model = None
_index = None
_chunks = None


def load_retriever():
    global _model, _index, _chunks

    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        _index = faiss.read_index("data/processed/medical_index.faiss")

        docs = load_documents()
        _chunks = chunk_documents(docs)

    return _model, _index, _chunks


def retrieve(query, k=5):
    model, index, chunks = load_retriever()

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = []

    for i in indices[0]:
        if i < len(chunks):
            results.append(chunks[i])

    return results
