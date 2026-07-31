# Python Reference Library (from shared chat)

All Python code developed as technical references while building the Master Builder Team agents.

## Layout

```
python_references/
├── README.md
├── src/                      # Clean, consolidated runnable modules (canonical)
│   ├── resource_management.py
│   ├── vector_similarity.py
│   ├── jaccard_similarity.py
│   ├── minhash_lsh.py
│   ├── context_compactor.py
│   └── kalman_filter.py
├── msg_*_full.md             # Original chat messages that contained code
└── *_b*.py.txt               # Raw extracted fenced blocks
```

## Linked Grok memory

See `.grok/memory/INDEX.md` for agent-facing memory notes.

## Provenance

User requested reference implementations during the chat (e.g. "Add Python code implementation", "Python MinHash signature example", context manager patterns, Kalman examples). Assistant-generated code was iterated and partially locked into agent prompts. This folder freezes those references as project memory.
