"""
Reference memory: Kalman filter (matrix form + 2D tracking numerical example).
Source chat: Research evidence / Bayesian + Kalman deep-dive.
Agent owner: 11 Research & Evidence Specialist
"""

from __future__ import annotations

import numpy as np


def kalman_predict(
    x: np.ndarray,
    P: np.ndarray,
    F: np.ndarray,
    Q: np.ndarray,
    B: np.ndarray | None = None,
    u: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Predict:
      x_{k|k-1} = F x + B u
      P_{k|k-1} = F P F^T + Q
    """
    if B is not None and u is not None:
        x_pred = F @ x + B @ u
    else:
        x_pred = F @ x
    P_pred = F @ P @ F.T + Q
    return x_pred, P_pred


def kalman_update(
    x_pred: np.ndarray,
    P_pred: np.ndarray,
    z: np.ndarray,
    H: np.ndarray,
    R: np.ndarray,
    joseph: bool = False,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Update:
      K = P H^T (H P H^T + R)^{-1}
      x = x + K (z - H x)
      P = (I - K H) P   [or Joseph form]
    Returns (x_updated, P_updated, K)
    """
    S = H @ P_pred @ H.T + R
    K = P_pred @ H.T @ np.linalg.inv(S)
    y = z - H @ x_pred
    x_upd = x_pred + K @ y
    I = np.eye(P_pred.shape[0])
    if joseph:
        IKH = I - K @ H
        P_upd = IKH @ P_pred @ IKH.T + K @ R @ K.T
    else:
        P_upd = (I - K @ H) @ P_pred
    return x_upd, P_upd, K


def demo_2d_tracking_from_chat() -> None:
    """
    Numerical example from the shared chat:
    state = [x, y, vx, vy]
    predicted x = [10, 5, 2, 1]
    P diag-ish = diag(2,2,1,1)
    H measures position only
    R = I
    z = [10.5, 5.2]
    Expected updated position ≈ [10.333, 5.133], velocity unchanged.
    """
    x_pred = np.array([10.0, 5.0, 2.0, 1.0])
    P_pred = np.diag([2.0, 2.0, 1.0, 1.0])
    H = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]])
    R = np.eye(2)
    z = np.array([10.5, 5.2])

    x_upd, P_upd, K = kalman_update(x_pred, P_pred, z, H, R)
    print("K =\n", K)
    print("x_upd =", x_upd)
    print("expected ≈ [10.333, 5.133, 2.0, 1.0]")


if __name__ == "__main__":
    demo_2d_tracking_from_chat()
