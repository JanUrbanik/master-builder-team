Here’s an updated **Jaccard similarity function** that supports both normal iterables and NumPy arrays:

```python
import numpy as np

def jaccard_similarity(a, b):
    """
    Jaccard similarity that supports:
    - Python lists / sets
    - NumPy arrays
    """
    # Convert NumPy arrays to flat Python lists
    if isinstance(a, np.ndarray):
        a = a.tolist()
    if isinstance(b, np.ndarray):
        b = b.tolist()

    set1 = set(a)
    set2 = set(b)

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    if union == 0:
        return 0.0
    return intersection / union
```

### Example Usage

```python
# With normal lists
print(jaccard_similarity(
    ["user", "wants", "clean", "folder"],
    ["user", "wants", "organized", "folder"]
))

# With NumPy arrays
a = np.array(["user", "wants", "clean", "folder"])
b = np.array(["user", "wants", "organized", "folder"])
print(jaccard_similarity(a, b))
```

### Note
This still treats the inputs as **sets of items** (tokens/values).  
It is not a dense-vector metric like cosine similarity. For embeddings, continue using cosine / dot product.