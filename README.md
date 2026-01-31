# 🐍 Modern Python Production Boilerplate

A professional, opinionated, and "zero-touch" Python project template. Built for developers who want industry-standard tooling, automated versioning, and strict quality gates out of the box.

[![Maintenance](https://img.shields.io/badge/Maintained%20with-Cruft-1f425f.svg)](https://github.com/cruft/cruft)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Security: mypy](https://img.shields.io/badge/Types-Mypy-blue.svg)](https://github.com/python/mypy)

## ✨ Key Features
* **Source Layout**: Clean `src/` directory structure to prevent accidental imports.
* **Modern Tooling**: `ruff` for linting/formatting and `mypy` for strict type checking.
* **Makefile Automation**: Single-word commands for environment setup, testing, and releasing.
* **100% Coverage Gate**: CI/CD pipeline fails if test coverage drops below 100%.
* **Automated SemVer**: Version bumping and Git tagging via `make release`.
* **Cruft Enabled**: Easily sync updates from this template back into your project.

## 🚀 Quick Start

### 1. Generate Project
Ensure you have `cruft` installed: `pip install cruft`

```bash
cruft create https://github.com/ashwinbhola/python-cookiecutter
```

### 2. Development Workflow
The `Makefile` handles everything. Just run:

```bash
make install-requirements  # Sets up a python env with all the installed dependencies
make fix-lint  # Format code and fix lint errors
make lint  # Run linting checks
make test  # Run tests
make bump PART=minor  # Increment version
make help  # View all make commands
```

## 🛠 Tech Stack
- **Build System**: [Setuptools](https://setuptools.pypa.io/) (via pyproject.toml)
- **Linting**: [Ruff](https://github.com/astral-sh/ruff)
- **Testing**: [Pytest](https://docs.pytest.org/) + [Pytest-Cov](https://pytest-cov.readthedocs.io/)
- **Versioning**: [bump-my-version](https://github.com/callowayproject/bump-my-version)
- **CI/CD**: GitHub Actions (Linting, Testing, and Auto-Release)