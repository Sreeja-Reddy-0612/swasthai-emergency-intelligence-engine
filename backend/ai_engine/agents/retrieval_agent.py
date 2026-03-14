from ..rag.retriever import retrieve
from ..rag.reranker import rerank


def run_retrieval_agent(state):

    query=state["message"]

    docs=retrieve(query)

    ranked_docs=rerank(query,docs)

    state["evidence"]=ranked_docs

    state["agent_trace"].append(
        "Retrieval Agent: retrieved medical evidence"
    )

    return state
