import chromadb
from datetime import datetime

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="morning_briefs"
)


def save_brief_to_memory(brief_text: str):
    today = datetime.now().strftime("%Y-%m-%d")

    collection.add(
        documents=[brief_text],
        ids=[f"brief_{today}"],
        metadatas=[{"date": today}]
    )

    return f"Brief saved to ChromaDB for {today}"


def search_memory(query: str, limit: int = 3):
    results = collection.query(
        query_texts=[query],
        n_results=limit
    )

    return results

def format_search_results(results):
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "No previous memory found."

    formatted = []

    for doc, metadata in zip(documents, metadatas):
        date = metadata.get("date", "unknown date")
        formatted.append(f"Date: {date}\nBrief:\n{doc}")

    return "\n\n---\n\n".join(formatted)

def get_memory_count():
    return collection.count()


def get_all_memory():
    return collection.get(
        include=["documents", "metadatas"]
    )