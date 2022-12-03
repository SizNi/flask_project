export PYTHONPATH=src

console:
	@poetry run flask shell

start:
	poetry run flask run -h 0.0.0.0 -p 8080

test:
	poetry run pytest -vv tests
