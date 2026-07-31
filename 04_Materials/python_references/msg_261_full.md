Here are the **Advanced Context Manager Patterns** worth knowing:

### 1. Context Manager with State / Values
```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire_resource()
    try:
        yield resource          # This value is returned to the `as` variable
    finally:
        release_resource(resource)
```

### 2. Reusable Context Manager Class with Parameters
```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.conn = connect(self.host, self.port)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
```

### 3. Suppressing Specific Exceptions
```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp_file.txt")
```

### 4. Multiple Context Managers in One `with`
```python
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

### 5. Async Context Manager with `contextlib.asynccontextmanager`
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource():
    resource = await acquire_async()
    try:
        yield resource
    finally:
        await release_async(resource)
```

### 6. Context Manager that Returns Different Values on Exception
More advanced pattern where cleanup behavior changes depending on whether an exception occurred.

---

**Would you like me to add the most important advanced patterns into the Code & Execution Specialist agent?**