# {{cookiecutter.package_name}}

{{cookiecutter.project_short_description}}

## Commands

```bash
uv run pytest                  # Run tests
uv run ruff check .            # Lint
uv run ruff format .           # Format

# CLI Commands Here

```

## Setup

```bash
uv sync
```

## Dependencies

## Project Structure

```
.
├── {{cookiecutter.package_name}}
│   ├── assets
│   │   └── ascii-art-text.png
│   ├── CLAUDE.md
│   ├── docs
│   │   ├── logs.md
│   │   └── roadmap.md
│   ├── justfile
│   ├── pyproject.toml
│   ├── README.md
│   ├── src
│   │   └── {{cookiecutter.project_slug}}
│   │       ├── __init__.py
│   │       ├── __main__.py
│   │       ├── {{cookiecutter.project_slug}}.py
│   │       ├── cli.py
│   │       └── utils.py
│   └── tests
│       ├── __init__.py
│       └── test_{{cookiecutter.project_slug}}.py
├── CLAUDE.md
├── cookiecutter.json
├── docs
│   └── ascii-stellar-cookiecutter.png
├── hooks
│   ├── post_gen_project.py
│   └── pre_gen_project.py
├── justfile
├── pyproject.toml
├── README.md
├── run.py
├── tests
│   └── test_bake_project.py
└── uv.lock

10 directories, 25 files


```

## Code Style

- Python 3.14
- Type hints on all functions
- Google-style docstrings
- Line length: 80 characters
- Use `async`/`await` where supported
- Always use fstrings for `f"Text {var}"`
- 

## Architecture Notes


## Environment Variables
Store in .env file

```

```

## Testing

- Use pytest fixtures for mock Airtable responses
- Use in-memory DuckDB (`:memory:`) for storage tests

## Repository
 - @docs/logs.md: Use this to store the latest changes. Keep updates short
 - @docs/roadmap.md: The plan for the project