from dotenv import load_dotenv
import os

from pinecone import Pinecone

print("Current directory:", os.getcwd())

loaded = load_dotenv()

print("Dotenv loaded:", loaded)
print("API Key:", os.getenv("PINECONE_API_KEY"))

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

print(pc.list_indexes())


from src.memory.pinecone_store import save_memory, search_memory

save_memory("Yesterday Nvidia stock increased and Dallas weather was overcast.")

results = search_memory("What happened with Nvidia yesterday?")

print(results)