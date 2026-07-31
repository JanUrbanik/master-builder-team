# Memory: Dense Vector Similarity

**Code:** `04_Materials/python_references/src/vector_similarity.py`  
**Chat origin:** embeddings / similarity metrics thread (≈413–419)

## Metrics

| Metric | Formula idea | Higher means |
|--------|--------------|--------------|
| Dot product | `u·v` | more similar (scale-sensitive) |
| Cosine similarity | `(u·v) / (‖u‖‖v‖)` | more similar direction |
| Euclidean distance | `‖u−v‖` | **less** similar (lower is closer) |

## Reference vectors from chat

- A = `[0.8, 0.6, 0.2]` — clean folder structure
- B = `[0.7, 0.5, 0.3]` — well organized project
- C = `[0.1, 0.2, 0.9]` — battery is dead

Expected qualitative result: **A≈B**, **A≉C**.

## When to use

- Semantic embeddings / vector DB retrieval → cosine (default) or dot product
- Geometric closeness in same space → Euclidean
- **Not** for raw token sets → use Jaccard instead
