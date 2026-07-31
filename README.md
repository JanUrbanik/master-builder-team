# Master Builder Team

ADOPT A **16-agent** kit for **Grok Build**: council-led initiation, charter-as-law execution, ownership locks, and marketplace plugins.

| | |
|--|--|
| **Repo** | https://github.com/JanUrbanik/master-builder-team |
| **Local path** | `Desktop/master-builder-team` |
| **Release** | **v1.0.0** (+ later `main` commits for verification artifacts) |
| **Governance** | KnowledgeBase **ENTRY-008** (binding) |
| **Plugins** | ENTRY-009 · superpowers · firecrawl · tavily · chrome-devtools |
| **Hardening** | ENTRY-010 · agent YAML frontmatter · `routing_manifest.yaml` |
| **Verified** | ENTRY-011 FULL PASS · E2E archived · **activation-prompt test PASS** |

---

## Quick start

```bash
cd "/Users/generationalwealth/Desktop/master-builder-team"   # or your clone
export PATH="$HOME/.grok/bin:$PATH"
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

grok inspect          # loads AGENTS.md + plugins
grok plugin list      # four plugins enabled
grok mcp doctor       # expect 3 healthy / 0 failing
grok                  # interactive TUI
```

Headless tool calls may need `--always-approve` (or interactive trust in the TUI).

**New FULL project:** paste `05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md` into Grok (replace `USER_TASK`).

---

## Workflow (ADOPT A)

| Source | Role |
|--------|------|
| [`01_Context/routing_manifest.yaml`](01_Context/routing_manifest.yaml) | Default LIGHT/FULL topology (machine-readable) |
| **PROJECT_CHARTER** (after User approval) | Per-task law — stage order, owners, plugin ratings |
| [`AGENTS.md`](AGENTS.md) | Constitution |
| KnowledgeBase **ENTRY-008** | Binding operating law |

### Triage (Workflow Steward — seat 01)

| Mode | When | Path |
|------|------|------|
| **LIGHT** | Single deliverable; no lasting system; no research depth | 3-line mini-charter (goal / owner seats / done-when) → User OK → execute owners → optional Final Synthesizer |
| **FULL** | Systems, multi-stage, or research | Initiation Council → PROJECT_CHARTER → **User approval gate** → staged execution |
| Unsure | — | Ask User; **default FULL** |

### FULL path

```text
User task
  → Workflow Steward opens Initiation (no strategy of its own)
  → Council of 3 (free collab during Initiation only)
       1. Strategic Vision Architect   — real goal, success criteria, non-goals, constraints
       2. System & Reasoning Architect — seat fitness (Active/Standby/Not-needed), ownership, collab edges, stage order
       3. Tool & Function Master       — environment + plugin readiness (required/optional/N/A)
  → PROJECT_CHARTER (template: 06_Roadmaps/PROJECT_CHARTER_TEMPLATE.md)
  → USER APPROVAL (hard gate — no specialist execution before APPROVED)
  → Steward enforces stages: call agents by exact full name only
  → After major decisions: Knowledge Management Architect + Decision Traceability Specialist
  → Final Synthesizer composes deliverable (does not erase source artifacts)
```

### Hard rules

- **Ownership locks** — one owner per major artifact; reviews are separate files; no silent overwrites  
- **Collab** — solo default; review common; co-own rare (dual justification)  
- **Off** — voting, forced unanimity, free debate mesh, separate judge model  
- **Critique caps** — seat 06 pre-decision, seat 10 post-build; max **2** rounds each; Review artifacts only  
- **Speaking** — seats speak only when Steward calls exact name (Council free only in Initiation)  
- **Claims** — label **Verified / Assumed / Speculative**; no invented numeric confidence  
- **Ultimate authority** — User  
- **Failure** — owner retries once → Steward pauses → versioned charter amendment  

---

## Agent roster and capabilities

Runtime prompts: `02_Agents/*.md` (YAML frontmatter + body). Call by **exact seat name**.

| # | Seat | Tier | Capability (what they own) | Plugins (when useful) |
|---|------|------|----------------------------|------------------------|
| 01 | **Workflow Steward** | Enforcement | LIGHT/FULL triage; stage order; ownership locks; no strategy | — |
| 02 | **Strategic Vision Architect** | Initiation Council | Real goal, success criteria, non-goals, constraints | — |
| 03 | **System & Reasoning Architect** | Initiation Council | Seat fitness, ownership map, collab graph, stage order, reasoning scaffolds | superpowers |
| 04 | **Tool & Function Master** | Initiation Council | Env/tool rating; plugin inventory; pros/cons/requirements | all four (inventory) |
| 05 | **Knowledge Management Architect** | Execution | `KnowledgeBase.md` entries (structure + append) | — |
| 06 | **Deep Analysis & Reality Checker** | Execution | Pre-decision critique, pre-mortems, claim labels (max 2 rounds) | chrome-devtools |
| 07 | **Clarity & Structure Engineer** | Execution | Ambiguity removal; revision artifacts only (never overwrite owners) | — |
| 08 | **Code & Execution Specialist** | Execution | Code, scripts, tests, folders; resource-management patterns | superpowers |
| 09 | **Practical Execution Architect** | Execution | Step-level plans inside approved charter stages | superpowers |
| 10 | **Truth & Resilience Guardian** | Execution | Post-build red-team, hallucination/goal-drift checks (max 2 rounds) | chrome-devtools |
| 11 | **Research & Evidence Specialist** | Execution | Evidence packs, sources, conflict weighing | tavily, firecrawl |
| 12 | **Final Synthesizer** | Execution | Final deliverable package from owned artifacts | — |
| 13 | **Human-AI Interface Specialist** | Execution | In-process user interaction design; review-only on final package | — |
| 14 | **Cross-Platform Continuity Specialist** | Execution | Portability (web/Build/WSL/PowerShell/local); relative paths | — |
| 15 | **Context Compression Specialist** | Execution | Context compaction (project memory: MinHash/vector/Jaccard) | — |
| 16 | **Decision Traceability Specialist** | Execution | DEC records (options, rationale); hands off to seat 05 | — |

### Boundary pairs (do not blur)

| Pair | Split |
|------|--------|
| 06 vs 10 | Pre-decision critique vs post-build red-team |
| 03 vs 09 | Charter-level structure vs step-level plans |
| 12 vs 13 | Final package ownership vs in-process UX |
| 05 vs 16 | KB structure/entries vs decision records |
| 07 vs owners | Clarity produces Review/Revision only |

---

## Plugin capabilities (Grok Build)

| Plugin | Kind | What it adds | Primary seats |
|--------|------|--------------|----------------|
| **superpowers** | skills + hooks | writing-plans, TDD, systematic-debugging, verification-before-completion, parallel agents | 03, 08, 09 |
| **tavily** | MCP (~5 tools) | Structured research search + specialized research skills | 11 |
| **firecrawl** | MCP (~26 tools) | Scrape/crawl/map/search pages; JS-rendered content | 11 |
| **chrome-devtools** | MCP (~29 tools) | Live browser control; title/console/network/UI checks | 06, 10 |

### Operator rules for plugins

1. Rate each plugin **required / optional / N/A** in the charter (Tool & Function Master).  
2. Prefer installed plugins over reinventing the same capability in Grok Build.  
3. Auth/quota/handshake failure → escalate to User; **never invent tool output**.  
4. Heavy chat remains valid for LIGHT tasks that need no plugins.

### Health commands

```bash
grok plugin list
grok mcp doctor   # expect: firecrawl, tavily, chrome-devtools — 3 healthy / 0 failing
```

### Smoke checks (optional)

| Plugin | Smoke |
|--------|--------|
| firecrawl | Scrape `https://example.com` → title Example Domain |
| tavily | Search returns ≥2 real `http` sources |
| chrome-devtools | Open URL → title OK, console errors No |
| superpowers | Short writing-plans checklist, no file edits |

---

## Repository layout

```text
README.md                 # This file — workflow + capabilities
AGENTS.md                 # Constitution
01_Context/
  routing_manifest.yaml   # LIGHT/FULL topology
  PRODUCTION.md           # Production checklist
02_Agents/                # 16 seats + YAML frontmatter (RUNTIME)
03_Knowledge/KnowledgeBase.md
04_Materials/
  raw/                    # heavy dumps — not default context (gitignored bulk)
  agent_drafts_from_chat/ # provenance only — NOT runtime agents
05_Prompts/               # TEAM_ACTIVATION paste, etc.
06_Roadmaps/              # charters + roadmaps
07_Outputs/               # active deliverables
  archive/                # frozen verification reports
.grok/                    # config.toml, rules.md, memory/, skills/
```

**Runtime vs archive:** load `AGENTS.md` + `02_Agents/` + KB. Do not treat numbered chat drafts or raw dumps as the agent system.

---

## Key docs

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Team constitution |
| `01_Context/routing_manifest.yaml` | Programmatic LIGHT/FULL routing |
| `01_Context/PRODUCTION.md` | Production readiness + machine requirements |
| `02_Agents/` | Seat system prompts |
| `03_Knowledge/KnowledgeBase.md` | Living law / decisions (ENTRY-008 current) |
| `05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md` | FULL kickoff paste |
| `06_Roadmaps/PROJECT_CHARTER_TEMPLATE.md` | Charter template |
| `07_Outputs/OPERATOR_BRIEF_ACTIVATION_TEST.md` | Operator brief from activation test |

---

## Verification artifacts

| Kind | Path | Result |
|------|------|--------|
| LIGHT status | `07_Outputs/PLUGIN_STACK_STATUS.md` | PASS |
| FULL readiness | `07_Outputs/FULL_HARDENED_WORKFLOW_TEST_REPORT.md` | PASS |
| FULL charter (earlier) | `06_Roadmaps/PROJECT_CHARTER_FULL_TEST_2026-07-31.md` | APPROVED |
| Activation test charter | `06_Roadmaps/PROJECT_CHARTER_ACTIVATION_TEST_2026-07-31.md` | APPROVED |
| Activation steward log | `07_Outputs/ACTIVATION_WORKFLOW_LOG_2026-07-31.md` | PASS |
| Operator Brief | `07_Outputs/OPERATOR_BRIEF_ACTIVATION_TEST.md` | PASS |
| E2E deploy (**archived**) | `07_Outputs/archive/E2E_DEPLOYMENT_VERIFICATION_2026-07-31.md` | PASS |
| Closeout | `07_Outputs/PROJECT_CLOSEOUT_2026-07-31.md` | CLOSED — OPERATIONAL |

---

## Production

See [`01_Context/PRODUCTION.md`](01_Context/PRODUCTION.md) for machine requirements, plugin install, health gates, and what not to ship.

Release tag: **`v1.0.0`** on `main` (additional verification commits may follow on `main`).

### Operator checklist (healthy stack)

1. `git pull origin main`  
2. `grok inspect` shows project instructions + plugins  
3. `grok mcp doctor` → **3 healthy / 0 failing**  
4. Optional smokes (table above)  
5. New work: LIGHT mini-charter **or** FULL activation prompt + charter approval  
