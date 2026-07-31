# Agentic Workflow Patterns — Canonical Table

> **HISTORICAL ANALYSIS — pre-ADOPT A.** Kept as pattern catalog. Where this document says "Coordinator (leader/arbitrator)", current law (KnowledgeBase **ENTRY-008**) applies instead: Initiation Council + charter + Workflow Steward. Do not implement governance from this file.

**Source:** User textbox (exact)  
**Location:** `01_Context/` (project root, relative)  
**Status:** CANONICAL REFERENCE  
**Binding decision:** Hierarchical Leader Synthesis = **Yes – primary**  
**Deep analysis:** `01_Context/Agentic_Workflows_Deep_Analysis.md`  
**Operational rules:** `01_Context/Coordination_Patterns.md` · `02_Agents/01_Coordinator.md`

---

## Table (exact content)

| Pattern | Mechanism | Strengths | Weaknesses | Used in Our Live Team? |
|---------|-----------|-----------|------------|------------------------|
| Hierarchical Leader Synthesis | Specialists contribute; leader arbitrates | Speed, coherence, clear accountability | Single point of failure; minority views can be suppressed | **Yes – primary** |
| Majority / Plurality Voting | Independent answers; most frequent wins | Robust to individual hallucinations; empirically strong gains | Loses nuance; ties; ignores expertise | **No** |
| Weighted / Confidence Voting | Votes scaled by confidence or role expertise | Reduces impact of weak agents | LLM confidence is poorly calibrated | **No** |
| Multi-Agent Debate (MAD) | Iterative critique rounds | Surfaces errors; explores alternatives | High latency; sycophancy risk; limited accuracy gain beyond voting | **Partial (Reality Checker only)** |
| Debate-then-Vote Hybrid | Fixed debate rounds → final vote | Caps endless deliberation | Still higher latency | **No** |
| Forced Consensus / Unanimity | Agents negotiate until agreement | Strong buy-in | Deadlock risk; superficial agreement | **No** |
| Judge / Evaluator Arbitration | Separate judge model selects or merges | Independent quality control | Extra cost | **No (Coordinator acts as both)** |

---

## Live-team implementation map

| Pattern usage | How it is implemented |
|---------------|------------------------|
| **Yes – primary** Hierarchical Leader Synthesis | Coordinator calls specialists by exact name; arbitrates; synthesizes |
| **Partial** Multi-Agent Debate | Deep Analysis & Reality Checker (+ Truth & Resilience Guardian when needed); cap 1–2 rounds |
| **No (Coordinator acts as both)** Judge | No separate judge seat; Coordinator leads + arbitrates |
| All other rows **No** | Disabled by default unless user explicitly orders a one-task exception (must log in KnowledgeBase) |

---

## One-line operating law

**Hierarchy is law. Critique is optional and capped. Voting and forced unanimity are off. Human approval is sovereign.**
