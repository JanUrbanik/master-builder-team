# FIX CHANGELOG — Consistency Pass (2026-07-26)

Applied after external stress test. All 16 seats preserved (UI constraint). ADOPT A is now the only live regime.

## 1. Law consolidation
- **KnowledgeBase ENTRY-001 marked SUPERSEDED** (supersession banner; historical record kept per append-only rule)
- **ENTRY-008 added** — single current operating law (governance, triage, failure protocol, naming law, boundary splits, precedence)
- ENTRY LOG table updated with all 8 entries and statuses
- `AGENTS.md` fully rewritten: one regime, no Coordinator-king remnants, precedence order added (§8)
- `.grok/rules.md` and `.grok/config.toml` rewritten to ADOPT A
- `01_Context/Core_Rules.md` updated; points to ENTRY-008
- Historical analysis files banner-marked as pre-ADOPT A catalogs

## 2. Naming law
- "System & Agent Architect" retired everywhere from active law → **System & Reasoning Architect** only
- Seat 01 = **Workflow Steward** in every active file; `Coordinator:` prefix rule removed
- All agent files 02–16: "the Coordinator" → "Workflow Steward" with context-correct rewording

## 3. Agent prompt migration (ADOPT A propagation)
- Shared **ADOPT A Awareness block** (charter, ownership locks, review-not-overwrite, Standby silence) added to seats 05–16
- Seat 07: rewrites explicitly produced as Review/Revision artifacts — never direct overwrites

## 4. Overlap resolution (boundary splits, seats kept)
- **06 vs 10:** 06 = pre-decision critique of plans; 10 = post-build red-team of artifacts. Binding tables in both files. Max 2 critique rounds each, Review artifacts only.
- **12 vs 13:** 12 owns final deliverable package; 13 = in-process interaction design, review-only on the final package.
- **03 vs 09:** 03 = charter-level structure; 09 = step-level plans inside approved stages; 09 escalates for charter amendment instead of redefining structure.
- 05 vs 16 handoff restated in ENTRY-008.

## 5. Epistemics
- **Reality Score (0–100%) removed** — replaced by three-bucket claim labels (Verified / Assumed / Speculative), consistent with the team's own ENTRY-004 calibration finding
- Kalman/Bayesian memory rescoped as conceptual method + runnable code via seat 08, with explicit "no fake mathematical precision" rule
- "SuperGrok Heavy / full capacity / no artificial limits" flattery boilerplate stripped from all agent prompts
- **Tier fact re-added per user field experience** (Grok guesses the plan / invents limits when untold): one dry line per agent file — "Operating context (given fact): SuperGrok Heavy tier. Never guess or ask the user's plan; never invent plan-based limits; never claim capabilities you cannot verify." Flattery framing and "no limitations" capability claims remain forbidden (AGENTS.md §2, rules.md #8, ENTRY-008 §1)

## 6. Runtime protocols added
- **LIGHT vs FULL task triage** — mini-charter path for simple tasks (Steward file, activation prompts, rules, ENTRY-008)
- **Failure & re-planning protocol** — owner retry → pause → versioned charter amendment (Steward file, AGENTS.md, activation prompt, ENTRY-008)
- **Charter versioning** — version field + amendments table added to PROJECT_CHARTER_TEMPLATE
- **Critique caps** (2 rounds, review-only) written into seats 06/10 and activation prompts

## 7. Portability
- All hardcoded `C:\Users\Dell\...` paths removed from active files (relative paths only; path law in AGENTS.md §6)

## Untouched by design
- `04_Materials/` archive (source-fidelity: original pastes, chat transcript, drafts)
- `.grok/memory/` technical notes and `python_references/src/` modules
