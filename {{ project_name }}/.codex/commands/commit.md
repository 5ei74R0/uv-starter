Prepare the current changes for commit.

Steps:
1. `make fmt` — format code
2. `make lint` — verify lint and types
3. `make test` — run tests
4. If all pass, show `git diff --stat` and suggest a concise commit message following Conventional Commits format (e.g. `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`)
5. Do NOT commit without user confirmation
