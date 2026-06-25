from dotenv import load_dotenv
from pinecone import Pinecone
from datetime import datetime
import os

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))


def save_memory(text: str):
    today = datetime.now().strftime("%Y-%m-%d")

    index.upsert_records(
        namespace="morning-briefs",
        records=[
            {
                "_id": f"brief-{today}",
                "text": text,
                "date": today
            }
        ]
    )

    return f"Saved memory for {today}"


def search_memory(query: str, limit: int = 3):
    results = index.search(
        namespace="morning-briefs",
        query={
            "top_k": limit,
            "inputs": {
                "text": query
            }
        }
    )

    return results