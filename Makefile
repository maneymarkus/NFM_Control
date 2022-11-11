# Makefile containing some general/generic management tasks that can and should be triggered from the command line
# Since entering the virtual environment (via `pipenv shell`) prevents executing further commands in the recipes
# this Makefile falls back to use pipenv scripts for some tasks
all: venv

init:
	python -m pip install --upgrade pip
	pip install pipenv
# install pipenv requirements
	pipenv install

# activate virtual environment (pipenv shell in this case)
venv:
	pipenv shell

test:
	pipenv run test

lint:
	pipenv run lint

.PHONY: all init venv test lint