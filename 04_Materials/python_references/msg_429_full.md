Here’s a **batch processing version** that compares one query against many documents:

```python
import numpy as np

def jaccard_similarity_ids(a, b):
    """Fast Jaccard for two integer ID arrays."""
    a_unique = np.unique(np.asarray(a, dtype=np.int64))
    b_unique = np.unique(np.asarray(b, dtype=np.int64))

    intersection = np.intersect1d(a_unique, b_unique, assume_unique=True).size
    union = a_unique.size + b_unique.size - intersection

    if union == 0:
        return 0.0
    return intersection / union

def batch_jaccard_similarity(query_ids, documents_ids):
    """
    Compare one query against many documents.

    Parameters:
    - query_ids: 1D array-like of integer IDs
    - documents_ids: list of arrays (each document is a list/array of IDs)

    Returns:
    - NumPy array of Jaccard scores
    """
    scores = [
        jaccard_similarity_ids(query_ids, doc_ids)
        for doc_ids in documents_ids
    ]
    return np.array(scores, dtype=np.float64)
```

### Example Usage

```python
query = np.array([1, 5, 9, 12], dtype=np.int64)

documents = [
    np.array([5, 9, 12, 20], dtype=np.int64),      # similar
    np.array([1, 2, 3], dtype=np.int64),           # less similar
    np.array([9, 12, 15, 18, 22], dtype=np.int64)  # medium
]

scores = batch_jaccard_similarity(query, documents)
print(scores)

# Get ranking (best match first)
ranking = np.argsort(scores)[::-1]
print("Best document index:", ranking[0])
print("All ranked indices:", ranking)
```

### Expected Behavior
- Returns one similarity score per document
- Higher score = more overlap with the query
- You can sort the scores to rank the best matches

---

Would you like a faster version that avoids Python loops as much as possible for very large document sets?