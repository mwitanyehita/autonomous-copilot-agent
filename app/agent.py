from app.llm import router
from app.memory import MemoryStore


class JarvisAgent:
    def __init__(self, memory: MemoryStore) -> None:
        self.memory = memory

    def chat(self, user_message: str) -> str:
        self.memory.add("user", user_message)

        history = self.memory.get_recent(12)
        context = "\n".join(f"{msg['role']}: {msg['content']}" for msg in history)

        prompt = (
            "You are JARVIS, a helpful local Linux terminal assistant. "
            "Be concise, practical, and useful. "
            "Prefer direct actions, explanations, and command suggestions.\n\n"
            f"Conversation history:\n{context}\n\n"
            f"User: {user_message}\n\nAssistant:"
        )

        try:
            response = router.generate(prompt)
        except Exception as exc:
            response = (
                "I couldn't reach the configured LLM backend. "
                f"Install Ollama or set ANTHROPIC_API_KEY. Details: {exc}"
            )

        self.memory.add("assistant", response)
        return response

