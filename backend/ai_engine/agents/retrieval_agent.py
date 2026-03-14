from ..rag.retriever import retrieve
from ..rag.reranker import rerank


def run_retrieval_agent(state):

    query = state["message"]

    # Retrieve documents
    docs = retrieve(query)

    # docs are already text strings
    texts = docs

    # Rank them using cross-encoder
    ranked_docs = rerank(query, texts)

    state["evidence"] = ranked_docs

    state["agent_trace"].append(
        "Retrieval Agent: retrieved and ranked medical evidence"
    )

    return state
