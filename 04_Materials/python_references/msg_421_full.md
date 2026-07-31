Here’s the updated Python example with a **Jaccard similarity** function added:

```python
import numpy as np

# Example vectors (for cosine / dot product / euclidean)
A = np.array([0.8, 0.6, 0.2])
B = np.array([0.7, 0.5, 0.3])
C = np.array([0.1, 0.2, 0.9])

def dot_product(u, v):
    return np.dot(u, v)

def cosine_similarity(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def euclidean_distance(u, v):
    return np.linalg.norm(u - v)

def jaccard_similarity(set1, set2):
    """
    Jaccard similarity for sets (e.g. words/tokens).
    Formula: intersection / union
    """
    set1 = set(set1)
    set2 = set(set2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0.0
    return intersection / union

# Vector metrics
print("=== Dot Product ===")
print("A · B =", round(dot_product(A, B), 4))
print("A · C =", round(dot_product(A, C), 4))

print("\n=== Cosine Similarity ===")
print("A vs B =", round(cosine_similarity(A, B), 4))
print("A vs C =", round(cosine_similarity(A, C), 4))

print("\n=== Euclidean Distance ===")
print("A vs B =", round(euclidean_distance(A, B), 4))
print("A vs C =", round(euclidean_distance(A, C), 4))

# Jaccard example with token sets
sentence_a = ["user", "wants", "clean", "folder", "structure"]
sentence_b = ["project", "should", "be", "well", "organized"]
sentence_c = ["user", "wants", "organized", "folder"]

print("\n=== Jaccard Similarity (token sets) ===")
print("A vs B =", round(jaccard_similarity(sentence_a, sentence_b), 4))
print("A vs C =", round(jaccard_similarity(sentence_a, sentence_c), 4))
```

### Important Note
- **Cosine / Dot Product / Euclidean** → used for dense embedding vectors  
- **Jaccard** → used for sets (words, tokens, tags), not raw embedding vectors

Jaccard is useful for simple keyword overlap, while cosine similarity is much better for semantic meaning.