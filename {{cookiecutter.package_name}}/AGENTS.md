# {{cookiecutter.package_name}}

{{cookiecutter.project_short_description}}


## Dependencies

## Project Structure
The project structure is displayed below
```

```

# Global rules
- Simplicity first. Fewer abstractions, fewer indirections, fewer files
- Tests should be used to verify all work, however only use the minimal amount of text required
- Keep dependencies minimal, and only use highly popular and trusted dependencies. Notify if a smaller dependency is to be used
- Use the justfile for common commands

## Docs and Natural Language
- Never use `—` always use `-`
- Always use British English
- Keep all text concise and don't use emojis
- If you start a web server, remember to always shut it down

## Python projects
- Use `uv`, `ruff` and `ty` exclusively for all projects
- Use f-strings in this format `f""`
- Docstrings should use the Google standard
- Type hints on all functions
- Line length: 90 characters
- Use `async`/`await` where supported
- Always use fstrings for `f"Text {var}"`
- 

# Navigation index
All project plans, todos and documentation created should be stored in the local `@docs` folder. Don't store any information outside this project.

Specific information:
`@README.md`: for information about the project
`@docs/roadmap.md`: for overal project roadmap and key milestones.
`@docs/architecture.md`: contains the system and code architecture.
`@docs/memory.md`: to be used to record findings and information that should be persisted across states.

# Conventions
- Always check the work that you have completed after a turn of work. Does it satisfy the original requirements and ask?
- Use test driven development where you can.

# References

## Architecture Notes


## Environment Variables
Store in .env file

```

```



