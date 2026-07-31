# Memory: Bayesian Updating + Kalman Filter

**Code:** `04_Materials/python_references/src/kalman_filter.py`  
**Owner agent:** 11 Research & Evidence Specialist  
**Chat origin:** Bayesian updating + Kalman deep-dive (≈299–317)

## Bayesian-style evidence update (practical)

1. Assign prior confidence (High / Moderate / Low / Very Low) by source quality
2. Evaluate new evidence likelihood (supports / weakens / neutral)
3. Update posterior confidence proportionally to evidence strength
4. Report confidence + why it changed (never fake binary certainty)

## Kalman matrix form

**Predict**

- `x = F x + B u`
- `P = F P Fᵀ + Q`

**Update**

- `K = P Hᵀ (H P Hᵀ + R)⁻¹`
- `x = x + K (z − H x)`
- `P = (I − K H) P` (Joseph form optional for stability)

## 2D tracking example (from chat)

State: `[x, y, vx, vy]`  
Predicted: `[10, 5, 2, 1]`  
`P = diag(2,2,1,1)`, `R = I`, measure position only  
`z = [10.5, 5.2]`  
Updated position ≈ `[10.333, 5.133]`, velocity unchanged.

## Meaning for research agents

Treat Kalman as a **metaphor + tool** for fusing noisy measurements with prior belief: high sensor trust → move more toward measurement; high noise → stay closer to prediction.
