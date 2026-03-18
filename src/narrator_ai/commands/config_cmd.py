"""Config management commands."""

import typer

from narrator_ai.config import CONFIG_FILE, load_config, save_config
from narrator_ai.output import print_dict, print_success

app = typer.Typer(
    help=(
        "Manage CLI configuration.\n\n"
        "Config is stored in ~/.narrator-ai/config.yaml.\n"
        "Environment variables NARRATOR_SERVER, NARRATOR_APP_KEY, NARRATOR_TIMEOUT, NARRATOR_OUTPUT override config values."
    ),
)


@app.command()
def init(
    server: str = typer.Option(..., prompt="Server URL (e.g. https://api.example.com)"),
    app_key: str = typer.Option(..., prompt="App Key"),
    output: str = typer.Option("table", help="Default output format: table or json"),
    timeout: int = typer.Option(30, help="Request timeout in seconds"),
):
    """Initialize configuration interactively. Prompts for server URL and app key."""
    config = {
        "server": server.rstrip("/"),
        "app_key": app_key,
        "output": output,
        "timeout": timeout,
    }
    save_config(config)
    print_success(f"Config saved to {CONFIG_FILE}")


@app.command()
def show(
    json: bool = typer.Option(False, "--json", help="Output as JSON"),
):
    """Show current configuration (app key is always masked)."""
    cfg = load_config()
    # Always mask the app key to prevent leaking in logs
    if cfg.get("app_key"):
        key = cfg["app_key"]
        if len(key) > 8:
            cfg["app_key"] = key[:4] + "****" + key[-4:]
        else:
            cfg["app_key"] = "****"
    print_dict(cfg, title="Configuration", json_mode=json)


@app.command("set")
def set_value(
    key: str = typer.Argument(..., help="Config key: server, app_key, output, timeout"),
    value: str = typer.Argument(..., help="Config value"),
):
    """Set a single configuration value.

    Examples:
      narrator-ai-cli config set server https://api.example.com
      narrator-ai-cli config set app_key your_api_key
      narrator-ai-cli config set output json
      narrator-ai-cli config set timeout 60
    """
    cfg = load_config()
    if key not in ("server", "app_key", "output", "timeout"):
        raise typer.BadParameter(f"Unknown config key: {key}. Valid: server, app_key, output, timeout")
    if key == "timeout":
        cfg[key] = int(value)
    elif key == "server":
        cfg[key] = value.rstrip("/")
    else:
        cfg[key] = value
    save_config(cfg)
    print_success(f"Set {key} = {value}")
