# Memory: Context Compaction

**Code:** `04_Materials/python_references/src/context_compactor.py`  
**Owner agent:** 15 Context Compression Specialist  
**Chat origin:** compaction code example (≈396–411)

## Hybrid method (default)

1. Keep last **N** messages in full (sliding window)
2. Compress older messages into a running summary
3. Return: `[summary as system]` + recent full messages

## Structured summary sections (must preserve)

- Key Decisions
- Constraints & Rules
- Important Facts
- Open Questions
- Next Actions

## Must never drop

- User decisions
- Explicit constraints
- Approved technical choices
- Critical requirements
- Still-open questions

## Can aggressively drop

- Repeated explanations
- Filler
- Abandoned ideas
- Redundant confirmations

## Failure handling

If compression loses meaning → report failure → lighter compression / keep more original → never sacrifice critical info for shortness.
