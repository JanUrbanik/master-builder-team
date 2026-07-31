# Memory: MinHash (Approximate Jaccard)

**Code:** `04_Materials/python_references/src/minhash_lsh.py`  
**Chat origin:** MinHash locality hashing (≈430–433)

## Idea

- Build a signature of minimum hash values over random seeds
- Approximate Jaccard by fraction of equal signature positions
- Useful for large sets where exact Jaccard is expensive

## API

- `minhash_signature(items, num_hashes=8|16)`
- `minhash_similarity(sig_a, sig_b)`

## Expected behavior (chat demo)

- Similar token sets (A vs B folder wording) → higher score
- Unrelated sets (A vs battery-dead) → much lower score

## Relation to other memory

- Exact small sets → Jaccard
- Approximate large sets → MinHash
- Dense semantics → Cosine
