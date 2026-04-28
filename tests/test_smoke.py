"""Smoke tests — verify the package is importable and CLI entry point is callable."""

from typer.testing import CliRunner

from narrator_ai import __version__
from narrator_ai.cli import app

runner = CliRunner()


def test_version_importable():
    """Package version should be a non-empty string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_cli_help():
    """CLI --help should exit 0 and show usage info."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "narrator-ai-cli" in result.output.lower() or "narrat" in result.output.lower()


def test_cli_version():
    """CLI --version should print version and exit 0."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_cli_no_args_shows_help():
    """Running with no arguments should display help text (no_args_is_help=True)."""
    result = runner.invoke(app, [])
    assert "narrator" in result.output.lower() or "usage" in result.output.lower()
