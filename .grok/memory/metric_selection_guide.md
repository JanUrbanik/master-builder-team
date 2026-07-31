# Memory: Metric & Method Selection Guide

Quick chooser so agents do not misuse reference code.

| Need | Use | Module |
|------|-----|--------|
| Resource cleanup / files / handles | Context managers | `resource_management.py` |
| Semantic similarity of embeddings | Cosine (or dot) | `vector_similarity.py` |
| Token/tag overlap | Jaccard set version | `jaccard_similarity.py` |
| Large array token overlap | Jaccard fast | `jaccard_similarity.py` |
| Integer ID overlap / retrieval | Jaccard IDs + batch | `jaccard_similarity.py` |
| Approximate large-set overlap | MinHash | `minhash_lsh.py` |
| Long chat memory pressure | ContextCompactor hybrid | `context_compactor.py` |
| Conflicting evidence confidence | Bayesian update steps | `kalman_bayesian_updating.md` |
| Sequential noisy estimate fusion | Kalman predict/update | `kalman_filter.py` |

## Anti-confusion rules

- Do **not** run Jaccard on raw embedding floats as if they were sets
- Do **not** use cosine on unordered token bags without embedding them first
- Do **not** compress away user decisions
- Do **not** open resources without `with` / `async with` in production code
