from dotenv import load_dotenv
from pinecone import Pinecone
from datetime import datetime
import os

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))


def save_memory(text: str, memory_type: str = "conversation_note"):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    index.upsert_records(
        namespace="agent-memory-v2",
        records=[
            {
                "_id": f"{memory_type}-{timestamp}",
                "text": text,
                "memory_type": memory_type,
                "date": timestamp
            }
        ]
    )

    return f"Saved {memory_type} memory."


def search_memory(query: str, memory_type: str = None, limit: int = 3):
    search_request = {
        "top_k": limit,
        "inputs": {
            "text": query
        }
    }

    if memory_type:
        search_request["filter"] = {
            "memory_type": {"$eq": memory_type}
        }

    return index.search(
        namespace="agent-memory-v2",
        query=search_request
    )

def get_memory_stats():
    stats = index.describe_index_stats()
    return stats

def format_memory_results(results):
    """
    Convert Pinecone search results into readable text.
    """

    if not results.result.hits:
        return "I couldn't find anything in memory."

    memories = []

    for hit in results.result.hits:
        text = hit.fields.get("text", "")
        date = hit.fields.get("date", "Unknown")

        memories.append(
            f"📅 {date}\n{text}"
        )

    return "\n\n".join(memories)