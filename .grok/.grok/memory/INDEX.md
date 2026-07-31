# Project Memory Index

Durable technical memory extracted from the shared Grok chat (Rex / Master Builder Team).

**Source:** https://grok.com/share/c2hhcmQtMg_4b87a6bd-bab6-4251-9a79-98fe32435b74

## How agents should use this memory

1. Treat files here as **canonical technical references** (not chat history).
2. Prefer runnable modules under `04_Materials/python_references/src/`.
3. Prefer concept notes under `.grok/memory/*.md` for rules, when-to-use, and agent ownership.
4. When implementing code, **Code & Execution Specialist** must follow resource-management memory.
5. When scoring similarity / compressing context, use vector / Jaccard / MinHash / compaction memory.
6. When updating belief under conflicting evidence, use Bayesian + Kalman memory as conceptual tools.

## Memory catalog

| Memory file | Python module | Primary agents |
|-------------|---------------|----------------|
| `resource_management.md` | `src/resource_management.py` | 08 Code & Execution |
| `vector_similarity.md` | `src/vector_similarity.py` | 11 Research, 15 Compression |
| `jaccard_similarity.md` | `src/jaccard_similarity.py` | 11 Research, 15 Compression |
| `minhash_lsh.md` | `src/minhash_lsh.py` | 15 Compression |
| `context_compaction.md` | `src/context_compactor.py` | 15 Compression |
| `kalman_bayesian_updating.md` | `src/kalman_filter.py` | 11 Research |
| `metric_selection_guide.md` | (see guide) | 11, 15, 08 |

## Important provenance note

In the shared chat, almost all **executable Python** was produced during the conversation as **requested reference implementations** (user asked for examples; Rex/assistant wrote the code). No large standalone `.py` file was uploaded by the user. Those references are still treated as **project memory** because they were deliberately developed, iterated, and locked into agent capabilities (especially Agent 08 and Agent 15).
