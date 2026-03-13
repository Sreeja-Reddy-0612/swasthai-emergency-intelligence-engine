def chunk_documents(documents):

    chunks = []

    for doc in documents:

        lines = doc.split("\n")

        chunk = " ".join(lines)

        chunks.append(chunk)

    return chunks