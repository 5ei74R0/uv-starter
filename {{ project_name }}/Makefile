.PHONY: fmt lint test cov sync

fmt:
	uv run ruff format .
	uv run ruff check --fix .
lint:
	uv run ruff check .
	uv run ty check .
test:
	uv run pytest tests
cov:
	uv run pytest --cov=src --cov-report=html tests
sync:
	uv sync --all-groups
