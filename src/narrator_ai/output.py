"""Output formatting for CLI responses.

Supports JSON mode (for agents) and rich table mode (for humans).
"""

import json
import sys
from typing import Any, Optional

from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table

console = Console()
err_console = Console(stderr=True)


def print_json(data: Any):
    """Print raw JSON to stdout (agent-friendly)."""
    print(json.dumps(data, ensure_ascii=False, indent=2, default=str))


def print_error(message: str, code: Optional[int] = None):
    prefix = f"[{code}] " if code else ""
    err_console.print(f"[red]Error: {escape(prefix + message)}[/red]")


def print_success(message: str):
    err_console.print(f"[green]{message}[/green]")


def print_info(message: str):
    err_console.print(f"[blue]{message}[/blue]")


def print_dict(data: dict, title: Optional[str] = None, json_mode: bool = False):
    """Print a dict as JSON or a rich panel."""
    if json_mode:
        print_json(data)
        return
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Key", style="cyan", no_wrap=True)
    table.add_column("Value")
    for k, v in data.items():
        table.add_row(str(k), str(v))
    if title:
        console.print(Panel(table, title=title, border_style="blue"))
    else:
        console.print(table)


def print_table(
    items: list[dict],
    columns: list[tuple[str, str]],
    title: Optional[str] = None,
    json_mode: bool = False,
):
    """Print a list of dicts as JSON or a rich table.

    columns: list of (key, display_name) tuples.
    """
    if json_mode:
        print_json(items)
        return
    table = Table(title=title, show_lines=False)
    for key, name in columns:
        table.add_column(name, no_wrap=(key in ("task_id", "file_id", "status")))
    for item in items:
        row = [str(item.get(key, "")) for key, _ in columns]
        table.add_row(*row)
    console.print(table)


def print_sse_event(event_type: str, data: dict, json_mode: bool = False):
    """Print an SSE event."""
    if json_mode:
        print_json({"event": event_type, "data": data})
        sys.stdout.flush()
        return
    if event_type == "event_close":
        return
    msg = data.get("message", data.get("status", ""))
    progress = data.get("progress")
    if progress is not None:
        err_console.print(f"  [{event_type}] {escape(str(msg))} ({progress}%)")
    elif msg:
        err_console.print(f"  [{event_type}] {escape(str(msg))}")
    else:
        err_console.print(f"  [{event_type}] {escape(str(data))}")
