import faiss
import numpy as np

from ingestion.document_loader import load_documents
from ingestion.chunking import chunk_documents
from ingestion.embedding_generator import generate_embeddings

def build_index():

    docs = load_documents()

    chunks = chunk_documents(docs)

    embeddings = generate_embeddings(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, "data/processed/medical_index.faiss")

    return chunks


if __name__ == "__main__":

    chunks = build_index()

    print("Vector DB created")