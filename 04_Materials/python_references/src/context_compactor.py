"""
Reference memory: Hybrid context compaction (sliding window + running summary).
Source chat: Agent 15 Context Compression Specialist.
Agent owner: 15 Context Compression Specialist
"""

from __future__ import annotations

from typing import Dict, List, Optional


class ContextCompactor:
    """
    Keep the most recent messages in full.
    Compress older messages into a running structured summary.
    """

    def __init__(self, window_size: int = 6) -> None:
        self.window_size = window_size
        self.summary: str = ""
        self.recent_messages: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str) -> None:
        self.recent_messages.append({"role": role, "content": content})

        if len(self.recent_messages) > self.window_size:
            old_messages = self.recent_messages[: -self.window_size]
            self.recent_messages = self.recent_messages[-self.window_size :]
            old_text = "\n".join(f"{m['role']}: {m['content']}" for m in old_messages)
            self.summary = self.compress(self.summary, old_text)

    def compress(self, previous_summary: str, new_old_text: str) -> str:
        """
        Placeholder for an LLM compression call.
        Production version should preserve:
        Key Decisions, Constraints & Rules, Important Facts,
        Open Questions, Next Actions.
        """
        if not previous_summary:
            return f"Summary so far:\n{new_old_text}"
        return f"{previous_summary}\n\nAdditional context:\n{new_old_text}"

    def get_context(self) -> List[Dict[str, str]]:
        context: List[Dict[str, str]] = []
        if self.summary:
            context.append({"role": "system", "content": self.summary})
        context.extend(self.recent_messages)
        return context


def demo() -> None:
    compactor = ContextCompactor(window_size=4)
    compactor.add_message("user", "I want to build a 16-agent system.")
    compactor.add_message("assistant", "Understood. Let's define the roles.")
    for i in range(6):
        compactor.add_message("user", f"Message {i}")
        compactor.add_message("assistant", f"Reply {i}")
    final_context = compactor.get_context()
    print("context items:", len(final_context))
    print("has summary:", bool(compactor.summary))


if __name__ == "__main__":
    demo()
