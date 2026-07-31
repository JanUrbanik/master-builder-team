# PROJECT_CHARTER — FULL operational readiness test
**Status:** APPROVED  
**Version:** v1.0  
**Mode:** FULL  
**Project name:** Hardened workflow + routing_manifest verification  
**Date:** 2026-07-31  
**User task (verbatim):** Run a full-scale test task to verify the hardened workflow and routing manifest.

---

## 1. Topic analysis (Strategic Vision Architect)

**Real goal:** Prove ADOPT A FULL path + ENTRY-009/010 hardening work end-to-end with live plugin stages.  
**Success criteria:**
- routing_manifest FULL keys usable as stage spine
- 16 agent frontmatter present
- All four plugins execute once successfully
- Charter + readiness report + KB entry produced  
**Non-goals:** New product features; Gemini draft renames; installing more plugins  
**Constraints:** Grok Build in this project folder; relative paths; no invented tool output  
**Open questions:** none for this test  

---

## 2. Skillset map (System & Reasoning Architect)

| Skillset needed | Why | Best-fit agent seat |
|-----------------|-----|---------------------|
| Workflow enforcement | FULL stage order | 01 Workflow Steward |
| Goal/success framing | Charter §1 | 02 Strategic Vision Architect |
| Seat fitness + stages | Charter structure | 03 System & Reasoning Architect |
| Plugin/env rating | Live stack | 04 Tool & Function Master |
| Research evidence | Tavily stage | 11 Research & Evidence |
| Page extract | Firecrawl stage | 11 (+ firecrawl) |
| Browser truth check | Chrome stage | 06 / 10 + chrome-devtools |
| Planning discipline | Superpowers stage | 03/08/09 patterns via superpowers |
| Final package | Deliverable | 12 Final Synthesizer |
| Knowledge + DEC | Capture | 05 + 16 |

---

## 3. Seat activation of the 16

| # | Agent | Activation | Role this project | Owns (artifacts) |
|---|--------|------------|-------------------|------------------|
| 01 | Workflow Steward | Active | Enforce FULL stages | workflow log |
| 02 | Strategic Vision Architect | Active | Goal framing | charter §1 |
| 03 | System & Reasoning Architect | Active | Fitness + stages | charter §2–4,6 |
| 04 | Tool & Function Master | Active | Env/plugin rating | charter §5 + tool evidence |
| 05 | Knowledge Management Architect | Active | KB ENTRY-011 | KnowledgeBase append |
| 06 | Deep Analysis & Reality Checker | Standby | Available for pre-decision if needed | — |
| 07 | Clarity & Structure Engineer | Standby | — | — |
| 08 | Code & Execution Specialist | Standby | superpowers patterns only via skill path | — |
| 09 | Practical Execution Architect | Standby | — | — |
| 10 | Truth & Resilience Guardian | Active | Browser verify assist / post-check | browser verification note |
| 11 | Research & Evidence Specialist | Active | Tavily + Firecrawl stages | research + extract notes |
| 12 | Final Synthesizer | Active | Final readiness report | `07_Outputs/FULL_HARDENED_WORKFLOW_TEST_REPORT.md` |
| 13 | Human-AI Interface Specialist | Not-needed-this-project | no user UX redesign | — |
| 14 | Cross-Platform Continuity Specialist | Standby | path law already satisfied | — |
| 15 | Context Compression Specialist | Not-needed-this-project | short test | — |
| 16 | Decision Traceability Specialist | Active | DEC for test outcome | DEC-20260731-02 |

---

## 4. Collab graph

### Review edges
| Reviewer | Reviews | Why |
|----------|---------|-----|
| 10 Truth Guardian | browser/page claims | post-build style live check |
| 06 Deep Analysis | optional pre-decision | standby unless contradiction |

### Co-own edges
None.

### Default
Solo only.

---

## 5. Environment / tools (Tool & Function Master)

**Recommended primary environment:** Grok Build CLI in project folder  

| Option | Pros | Cons | Requirements | User approval needed? |
|--------|------|------|--------------|----------------------|
| Grok Build | plugins + MCP live | needs CLI/auth | PATH + Node for chrome | No (already set up) |
| SuperGrok Heavy chat | fast prose | no marketplace MCP stack | none | N/A for this test |

**Installed plugin readiness**

| Plugin | Status this task | MCP/auth OK? | Notes |
|--------|------------------|--------------|-------|
| superpowers | **required** | skills path OK | writing-plans smoke |
| firecrawl | **required** | healthy | scrape docs page |
| tavily | **required** | healthy | search marketplace |
| chrome-devtools | **required** | healthy | open docs page |

---

## 6. Execution stages (order is law)

| Stage | Agent(s) | Input | Output artifact | Done-when |
|-------|----------|-------|-----------------|-----------|
| 0 | Steward | user task | triage=FULL | FULL declared |
| 1 | 02+03+04 | task | this charter | charter filed |
| 2 | User | charter | APPROVED | this file Status=APPROVED (execute order) |
| 3 | 04 | live CLI | preflight plugin/MCP | 3 healthy MCPs |
| 4 | 11 + tavily | query | research bullets | end_turn + URLs |
| 5 | 11 + firecrawl | docs URL | title+bullets | end_turn + title |
| 6 | 10/06 + chrome-devtools | docs URL | title + console | end_turn + no errors |
| 7 | superpowers path | monthly health | plan text | end_turn + 5-step plan |
| 8 | 03 structure audit | frontmatter+manifest | consistency check | 16 FM + manifest keys |
| 9 | 12 | all stage outputs | readiness report | file in 07_Outputs |
| 10 | 05+16 | outcomes | ENTRY-011 + DEC | KB updated |

---

## 7. Anti-overwrite confirmation
- [x] Ownership locks apply  
- [x] No agent overwrites another’s owned artifact  
- [x] Final Synthesizer composes, does not erase sources  

---

## 8. User approval
**User decision:** APPROVED (execute full-scale test order)  
**Date:** 2026-07-31  
**Notes:** Implied by user command to run FULL test.

---

## 9. Amendments
| Version | Date | Trigger | Change | User decision |
|---------|------|---------|--------|---------------|
| | | | | |
