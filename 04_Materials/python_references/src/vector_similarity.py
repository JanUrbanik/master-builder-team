"""
Reference memory: Dense vector similarity metrics.
Source chat: Vector database embeddings thread.
Agent owners: 15 Context Compression Specialist, 11 Research & Evidence Specialist
"""

from __future__ import annotations

import numpy as np


# Example embedding-like vectors from chat
A = np.array([0.8, 0.6, 0.2])  # "User wants a clean folder structure"
B = np.array([0.7, 0.5, 0.3])  # "The project should be well organized"
C = np.array([0.1, 0.2, 0.9])  # "The battery is dead"


def dot_product(u: np.ndarray, v: np.ndarray) -> float:
    return float(np.dot(u, v))


def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    denom = float(np.linalg.norm(u) * np.linalg.norm(v))
    if denom == 0.0:
        return 0.0
    return float(np.dot(u, v) / denom)


def euclidean_distance(u: np.ndarray, v: np.ndarray) -> float:
    return float(np.linalg.norm(u - v))


def demo() -> None:
    print("=== Dot Product ===")
    print("A · B =", round(dot_product(A, B), 4))
    print("A · C =", round(dot_product(A, C), 4))

    print("\n=== Cosine Similarity ===")
    print("A vs B =", round(cosine_similarity(A, B), 4))
    print("A vs C =", round(cosine_similarity(A, C), 4))

    print("\n=== Euclidean Distance ===")
    print("A vs B =", round(euclidean_distance(A, B), 4))
    print("A vs C =", round(euclidean_distance(A, C), 4))


if __name__ == "__main__":
    demo()
