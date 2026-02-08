![Stellar CookieCutter](docs/ascii-stellar-cookiecutter.png)

# Stellar Cookiecutter

A modern Python package template using current tooling. Forked from [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage.git).

## Features

- **uv** for dependency management
- **ruff** and **ty** for linting and type checking
- **pytest** for testing
- **Typer** CLI out of the box
- **GitHub Actions** CI for Python 3.10–3.13
- **Pre-commit hooks** configured
- Optional **data platform** scaffolding (pipelines, orchestration, transformation, visualisation)

## Quickstart

```bash
# Install cookiecutter
brew install cookiecutter

# Generate a project
cookiecutter https://github.com/stellarglyph/stellar-cookiecutter
```

## Template Variables

| Variable | Default | Description |
|---|---|---|
| `package_name` | `stellar-boilerplate` | Package directory name (with hyphens) |
| `project_name` | `Python Boilerplate` | Human-readable project name |
| `project_slug` | auto-derived | Python module name (underscores) |
| `project_command_line_alias` | auto-derived | CLI command (strips `stellar-` prefix) |
| `is_data_platform` | `no` | Add data platform folders (`pipelines/`, `orchestration/`, `transformation/`, `visualisation/`) |

## Development

```bash
just list          # Show available commands
just make          # Generate project without defaults
just bake          # Generate project with defaults
just clean         # Remove generated project
just watch         # Watch template and auto-regenerate

uv run pytest      # Run tests
uv run ruff check  # Lint
```