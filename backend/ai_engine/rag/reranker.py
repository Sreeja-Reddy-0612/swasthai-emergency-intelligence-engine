from sentence_transformers import CrossEncoder

_reranker = None


def load_reranker():
    global _reranker

    if _reranker is None:
        _reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    return _reranker


def rerank(query, docs):
    if len(docs) == 0:
        return docs

    reranker = load_reranker()

    pairs = [[query, doc] for doc in docs]

    scores = reranker.predict(pairs)

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

    return [doc for doc, score in ranked]
