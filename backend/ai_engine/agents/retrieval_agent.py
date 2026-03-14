from ..rag.retriever import retrieve
from ..rag.reranker import rerank


def run_retrieval_agent(state):

    query = state["message"]

    docs = retrieve(query, k=5)

    ranked_docs = rerank(query, docs)

    state["evidence"] = ranked_docs[:3]

    state["agent_trace"].append(
        "Retrieval Agent: retrieved and ranked evidence"
    )

    return state
