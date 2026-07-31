# Raw archive (not active runtime context)

Heavy source dumps live here so they are **not** mistaken for runtime agent prompts or default context pack.

| Path | Description |
|------|-------------|
| `shared_chat_full.json` | Full shared conversation API dump |
| `share_raw.html` | Raw HTML of the share page |
| `js_chunks/` | Disposable Grok web JS used only to discover share API |

**Do not** load these into agent prompts by default.

Prefer:
- `AGENTS.md`, `02_Agents/`, `03_Knowledge/KnowledgeBase.md`
- Readable transcript: `../shared_chat_transcript.md` (if present at materials root)
- Runtime routing: `../../01_Context/routing_manifest.yaml`
