Here’s the full **matrix form** of the Kalman Filter, derived step by step.

### 1. Prediction Step (Time Update)

We predict the next state and its uncertainty:

**State prediction:**
\[
\hat{x}_{k|k-1} = F_k \hat{x}_{k-1|k-1} + B_k u_k
\]

**Covariance prediction:**
\[
P_{k|k-1} = F_k P_{k-1|k-1} F_k^\top + Q_k
\]

Where:
- \( F_k \) = State transition matrix
- \( B_k \) = Control matrix
- \( u_k \) = Control input
- \( Q_k \) = Process noise covariance

---

### 2. Kalman Gain (Full Matrix Form)

\[
K_k = P_{k|k-1} H_k^\top \left( H_k P_{k|k-1} H_k^\top + R_k \right)^{-1}
\]

Where:
- \( H_k \) = Observation matrix
- \( R_k \) = Measurement noise covariance

---

### 3. Update Step (Measurement Update)

**State update:**
\[
\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k \left( z_k - H_k \hat{x}_{k|k-1} \right)
\]

**Covariance update:**
\[
P_{k|k} = \left( I - K_k H_k \right) P_{k|k-1}
\]

(Alternative Joseph form for better numerical stability):

\[
P_{k|k} = \left( I - K_k H_k \right) P_{k|k-1} \left( I - K_k H_k \right)^\top + K_k R_k K_k^\top
\]

---

### Summary of the Full Matrix Kalman Filter

**Predict:**
\[
\begin{align*}
\hat{x}_{k|k-1} &= F_k \hat{x}_{k-1|k-1} + B_k u_k \\
P_{k|k-1} &= F_k P_{k-1|k-1} F_k^\top + Q_k
\end{align*}
\]

**Update:**
\[
\begin{align*}
K_k &= P_{k|k-1} H_k^\top (H_k P_{k|k-1} H_k^\top + R_k)^{-1} \\
\hat{x}_{k|k} &= \hat{x}_{k|k-1} + K_k (z_k - H_k \hat{x}_{k|k-1}) \\
P_{k|k} &= (I - K_k H_k) P_{k|k-1}
\end{align*}
\]

---

Would you like me to also explain what each matrix represents in simple terms?