"""
Reference memory: Jaccard similarity (sets / tokens / IDs).
Source chat: similarity metrics evolution (set → numpy → id → batch).
Agent owners: 15 Context Compression Specialist, 11 Research & Evidence Specialist
"""

from __future__ import annotations

from typing import Iterable, List, Sequence, Union

import numpy as np

ArrayLike = Union[Sequence, np.ndarray, Iterable]


def jaccard_similarity(a: ArrayLike, b: ArrayLike) -> float:
    """
    Jaccard for lists/sets/NumPy arrays of tokens.
    Formula: |intersection| / |union|
    """
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


def jaccard_similarity_fast(a: ArrayLike, b: ArrayLike) -> float:
    """Faster Jaccard for larger arrays via NumPy unique + intersect1d."""
    a_unique = np.unique(np.asarray(a))
    b_unique = np.unique(np.asarray(b))
    intersection = np.intersect1d(a_unique, b_unique, assume_unique=True).size
    union = a_unique.size + b_unique.size - intersection
    if union == 0:
        return 0.0
    return float(intersection / union)


def jaccard_similarity_ids(a: ArrayLike, b: ArrayLike) -> float:
    """Fast Jaccard for integer ID arrays (retrieval / memory overlap)."""
    a = np.asarray(a, dtype=np.int64).ravel()
    b = np.asarray(b, dtype=np.int64).ravel()
    a_unique = np.unique(a)
    b_unique = np.unique(b)
    intersection = np.intersect1d(a_unique, b_unique, assume_unique=True).size
    union = a_unique.size + b_unique.size - intersection
    if union == 0:
        return 0.0
    return float(intersection / union)


def batch_jaccard_similarity(
    query_ids: ArrayLike, documents_ids: List[ArrayLike]
) -> np.ndarray:
    """Compare one query against many documents; returns scores array."""
    scores = [jaccard_similarity_ids(query_ids, doc_ids) for doc_ids in documents_ids]
    return np.array(scores, dtype=np.float64)


# Selection guide from chat:
# - small token lists  → jaccard_similarity (Python sets)
# - large general arrays → jaccard_similarity_fast
# - integer IDs (systems) → jaccard_similarity_ids / batch_jaccard_similarity


def demo() -> None:
    sentence_a = ["user", "wants", "clean", "folder", "structure"]
    sentence_b = ["project", "should", "be", "well", "organized"]
    sentence_c = ["user", "wants", "organized", "folder"]
    print("set A vs B", round(jaccard_similarity(sentence_a, sentence_b), 4))
    print("set A vs C", round(jaccard_similarity(sentence_a, sentence_c), 4))

    query = np.array([1, 5, 9, 12], dtype=np.int64)
    documents = [
        np.array([5, 9, 12, 20], dtype=np.int64),
        np.array([1, 2, 3], dtype=np.int64),
        np.array([9, 12, 15, 18, 22], dtype=np.int64),
    ]
    scores = batch_jaccard_similarity(query, documents)
    ranking = np.argsort(scores)[::-1]
    print("batch scores", scores)
    print("best doc index", ranking[0])


if __name__ == "__main__":
    demo()
