# Memory: Jaccard Similarity

**Code:** `04_Materials/python_references/src/jaccard_similarity.py`  
**Chat origin:** Jaccard evolution (≈420–429)

## Formula

`J(A,B) = |A ∩ B| / |A ∪ B|`

## Function ladder (use the right one)

1. `jaccard_similarity` — small token lists / sets; supports NumPy by converting to lists
2. `jaccard_similarity_fast` — large general arrays via `np.unique` + `np.intersect1d`
3. `jaccard_similarity_ids` — integer ID arrays (retrieval / memory item IDs)
4. `batch_jaccard_similarity` — one query vs many documents; rank with `np.argsort(scores)[::-1]`

## When to use

- Keyword/token overlap
- Tag sets
- Memory item ID overlap
- **Not** for dense embedding vectors (use cosine)

## Example tokens from chat

- A: user, wants, clean, folder, structure
- C: user, wants, organized, folder → higher overlap with A than unrelated sets
