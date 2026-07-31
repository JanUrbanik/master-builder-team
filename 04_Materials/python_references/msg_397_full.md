Here’s a clear **code example for Compaction** (hybrid context compression):

### Concept
- Keep the most recent messages as-is (sliding window)
- Compress older messages into a running summary
- Combine them into the final context

### Python Example

```python
class ContextCompactor:
    def __init__(self, window_size=6):
        self.window_size = window_size
        self.summary = ""
        self.recent_messages = []

    def add_message(self, role, content):
        self.recent_messages.append({"role": role, "content": content})

        # If too many recent messages, compact the oldest ones
        if len(self.recent_messages) > self.window_size:
            old_messages = self.recent_messages[:-self.window_size]
            self.recent_messages = self.recent_messages[-self.window_size:]

            # Compress old messages into the running summary
            old_text = "\n".join(
                f"{m['role']}: {m['content']}" for m in old_messages
            )
            self.summary = self.compress(self.summary, old_text)

    def compress(self, previous_summary, new_old_text):
        """
        This is where an LLM call would normally happen.
        For illustration, we just join them.
        """
        if not previous_summary:
            return f"Summary so far:\n{new_old_text}"
        return f"{previous_summary}\n\nAdditional context:\n{new_old_text}"

    def get_context(self):
        context = []
        if self.summary:
            context.append({
                "role": "system",
                "content": self.summary
            })
        context.extend(self.recent_messages)
        return context
```

### How to use it

```python
compactor = ContextCompactor(window_size=4)

compactor.add_message("user", "I want to build a 16-agent system.")
compactor.add_message("assistant", "Understood. Let's define the roles.")
# ... more messages ...

final_context = compactor.get_context()
```

### Resulting Structure
```text
[Compressed older history]
+
[Most recent N messages kept in full]
```

This is one of the best practical methods for long-running agent systems.

---

Would you like a version of this example that is more specifically written for agent handoff summaries?