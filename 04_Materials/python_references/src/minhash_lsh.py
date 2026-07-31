"""
Reference memory: MinHash signatures for approximate Jaccard.
Source chat: MinHash / locality hashing thread.
Agent owner: 15 Context Compression Specialist
"""

from __future__ import annotations

import hashlib
from typing import Iterable, List, Sequence

import numpy as np


def hash_function(seed: int, value: object) -> int:
    """Deterministic hash function with a seed."""
    data = f"{seed}-{value}".encode("utf-8")
    return int(hashlib.md5(data).hexdigest(), 16)


def minhash_signature(items: Sequence[object], num_hashes: int = 8) -> np.ndarray:
    """Create a MinHash signature for a set of items."""
    unique_items: List[object] = list(set(items))
    signature = []
    for seed in range(num_hashes):
        hashes = [hash_function(seed, item) for item in unique_items]
        signature.append(min(hashes) if hashes else 0)
    return np.array(signature, dtype=object)


def minhash_similarity(sig_a: np.ndarray, sig_b: np.ndarray) -> float:
    """Approximate Jaccard similarity from two MinHash signatures."""
    if len(sig_a) == 0:
        return 0.0
    matches = np.sum(sig_a == sig_b)
    return float(matches / len(sig_a))


def demo() -> None:
    A = ["user", "wants", "clean", "folder", "structure"]
    B = ["user", "wants", "organized", "folder"]
    C = ["battery", "is", "dead"]
    sig_a = minhash_signature(A, num_hashes=16)
    sig_b = minhash_signature(B, num_hashes=16)
    sig_c = minhash_signature(C, num_hashes=16)
    print("A vs B similarity:", round(minhash_similarity(sig_a, sig_b), 4))
    print("A vs C similarity:", round(minhash_similarity(sig_a, sig_c), 4))


if __name__ == "__main__":
    demo()
