# Production readiness

**Status:** Production-ready (2026-07-31)  
**Release:** `v1.0.0` on `main`  
**Closeout:** `07_Outputs/PROJECT_CLOSEOUT_2026-07-31.md`

## What “production” means here
This is a **Grok Build project kit**, not a hosted web service. Production use means:
1. Clean `main` clone or pull
2. Grok CLI authenticated
3. Marketplace plugins installed + MCP healthy
4. Work runs under ADOPT A (ENTRY-008) with LIGHT/FULL routing

## Required runtime (operator machine)
| Component | Purpose |
|-----------|---------|
| Grok Build CLI | Agent runtime |
| Node LTS (nvm ok) | chrome-devtools MCP via `npx` |
| Google Chrome | Browser verification |
| GitHub access | Optional; for pull/push only |

## Install plugins (once per machine)
```bash
export PATH="$HOME/.grok/bin:$PATH"
grok plugin marketplace add xai-org/plugin-marketplace
grok plugin install superpowers --trust
grok plugin install firecrawl --trust
grok plugin install tavily --trust
grok plugin install chrome-devtools --trust
# then authorize firecrawl + tavily in TUI: /mcp
```

## Health gate before real work
```bash
git pull origin main
grok inspect
grok plugin list
grok mcp doctor   # expect 3 healthy / 0 failing
```

## Do not ship / do not load by default
- `04_Materials/raw/*` heavy dumps
- `04_Materials/agent_drafts_from_chat/` numbered drafts
- `local_dev_archive/` (gitignored machine notes)
- Secrets: `.env`, `auth.json`, API keys

## Canonical entrypoints
| Path | Role |
|------|------|
| `README.md` | Operator workflow |
| `AGENTS.md` | Constitution |
| `01_Context/routing_manifest.yaml` | LIGHT/FULL topology |
| `02_Agents/` | Runtime seats |
| `03_Knowledge/KnowledgeBase.md` | Law (ENTRY-008) |
| `05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md` | FULL kickoff |

## Support artifacts
- LIGHT: `07_Outputs/PLUGIN_STACK_STATUS.md`
- FULL: `07_Outputs/FULL_HARDENED_WORKFLOW_TEST_REPORT.md`
- E2E: `07_Outputs/archive/E2E_DEPLOYMENT_VERIFICATION_2026-07-31.md`
- Closeout: `07_Outputs/PROJECT_CLOSEOUT_2026-07-31.md`
