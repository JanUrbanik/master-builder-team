# Master Builder Team

ADOPT A 16-agent kit for **Grok Build**: council-led initiation, charter-as-law execution, ownership locks, and marketplace plugins.

| | |
|--|--|
| **Repo** | https://github.com/JanUrbanik/master-builder-team |
| **Governance** | KnowledgeBase **ENTRY-008** (binding) |
| **Plugins** | ENTRY-009 · superpowers · firecrawl · tavily · chrome-devtools |
| **Hardening** | ENTRY-010 · frontmatter · `routing_manifest.yaml` · raw archive |
| **Verified** | ENTRY-011 + archived E2E report (PASS on `main`) |

---

## Quick start

```bash
cd master-builder-team   # or your local clone path
export PATH="$HOME/.grok/bin:$PATH"
# chrome-devtools MCP needs Node:
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

grok inspect
grok plugin list
grok mcp doctor
grok
```

Headless tool calls may need `--always-approve` (or interactive trust in the TUI).

---

## Workflow (ADOPT A)

Machine-readable topology: [`01_Context/routing_manifest.yaml`](01_Context/routing_manifest.yaml)  
Per-task law after approval: **PROJECT_CHARTER** (template: `06_Roadmaps/PROJECT_CHARTER_TEMPLATE.md`)

### Triage (Workflow Steward first)

| Mode | When | Path |
|------|------|------|
| **LIGHT** | Single deliverable, no lasting system, no research depth | Mini-charter (goal / owner seats / done-when) → User OK → execute owners → optional Final Synthesizer |
| **FULL** | Systems, multi-stage, or research | Initiation Council → PROJECT_CHARTER → **User approval gate** → staged execution |
| Unsure | — | Ask User; **default FULL** |

### FULL path

```text
User task
  → Workflow Steward opens Initiation (no strategy)
  → Council of 3
       • Strategic Vision Architect   — goal, success, non-goals
       • System & Reasoning Architect — seat fitness, ownership, stages
       • Tool & Function Master       — env/plugin rating
  → PROJECT_CHARTER
  → USER APPROVAL (hard gate)
  → Steward enforces charter stages (exact seat names only)
  → After major decisions: Knowledge Management + Decision Traceability
  → Final Synthesizer packages deliverable
```

### Hard rules

- **Ownership locks** — one owner per major artifact; reviews are separate; no silent overwrites
- **Collab** — solo default; review common; co-own rare
- **Off** — voting, forced unanimity, free debate mesh, separate judge
- **Critique caps** — seat 06 pre-decision, seat 10 post-build; max 2 rounds each
- **Ultimate authority** — User
- **Failure** — owner retries once → Steward pauses → charter amendment (versioned)

### Activation paste

For a new FULL project in chat/TUI, use:

`05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md`

---

## Plugins (Grok Build)

| Plugin | Role | Primary seats |
|--------|------|----------------|
| **superpowers** | Plans, TDD, systematic debug, verification | 03, 08, 09 |
| **firecrawl** | Scrape/crawl/map pages (MCP) | 11 |
| **tavily** | Structured research (MCP) | 11 |
| **chrome-devtools** | Live browser / console checks (MCP) | 06, 10 |

Charter must mark each plugin **required / optional / N/A**. Auth or quota failure → escalate to User; never invent tool output.

Verify:

```bash
grok plugin list
grok mcp doctor   # expect 3 healthy (firecrawl, tavily, chrome-devtools)
```

---

## Repository layout

```text
AGENTS.md                 # Constitution
01_Context/
  routing_manifest.yaml   # LIGHT/FULL topology
02_Agents/                # 16 seats + YAML frontmatter (runtime)
03_Knowledge/KnowledgeBase.md
04_Materials/
  raw/                    # heavy dumps — not default context
  agent_drafts_from_chat/ # provenance only — not runtime agents
05_Prompts/
06_Roadmaps/              # charters + roadmaps
07_Outputs/               # active deliverables
  archive/                # frozen verification reports
.grok/                    # config, rules, memory
```

**Runtime vs archive:** use `02_Agents/` + `AGENTS.md` + KB. Do not load numbered chat drafts or `04_Materials/raw/` as the agent system.

---

## Key docs

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Team constitution |
| `01_Context/routing_manifest.yaml` | Programmatic routing |
| `02_Agents/` | Seat prompts |
| `03_Knowledge/KnowledgeBase.md` | Living law / decisions |
| `06_Roadmaps/PROJECT_CHARTER_TEMPLATE.md` | Charter template |
| `05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md` | FULL kickoff paste |

---

## Verification artifacts

| Kind | Path |
|------|------|
| LIGHT status | `07_Outputs/PLUGIN_STACK_STATUS.md` |
| FULL readiness | `07_Outputs/FULL_HARDENED_WORKFLOW_TEST_REPORT.md` |
| FULL charter (test) | `06_Roadmaps/PROJECT_CHARTER_FULL_TEST_2026-07-31.md` |
| E2E deploy report (**archived**) | `07_Outputs/archive/E2E_DEPLOYMENT_VERIFICATION_2026-07-31.md` |

---


---

## Production

See [`01_Context/PRODUCTION.md`](01_Context/PRODUCTION.md) for the production checklist, required machine runtime, plugin install, and what not to ship.

Release tag: **`v1.0.0`** on `main`.

## Operator checklist (healthy stack)

1. On `main`, latest pull
2. `grok inspect` shows project instructions + plugins
3. `grok mcp doctor` → 3 healthy / 0 failing
4. Optional smoke: tavily search, firecrawl scrape `example.com`, chrome-devtools open same URL, superpowers short plan
5. New work: LIGHT mini-charter or FULL activation prompt + charter approval
