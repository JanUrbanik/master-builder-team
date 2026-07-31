Here’s an optimized **Jaccard similarity for integer ID arrays** (common in retrieval systems):

```python
import numpy as np

def jaccard_similarity_ids(a, b):
    """
    Fast Jaccard similarity for integer ID arrays.
    Assumes inputs are 1D arrays of item IDs.
    """
    a = np.asarray(a, dtype=np.int64).ravel()
    b = np.asarray(b, dtype=np.int64).ravel()

    # Remove duplicates efficiently
    a_unique = np.unique(a)
    b_unique = np.unique(b)

    # Fast intersection for sorted integer arrays
    intersection = np.intersect1d(a_unique, b_unique, assume_unique=True).size
    union = a_unique.size + b_unique.size - intersection

    if union == 0:
        return 0.0
    return intersection / union
```

### Example

```python
# Example: document token IDs or memory item IDs
doc_a = np.array([1, 5, 9, 12, 15, 9, 5], dtype=np.int64)
doc_b = np.array([5, 9, 20, 25, 12], dtype=np.int64)

print(jaccard_similarity_ids(doc_a, doc_b))
```

### Why this version is good
- Uses `int64` for speed and consistency
- Works well with large ID lists
- Avoids slow Python-level set operations
- Suitable for retrieval, ranking, and memory overlap checks

### When to use which version
| Input type | Best function |
|----------|----------------|
| Small text token lists | Python `set` version |
| Large general arrays | NumPy `jaccard_similarity_fast` |
| Integer IDs (recommended for systems) | `jaccard_similarity_ids` |

---

Would you like a batch version that compares one query against many documents at once?