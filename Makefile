.PHONY: setup lint clean

# Python virtual environment directory
VENV := .venv

# Setup virtual environment and install dependencies
setup:
	uv venv $(VENV)
	. $(VENV)/bin/activate

# Run ruff linter on all Python files
lint:
	uv run ruff check .

# Run ruff formater on all Python files
format:
	uv run ruff format .

# Clean up virtual environment
clean:
	rm -rf .ruff_cache