# Project Structure (from user text box)

**Source:** Shared chat H194  
**Refined official tree lives in project root; this preserves the user's original paste intent.**

```
project/
├── AGENTS.md              # Core architecture, rules, agent roles
├── .grok/                 # plugins, local config, rules
│   ├── config.toml
│   ├── rules.md
│   ├── skills/
│   └── memory/
├── context/               # foundational project understanding
├── agents/                # individual agent system prompts
├── knowledge/             # living knowledge base
│   └── KnowledgeBase.md
├── materials/             # research data, large references
├── prompts/               # reusable prompt templates
├── roadmaps/              # approved plans
└── outputs/               # final deliverables
```

## Mapping to current official folders

| User paste idea | Current folder |
|-----------------|----------------|
| AGENTS.md | `AGENTS.md` |
| .grok/ | `.grok/` |
| context/ | `01_Context/` |
| agents/ | `02_Agents/` |
| knowledge/ | `03_Knowledge/` |
| materials/ | `04_Materials/` |
| prompts/ | `05_Prompts/` |
| roadmaps/ | `06_Roadmaps/` |
| outputs/ | `07_Outputs/` |
