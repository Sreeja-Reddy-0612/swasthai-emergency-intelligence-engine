from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("data/processed/medical_index.faiss")

from ingestion.document_loader import load_documents
from ingestion.chunking import chunk_documents

docs = load_documents()
chunks = chunk_documents(docs)


def retrieve(query, k=2):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = []

    for i in indices[0]:

        results.append(chunks[i])

    return results