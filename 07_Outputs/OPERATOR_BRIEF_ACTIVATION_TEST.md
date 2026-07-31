# Operator Brief — Master Builder Team (production)
**Generated:** FULL activation test via TEAM_ACTIVATION_AND_STRUCTURE_PROMPT  
**Runtime locus:** project root · Grok Build · law ENTRY-008 / plugins ENTRY-009  

---

## 1. Start Grok Build

```bash
cd "/Users/generationalwealth/Desktop/master-builder-team"   # or clone path
export PATH="$HOME/.grok/bin:$PATH"
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

grok inspect          # AGENTS.md + plugins should load
grok plugin list      # four plugins enabled
grok mcp doctor       # expect 3 healthy / 0 failing
grok                  # interactive TUI
```

For a new FULL project, paste from `05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md` (replace `USER_TASK`).

---

## 2. Triage: LIGHT vs FULL

| Mode | Use when | Path |
|------|----------|------|
| **LIGHT** | One deliverable; no lasting system; no deep research | Mini-charter (goal / owners / done-when) → User OK → execute |
| **FULL** | Systems, multi-stage, or research | Council of 3 → PROJECT_CHARTER → **User approval** → staged execution |
| Unsure | — | Ask User; default **FULL** |

FULL spine (routing_manifest):  
`Steward opens Initiation → Vision → Structure → Tools → Charter → User gate → Execution → KB capture → Final Synthesizer`

---

## 3. When to use each plugin

| Plugin | Use for | Primary seats |
|--------|---------|----------------|
| **superpowers** | Plans, TDD, debug discipline, verification checklists | 03, 08, 09 |
| **tavily** | Structured web research with citations | 11 |
| **firecrawl** | Full-page scrape/crawl/map when depth matters | 11 |
| **chrome-devtools** | Live page title/console/UI truth checks | 06, 10 |

Charter each as **required / optional / N/A**. Auth/quota fail → escalate to User; never invent tool results.

**Verified live (this test):**
- Tavily: marketplace + docs sources for Grok Build plugins (**Verified**)
- Chrome DevTools: docs page title `Skills, Plugins & Marketplaces | SpaceXAI Docs`; console errors **No** (**Verified**)
- Docs URL: https://docs.x.ai/build/features/skills-plugins-marketplaces  
- Marketplace launch ref: https://x.ai/news/grok-plugin-marketplace  

---

## 4. Five-bullet health checklist

- [ ] **Inventory:** `grok plugin list` → superpowers, firecrawl, tavily, chrome-devtools installed/enabled  
- [ ] **MCP:** `grok mcp doctor` → 3 healthy / 0 failing (~26 / 5 / 29 tools)  
- [ ] **firecrawl smoke:** scrape `https://example.com` → title Example Domain  
- [ ] **tavily smoke:** search returns ≥2 real `http` sources  
- [ ] **chrome-devtools smoke:** open same docs or example URL → title OK, console errors No  

Optional: short superpowers writing-plans checklist for monthly cadence.

---

## 5. Hard rules (do not skip)

- Ownership locks; reviews never overwrite  
- No voting / free debate mesh  
- Critique caps: seat 06 pre-decision, seat 10 post-build (max 2)  
- Ultimate authority = User  

---

## Deliverable paths (this activation test)

| Artifact | Path |
|----------|------|
| Charter | `06_Roadmaps/PROJECT_CHARTER_ACTIVATION_TEST_*.md` |
| Workflow log | `07_Outputs/ACTIVATION_WORKFLOW_LOG_*.md` |
| This brief | `07_Outputs/OPERATOR_BRIEF_ACTIVATION_TEST.md` |

**Activation workflow test: PASS**
