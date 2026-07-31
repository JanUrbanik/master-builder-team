# Prompt Template — Use Technical Memory

Coordinator / specialist call pattern when a task needs code references.

---

{{AGENT_NAME}}: Use project technical memory for this task.

**Task:**
{{TASK}}

**Required memory:**
- Index: `.grok/memory/INDEX.md`
- Concept: `.grok/memory/{{MEMORY_FILE}}.md`
- Code: `04_Materials/python_references/src/{{MODULE}}.py`

**Rules:**
1. Follow the memory rules exactly (do not invent conflicting patterns)
2. Prefer the canonical module over new one-off code unless the module is insufficient
3. If you extend a pattern, document the change for Knowledge Management Architect
4. State which memory files you used
