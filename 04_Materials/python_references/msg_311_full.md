Here’s a concrete **2D tracking example** of the Kalman Filter.

### Scenario
We are tracking an object moving on a 2D plane (x, y).  
We estimate both **position** and **velocity**.

### State Vector (n = 4)
\[
\hat{x} = \begin{bmatrix}
x \\
y \\
v_x \\
v_y
\end{bmatrix}
\]

- \( x, y \) = position  
- \( v_x, v_y \) = velocity

---

### 1. State Transition Matrix \( F \) (assuming constant velocity)

\[
F = \begin{bmatrix}
1 & 0 & \Delta t & 0 \\
0 & 1 & 0 & \Delta t \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\]

---

### 2. Observation Matrix \( H \)
We only measure position (not velocity):

\[
H = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{bmatrix}
\]

---

### 3. Example Numbers

Assume:
- \( \Delta t = 1 \)
- Current state estimate:

\[
\hat{x}_{k|k-1} = \begin{bmatrix}
10 \\
5 \\
2 \\
1
\end{bmatrix}
\]

- Measurement (from sensor):

\[
z_k = \begin{bmatrix}
10.5 \\
5.2
\end{bmatrix}
\]

---

### 4. Simplified Update Insight

The Kalman Gain \( K \) will decide how much to pull the predicted position `(10, 5)` toward the measured position `(10.5, 5.2)`.

- If the sensor is very accurate → \( K \) becomes larger → estimate moves strongly toward the measurement.
- If the sensor is noisy → \( K \) becomes smaller → estimate stays closer to the prediction.

---

Would you like me to also calculate a full numerical example with assumed \( P \) and \( R \) values?