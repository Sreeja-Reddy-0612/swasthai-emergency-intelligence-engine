from ai_engine.vector_store.vector_db import get_vector_store,get_documents
from sentence_transformers import SentenceTransformer
import numpy as np

model=SentenceTransformer("all-MiniLM-L6-v2")


def retrieve(query,k=5):

    index=get_vector_store()

    docs=get_documents()

    query_embedding=model.encode([query])

    scores,ids=index.search(np.array(query_embedding),k)

    results=[]

    for i in ids[0]:
        results.append(docs[i])

    return results
