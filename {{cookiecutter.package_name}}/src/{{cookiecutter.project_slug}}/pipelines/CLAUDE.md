# Pipelines
This module contains the data pipelines for this project. {{cookiecutter.project_short_description}}

## Commands


## Dependencies


## Code Style

- Python 3.14
- Type hints on all functions
- Google-style docstrings
- Line length: 80 characters
- Use `async`/`await` where supported
- Always use fstrings for `f"Text {var}"`
- Always use standard logging

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