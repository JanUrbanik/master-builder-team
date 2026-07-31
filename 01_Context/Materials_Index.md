# Materials Index

Index of research data and source materials in `04_Materials/`.

| Path | Description |
|------|-------------|
| `04_Materials/raw/shared_chat_full.json` | Full shared conversation API dump (~7.8 MB) — archived raw |
| `04_Materials/raw/share_raw.html` | Raw HTML of the share page — archived |
| `04_Materials/raw/js_chunks/` | Temporary Grok web JS — archived disposable |
| `04_Materials/raw/README.md` | Raw archive policy |
| `04_Materials/shared_chat_transcript.md` | Readable full transcript of the shared chat |
| `04_Materials/original_16_agents_user_paste.md` | User's original 16-agent pack (pre-redesign) |
| `04_Materials/final_pieces/` | Extracted high-value assistant messages used to assemble this project |
| `04_Materials/agent_drafts_from_chat/` | Intermediate draft exports — **not runtime agents** |
| `01_Context/routing_manifest.yaml` | Machine-readable ADOPT A LIGHT/FULL routing |

## Source link

https://grok.com/share/c2hhcmQtMg_4b87a6bd-bab6-4251-9a79-98fe32435b74

## Notes

- Prefer structured files under `AGENTS.md`, `02_Agents/`, and `03_Knowledge/` for day-to-day work.
- Use the transcript/JSON only when you need original wording or to recover missing detail.

## Python reference memory

| Path | Description |
|------|-------------|
| `.grok/memory/INDEX.md` | Master memory catalog |
| `.grok/memory/*.md` | Concept memories (rules, when-to-use, owners) |
| `04_Materials/python_references/src/` | Canonical runnable Python modules |
| `04_Materials/python_references/msg_*_full.md` | Original chat messages containing code |
| `04_Materials/python_references/*_b*.py.txt` | Raw fenced blocks extracted from chat |

## User Text Box Kit

| Path | Description |
|------|-------------|
| `04_Materials/User_Textbox_Kit/README.md` | Master index of all structured user pastes |
| `04_Materials/User_Textbox_Kit/01_Original_16_Agents_User_Paste/` | User's original 16 agent prompts (split + raw) |
| `04_Materials/User_Textbox_Kit/02_Folder_Structure_User_Paste/` | User's folder structure paste |
| `04_Materials/User_Textbox_Kit/03_User_Requirements_Statements/` | User requirement statements as structured files |

## Coordination

| Path | Description |
|------|-------------|
| `01_Context/Coordination_Patterns.md` | Multi-agent pattern table + hierarchy decision (binding) |
| `01_Context/Agentic_Workflows_Deep_Analysis.md` | Deep analysis of agentic workflow governance textbox |
| `01_Context/routing_manifest.yaml` | Programmatic ADOPT A DAG / mode routing (not Gemini 3-node graph) |

## ADOPT A activation

| Path | Description |
|------|-------------|
| `05_Prompts/TEAM_ACTIVATION_AND_STRUCTURE_PROMPT.md` | Full team activation + structure prompt |
| `05_Prompts/TEAM_ACTIVATION_SHORT.md` | Short paste card |
| `06_Roadmaps/PROJECT_CHARTER_TEMPLATE.md` | Charter template Council must fill |
| `01_Context/Collab_and_Ownership_Rules.md` | No-overwrite + collab edges |

## Installed Grok Build plugin stack

| Path / entry | Description |
|--------------|-------------|
| `03_Knowledge/KnowledgeBase.md` **ENTRY-009** | Official record of installed plugins, smoke tests, seat mapping |
| `AGENTS.md` §5 | Constitution-level plugin table |
| `.grok/config.toml` `[plugins_stack]` | Machine-readable stack pointer |
| Live verify | `grok plugin list` · `grok mcp doctor` · `grok inspect` |
