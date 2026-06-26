from src.memory.pinecone_store import format_memory_results

class FakeHit:
    def __init__(self):
        self.fields = {
            "text": "My name is Sumit",
            "date": "2026-06-25"
        }

class FakeResult:
    def __init__(self):
        self.hits = [FakeHit()]

class FakeResponse:
    def __init__(self):
        self.result = FakeResult()

def test_format_memory_results():
    response = FakeResponse()

    result = format_memory_results(response)

    assert "My name is Sumit" in result
    assert "2026-06-25" in result