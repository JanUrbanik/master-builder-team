Here’s a **full numerical update** example for the 2D tracker.

### Given Values

**Predicted state:**
\[
\hat{x}_{k|k-1} = \begin{bmatrix}
10.0 \\
5.0 \\
2.0 \\
1.0
\end{bmatrix}
\]

**Predicted covariance \( P_{k|k-1} \):**
\[
P_{k|k-1} = \begin{bmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\]

**Observation matrix \( H \):**
\[
H = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{bmatrix}
\]

**Measurement noise \( R \):**
\[
R = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\]

**Measurement \( z_k \):**
\[
z_k = \begin{bmatrix}
10.5 \\
5.2
\end{bmatrix}
\]

---

### Step 1: Innovation Covariance

\[
S = H P H^\top + R = \begin{bmatrix}
2 & 0 \\
0 & 2
\end{bmatrix} + \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
3 & 0 \\
0 & 3
\end{bmatrix}
\]

---

### Step 2: Kalman Gain

\[
K = P H^\top S^{-1} = \begin{bmatrix}
2 & 0 \\
0 & 2 \\
0 & 0 \\
0 & 0
\end{bmatrix}
\begin{bmatrix}
1/3 & 0 \\
0 & 1/3
\end{bmatrix}
= \begin{bmatrix}
2/3 & 0 \\
0 & 2/3 \\
0 & 0 \\
0 & 0
\end{bmatrix}
\]

---

### Step 3: Innovation (Measurement Residual)

\[
y = z_k - H \hat{x}_{k|k-1} = \begin{bmatrix}
10.5 \\
5.2
\end{bmatrix}
-
\begin{bmatrix}
10.0 \\
5.0
\end{bmatrix}
= \begin{bmatrix}
0.5 \\
0.2
\end{bmatrix}
\]

---

### Step 4: State Update

\[
\hat{x}_{k|k} = \hat{x}_{k|k-1} + K y
= \begin{bmatrix}
10.0 \\
5.0 \\
2.0 \\
1.0
\end{bmatrix}
+
\begin{bmatrix}
2/3 & 0 \\
0 & 2/3 \\
0 & 0 \\
0 & 0
\end{bmatrix}
\begin{bmatrix}
0.5 \\
0.2
\end{bmatrix}
= \begin{bmatrix}
10.333 \\
5.133 \\
2.0 \\
1.0
\end{bmatrix}
\]

---

### Result

- Position was updated toward the measurement.
- Velocity remained unchanged (because we don’t directly measure velocity in this example).

---

Would you like me to also calculate the updated covariance \( P_{k|k} \)?