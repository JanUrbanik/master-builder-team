"""
Reference memory: Resource management patterns.
Source chat: Code & Execution Specialist development (async/context managers).
Agent owner: 08 Code & Execution Specialist
"""

from __future__ import annotations

from contextlib import asynccontextmanager, contextmanager, suppress
from typing import Any, AsyncIterator, Iterator, Optional


# --- Pattern 1: Manual (NOT recommended) ---
def manual_read(path: str) -> str:
    file = open(path, "r", encoding="utf-8")
    data = file.read()
    file.close()
    return data


# --- Pattern 2: try / finally ---
def try_finally_read(path: str) -> str:
    file = open(path, "r", encoding="utf-8")
    try:
        return file.read()
    finally:
        file.close()


# --- Pattern 3: Context manager (recommended) ---
def with_read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


# --- Pattern 4: Class-based custom context manager ---
class CustomResource:
    def __enter__(self) -> "CustomResource":
        # Setup
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # Cleanup
        return None


# --- Pattern 5: Async class-based context manager ---
class AsyncResource:
    async def __aenter__(self) -> "AsyncResource":
        # Setup
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        # Cleanup
        return None


# --- Pattern 6: contextlib decorator form ---
@contextmanager
def managed_resource() -> Iterator[str]:
    resource = "acquired"
    try:
        yield resource
    finally:
        # release
        pass


@asynccontextmanager
async def async_managed_resource() -> AsyncIterator[str]:
    resource = "acquired-async"
    try:
        yield resource
    finally:
        # release
        pass


# --- Pattern 7: parameterized class context manager ---
class DatabaseConnection:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.conn: Optional[Any] = None

    def __enter__(self) -> Any:
        # Placeholder for connect(self.host, self.port)
        self.conn = f"connected://{self.host}:{self.port}"
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn = None


# --- Pattern 8: suppress + multi-with ---
def safe_remove(path: str) -> None:
    with suppress(FileNotFoundError):
        import os

        os.remove(path)


def copy_text(src: str, dst: str) -> None:
    with open(src, "r", encoding="utf-8") as infile, open(
        dst, "w", encoding="utf-8"
    ) as outfile:
        outfile.write(infile.read())


# Preference ranking from chat:
# Manual < try/finally < with / async with (preferred for SuperGrok Heavy code work)
