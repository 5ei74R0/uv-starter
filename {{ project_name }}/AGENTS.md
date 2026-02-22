# Project: {{ project_name }}

## Tech Stack

- Language: Python {{ python_version }}
- Package Manager: uv
- Build Backend: hatchling
- Linter / Formatter: ruff
- Type Checker: ty
- Testing: pytest + pytest-cov

## Project Structure

```
{{ project_name }}/
├── src/{{ project_name }}/   # Source code
├── tests/                    # Test files
├── pyproject.toml            # Project configuration
└── Makefile                  # Development commands
```

This project uses the **src layout**. All source code lives under `src/{{ project_name }}/`.

## Commands

- `make fmt` — Format code with ruff (format + import sort + auto-fix)
- `make lint` — Run ruff linter and ty type checker
- `make test` — Run tests with pytest
- `make cov` — Run tests with coverage report (HTML output in `htmlcov/`)
- `make sync` — Sync all dependencies including dev

## Code Style

- Formatter: `ruff format` (Black-compatible)
- Lint rules: E (pycodestyle errors), F (pyflakes), I (isort), W (pycodestyle warnings)
- Always run `make fmt` before committing

## Testing

- Test files go in `tests/` and must be prefixed with `test_`
- Run `make test` to execute tests
- Run `make lint` after making changes to verify type safety and style

## Workflow

1. Make changes
2. `make fmt` — format
3. `make lint` — verify lint and types pass
4. `make test` — verify tests pass
5. Commit

## Commands

- `/check` — Format + lint + type check in one step
- `/test` — Run tests and analyze failures
- `/commit` — Full pre-commit flow (fmt → lint → test → suggest commit message)
- `/review` — Review uncommitted changes for issues

## Skills

### Adding a new module
1. Create `src/{{ project_name }}/<module>.py`
2. Create `tests/test_<module>.py` with corresponding tests
3. Run `/check` to verify

### Adding a dependency
1. `uv add <package>` for runtime deps
2. `uv add --group dev <package>` for dev-only deps
3. Run `make sync` to update lockfile
