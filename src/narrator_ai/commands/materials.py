"""Pre-built movie materials (video + SRT file IDs) for task creation."""

import typer

from narrator_ai import DOCS_URL
from narrator_ai.client import NarratorAPIError, NarratorClient
from narrator_ai.output import console, print_error, print_json, print_table

app = typer.Typer(
    help=(
        "Pre-built movie materials for task creation.\n\n"
        "These are ready-to-use video and SRT files. Use the file IDs directly\n"
        "in episodes_data when creating generate-writing or fast-clip-data tasks.\n\n"
        "View material previews: https://ceex7z9m67.feishu.cn/wiki/WLPnwBysairenFkZDbicZOfKnbc"
    ),
)

_API_PATH = "/v2/res/movie-sucai"


def _client() -> NarratorClient:
    return NarratorClient()


@app.command("list")
def list_materials(
    page: int = typer.Option(1, "--page", "-p", help="Page number"),
    size: int = typer.Option(100, "--size", "-n", help="Items per page"),
    json_mode: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """List pre-built movie materials (video + SRT file IDs).

    Use these file IDs directly in episodes_data for task creation.
    The video_file_id is used as both video_oss_key and negative_oss_key,
    and srt_file_id is used as srt_oss_key.

    View material previews: https://ceex7z9m67.feishu.cn/wiki/WLPnwBysairenFkZDbicZOfKnbc
    """
    try:
        data = _client().get(_API_PATH, params={"page": page, "size": size})
        total = data.get("total", 0)
        items = data.get("items", [])

        if not items:
            print_error("No materials found.")
            raise typer.Exit(1)

        if json_mode:
            print_json({"total": total, "page": page, "size": size, "items": items})
        else:
            columns = [
                ("name", "Title (CN)"),
                ("title", "Title (EN)"),
                ("year", "Year"),
                ("type", "Genre"),
                ("video_file_id", "Video ID"),
                ("srt_file_id", "SRT ID"),
                ("character_name", "Stars"),
                ("story_info", "Summary"),
            ]
            print_table(items, columns, title=f"Movie Materials (page {page}, {len(items)}/{total})")
            console.print(f"\n[dim]View previews: {DOCS_URL}[/dim]")
    except NarratorAPIError as e:
        print_error(e.message, e.code)
        raise typer.Exit(1)
