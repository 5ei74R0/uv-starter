---
name: quality-check
description: Check the code quality with project specific tools and suggest improvements.
---

To check the code quality of the project, we should use `make` commands:
```bash
make fmt lint  # Format the code and check for linting and type issues
make cov       # Run tests and check code coverage
```

These commands will help us identify any formatting issues, linting errors, type errors, and ensure that our tests are running correctly with good coverage. If there are any issues, the output from these commands will provide details on what needs to be fixed.
