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