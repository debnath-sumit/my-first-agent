from src.agent import run_agent

def test_remember_name():
    response = run_agent(
        "Remember this: my name is Sumit.",
        "llama-3.1-8b-instant"
    )

    assert "Saved" in response