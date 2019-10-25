THIS_FILE := $(lastword $(MAKEFILE_LIST))

.DEFAULT_GOAL := help

python-version: ## Provides the Python version
	pipenv run python --version
.PHONY: python-version

setup: ## Sets up the Python environvent with Pipenv
	pipenv install --dev
.PHONY: setup

run: ## Run the app
	pipenv run python -m sample
.PHONY: run

test: ## Run the tests
	@pipenv run mamba spec --format=documentation
.PHONY: test

repl: ## Fire up the Repl
	pipenv run python
.PHONY: repl

help:
	@echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\1:\2/' | column -c2 -t -s :)"
.PHONY: help
.DEFAULT_GOAL := help
