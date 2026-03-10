# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Cookiecutter template for generating modern Python packages. It produces projects with uv, ruff, ty, pytest, typer CLI, and GitHub Actions CI.

## Commands

```bash
# Development (justfile)
just list                      # Show available commands
just bake                      # Generate project with defaults (no prompts)
just bake ""                   # Generate project with prompts
just clean                     # Remove generated stellar-boilerplate directory
just watch                     # Watch template and auto-regenerate on changes

# Alternative watcher
uv run python run.py           # Watch {{cookiecutter.package_name}}/ for changes

# Testing
uv run pytest                  # Run all tests
uv run pytest -k test_bake_with_defaults  # Run single test

# Linting
uv run ruff check .            # Lint
uv run ruff format .           # Format
```

## Architecture

```
├── cookiecutter.json          # Template variables and defaults
├── hooks/
│   ├── pre_gen_project.py     # Validates project_slug is valid Python module name
│   └── post_gen_project.py    # Post-generation success message
├── {{cookiecutter.package_name}}/  # Template directory (Jinja2 templated)
│   ├── src/{{cookiecutter.project_slug}}/  # Generated package source
│   └── tests/                 # Generated test files
├── tests/
│   └── test_bake_project.py   # Tests using pytest-cookies
├── run.py                     # File watcher for development
└── justfile                   # Development task runner
```

## Template Variables

Key variables in `cookiecutter.json`:
- `package_name`: Directory/package name with hyphens (e.g., `stellar-myproject`)
- `project_slug`: Python module name, auto-derived by replacing hyphens with underscores
- `project_command_line_alias`: CLI command name, auto-derived by stripping `stellar-` prefix

## Testing Notes

Tests use `pytest-cookies` which provides a `cookies` fixture for baking templates in temp directories. The `bake_in_temp_dir` context manager ensures cleanup after tests.

## Code Style

- Python 3.10+
- Type hints on all functions
- Line length: 80 characters
- Ruff excludes the template directory (`*cookiecutter.package_name*`) from linting
