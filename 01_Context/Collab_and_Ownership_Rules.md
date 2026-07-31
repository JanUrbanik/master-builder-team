# Collaboration & Ownership Rules — ADOPT A

**Status:** BINDING  
**Project root:** (relative paths only — portable across machines)

---

## 1. Ownership locks (hard)

1. Every major artifact has **exactly one Owner agent** (named in PROJECT_CHARTER).  
2. **No agent may overwrite, replace, or silently edit** another agent’s owned artifact.  
3. Allowed non-owner actions:
   - Produce a **Review** artifact linked to the owner’s work  
   - Request revision (owner revises their own artifact)  
   - Escalate to User  
4. Final Synthesizer may **compose** from owned artifacts into a new final package; it may not erase owners’ source artifacts.

## 2. Collaboration modes

### A. Solo (default)

Agent works alone on owned artifact. No peer required.

### B. Review (common)

- Reviewer listed on a **review edge** in charter  
- Reviewer writes review only  
- Owner keeps write-lock  
- Owner accepts/rejects with reasons (Decision Traceability)

### C. Co-production (rare)

- Both agents listed on a **co-own edge**  
- **Both** must state why co-production raises quality for the **shared deliverable**  
- Output dual-signed  
- If either cannot justify → fall back to Review or Solo  

## 3. Illegal

- Free-for-all debate mesh  
- Majority / confidence voting  
- Forced unanimity  
- Overwriting another agent’s progress “to help”  
- Inventing collab pairs not in charter  

## 4. Enforcement

**Workflow Steward** blocks illegal overwrites and illegal collab.  
Violations → stop stage → report to User.
