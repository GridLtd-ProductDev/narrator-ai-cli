"""User management commands."""

import typer

from narrator_ai.client import NarratorClient, NarratorAPIError
from narrator_ai.output import print_dict, print_error, print_json, print_table

app = typer.Typer(help="User account management: balance, authentication, and API key operations.")


def _client() -> NarratorClient:
    return NarratorClient()


@app.command()
def balance(
    json: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Query account balance and user info.

    Returns: user_id, nickname, mobile (masked), balance, company_name.
    """
    try:
        data = _client().get("/v1/users/balance")
        print_dict(data, title="Account Balance", json_mode=json)
    except NarratorAPIError as e:
        print_error(e.message, e.code)
        raise typer.Exit(1)


@app.command()
def login(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True, hide_input=True),
    json: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Login with username/password and get access token.

    Note: This endpoint does not require an app-key.
    Returns: access_token, expire, user_id, nickname, uuid, company_name.
    """
    try:
        from narrator_ai.config import get_server
        client = NarratorClient(server=get_server(), app_key="")
        data = client.post("/v1/users/sign_in", json={
            "username": username,
            "password": password,
        })
        print_dict(data, title="Login Success", json_mode=json)
    except NarratorAPIError as e:
        print_error(e.message, e.code)
        raise typer.Exit(1)


@app.command()
def keys(
    page: int = typer.Option(1, help="Page number"),
    page_size: int = typer.Option(10, help="Items per page"),
    json: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """List sub API keys under the current account.

    Returns: total, page, page_size, items[{id, app_key, credit_quota, credit_quota_balance, status, remark}].
    """
    try:
        data = _client().get("/v1/users/app_key/sub/list", params={
            "page": page,
            "page_size": page_size,
        })
        if json:
            print_json(data)
        else:
            items = data.get("items", [])
            columns = [
                ("id", "ID"),
                ("app_key", "App Key"),
                ("credit_quota", "Quota"),
                ("credit_quota_balance", "Balance"),
                ("status", "Status"),
                ("remark", "Remark"),
                ("created_at", "Created"),
            ]
            print_table(items, columns, title=f"Sub Keys (total: {data.get('total', 0)})")
    except NarratorAPIError as e:
        print_error(e.message, e.code)
        raise typer.Exit(1)


@app.command("create-key")
def create_key(
    remark: str = typer.Option("", help="Description/label for the sub key"),
    quota: float = typer.Option(0, help="Initial point quota for the sub key"),
    json: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Create a new sub API key with optional quota and remark."""
    try:
        data = _client().post("/v1/users/app_key/create", json={
            "remark": remark,
            "quota": quota,
        })
        print_dict(data, title="Sub Key Created", json_mode=json)
    except NarratorAPIError as e:
        print_error(e.message, e.code)
        raise typer.Exit(1)
