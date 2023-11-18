install:
	pip install -r requirements.prod

install-dev:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.dev
	pre-commit install

lint:
	pylint *.py

test:
	pytest

run:
	waitress-serve --host 127.0.0.1 main:app

run-dev:
	flask --app main --debug run
