# Plugin Stack Status Note
**Project:** Master Builder Team  
**Mode:** LIGHT (mini-charter)  
**Date:** 2026-07-31  
**Runtime:** Grok Build 0.2.117 · project folder `groki builder team copy`  
**Law:** ADOPT A (ENTRY-008) · capability record ENTRY-009  

---

## Mini-charter

| Field | Value |
|-------|--------|
| **Goal** | One-page verified status of the installed Grok Build plugin stack |
| **Owner seats** | Tool & Function Master (status) · Final Synthesizer (package) |
| **Deliverable** | `07_Outputs/PLUGIN_STACK_STATUS.md` |
| **Done-when** | All four plugins listed with Verified install/MCP status; seat map; how-to-run |

**User OK:** implied by execute order for this LIGHT task.

---

## Workflow Steward log

- **Phase:** Execution (LIGHT) — no full Initiation Council  
- **Triage:** LIGHT (single deliverable, no lasting system redesign)  
- **Called:** Tool fitness check via live CLI (`grok plugin list`, `grok mcp doctor`, `grok inspect`)  
- **Packaged:** this note  

---

## Verified stack (2026-07-31)

### CLI / auth

| Check | Result | Label |
|-------|--------|--------|
| `grok --version` | 0.2.117 | **Verified** |
| xAI session | `~/.grok/auth.json` present (prior login) | **Verified** (file presence; not re-tested this run) |
| Marketplace | `xai-org/plugin-marketplace` | **Verified** (plugins installed from it) |
| Project instructions | `AGENTS.md` loaded by `grok inspect` | **Verified** |

### Plugins

| Plugin | Install | Skills (approx) | MCP | Live doctor | Label |
|--------|---------|-----------------|-----|-------------|--------|
| **superpowers** | installed, enabled | 14 + hooks | none (skills/hooks) | N/A (skills path) | **Verified** installed |
| **firecrawl** | installed, enabled | 10 + command | http · 26 tools | healthy | **Verified** |
| **tavily** | installed, enabled | 8 | http · 5 tools | healthy | **Verified** |
| **chrome-devtools** | installed as `chrome-devtools-mcp`, enabled | 6 | stdio · 29 tools | healthy | **Verified** |

### MCP doctor summary

```text
Found 3 healthy, 0 failing.
  chrome-devtools — handshake OK, 29 tools
  tavily          — handshake OK, 5 tools
  firecrawl       — handshake OK, 26 tools
```

**Label:** **Verified** this run.

### Prior functional smokes (2026-07-30, ENTRY-009)

| Capability | Smoke | Result | Label |
|------------|-------|--------|--------|
| firecrawl | scrape https://example.com | Title: Example Domain | **Verified** (prior) |
| tavily | search “What is example.com used for” | cited bullets | **Verified** (prior) |
| chrome-devtools | open example.com | title OK, no console errors | **Verified** (prior) |
| superpowers | writing-plans style plan | 4-step plan, no file edits | **Verified** (prior) |

This LIGHT run re-verified **install + MCP health**, not a full re-scrape.

---

## Seat mapping (who uses what)

| Plugin | Primary seats | Use |
|--------|---------------|-----|
| superpowers | 03, 08, 09 | plans, TDD, systematic debug, verification-before-completion |
| firecrawl | 11 | scrape/crawl/map/search pages |
| tavily | 11 | structured research + specialized research skills |
| chrome-devtools | 06, 10 | live page/UI/console verification |
| inventory/rating | 04 Tool & Function Master | charter environment table |
| routing only | 01 Workflow Steward | does not assume plugins always-on |

Charter rule: each plugin **required / optional / N/A** per task. Auth/quota failure → escalate to User; never invent tool output.

---

## How to run (operator)

```bash
cd "/Users/generationalwealth/Desktop/groki builder team copy"
export PATH="$HOME/.grok/bin:$PATH"
# optional Node for chrome-devtools npx:
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

grok plugin list
grok mcp doctor
grok
```

Inside TUI: `/plugins`, `/mcp`, `/skills` as needed.

---

## Kit law pointers

| Doc | Role |
|-----|------|
| `03_Knowledge/KnowledgeBase.md` ENTRY-008 | Governance (binding) |
| `03_Knowledge/KnowledgeBase.md` ENTRY-009 | Plugin capability record |
| `AGENTS.md` §5 | Constitution plugin table |
| `.grok/config.toml` `[plugins_stack]` | Machine-readable stack pointer |
| `06_Roadmaps/PROJECT_CHARTER_TEMPLATE.md` | Plugin readiness rows for FULL tasks |

---

## Risks / gaps (honest)

| Item | Label | Note |
|------|--------|------|
| Headless tool calls need `--always-approve` or interactive trust | **Verified** | earlier cancelled without it |
| Chrome path / privacy | **Assumed** | use non-sensitive profile for agent browser control |
| Sibling folder `groki builder team` not synced | **Verified** | this note only covers `groki builder team copy` |
| Gemini archive-renaming plan | **Out of scope** | not required for this LIGHT pass |

---

## Done-when check

- [x] Four plugins named with install status  
- [x] MCP doctor 3 healthy / 0 failing  
- [x] Seat map included  
- [x] Deliverable path: `07_Outputs/PLUGIN_STACK_STATUS.md`  

**LIGHT task: COMPLETE**
