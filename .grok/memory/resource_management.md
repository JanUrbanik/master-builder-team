# Memory: Resource Management (Python)

**Owner agent:** Code & Execution Specialist  
**Code:** `04_Materials/python_references/src/resource_management.py`  
**Chat origins:** messages on async context managers, custom context managers, advanced patterns (≈255–263)

## Hard rules (locked into Agent 08)

1. Prefer Context Managers (`with`) for resources.
2. Prefer Async Context Managers (`async with`) for async code.
3. Always use structured exception handling.
4. Catch specific exceptions when possible; no silent failures.
5. Know class-based, decorator (`@contextmanager` / `@asynccontextmanager`), multi-`with`, and `suppress`.

## Pattern ranking

| Pattern | Safety | Cleanliness | Use? |
|---------|--------|-------------|------|
| Manual open/close | Low | Low | No |
| try/finally | High | Medium | Acceptable |
| Context Manager (`with`) | High | High | **Yes** |
| Async Context Manager | High | High | **Yes** (async) |

## Patterns to remember

- Class `__enter__` / `__exit__`
- Async class `__aenter__` / `__aexit__`
- `@contextmanager` yielding a value
- `@asynccontextmanager`
- Multiple managers in one `with`
- `contextlib.suppress` for expected exceptions
- Parameterized managers (e.g. `DatabaseConnection(host, port)`)

## Anti-patterns

- Leaving files/handles open on exceptions
- Bare `except:` that swallows errors
- Fake non-runnable code
