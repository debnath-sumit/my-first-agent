from src.memory.chroma_store import save_brief_to_memory, search_memory, collection

save_brief_to_memory(
    "Today Nvidia stock increased and Dallas weather was overcast."
)

print("Count:", collection.count())

results = search_memory("What happened with Nvidia?")
print(results)