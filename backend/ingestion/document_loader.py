from pathlib import Path

def load_documents():

    path = Path("data/raw/first_aid_knowledge.txt")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    sections = text.split("---------------------------------")

    docs = [s.strip() for s in sections if s.strip()]

    return docs