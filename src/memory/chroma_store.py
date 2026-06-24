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