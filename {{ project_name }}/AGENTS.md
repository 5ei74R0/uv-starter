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
