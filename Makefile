# Makefile project management for local and ci environments

# Color output
START="\033[0;32m\#\#\# "
END=" \#\#\# \033[0m"

# Environment variables
PYTHON_VENV="$(shell pwd)/.venv/bin/python"
POETRY_BIN="$(shell which poetry)"
DISTPATH="$(shell pwd)/dist"
POETRY_CACHE_DIR=${HOME}/.cache/pypoetry

.PHONY: pre-install install install-prod update generate-requirements clean clean-cache clean-all

pre-install:
	$(POETRY_BIN) config virtualenvs.create true || exit 1; \
	$(POETRY_BIN) config virtualenvs.in-project true || exit 1;

install:
	$(POETRY_BIN) install --no-root || exit 1

install-prod:
	$(POETRY_BIN) install --no-dev --no-root || exit 1

update:
	$(POETRY_BIN) update || exit 1

generate-requirements:
	@echo -e $(START)'Generating requirements.txt'$(END)
	$(POETRY_BIN) export --without-hashes --dev --format requirements.txt > requirements.txt || exit 1

clean:
	@echo -e $(START)'Cleaning build and egg directories'$(END)
	rm -rf $(DISTPATH)
	rm -rf *.egg-info/

clean-cache:
	@echo -e $(START)'Clearing poetry cache'$(END)
	rm -rf $(POETRY_CACHE_DIR)

clean-all: clean clean-cache
	@echo -e $(START)'Clean all work files'$(END)
	rm -rf ./.venv
