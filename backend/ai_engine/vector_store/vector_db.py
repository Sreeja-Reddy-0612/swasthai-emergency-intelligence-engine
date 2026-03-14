from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model=SentenceTransformer("all-MiniLM-L6-v2")

vector_store=None
documents=[]


def build_vector_store(text_chunks):

    global vector_store
    global documents

    embeddings=model.encode(text_chunks)

    dimension=embeddings.shape[1]

    index=faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    vector_store=index
    documents=text_chunks


def get_vector_store():
    return vector_store


def get_documents():
    return documents
