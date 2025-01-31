install:
	uv venv
	uv sync

run:
	manage.py runserver localhost:8000

test:
	coverage run -m pytest -vv
	coverage xml
	coverage html
	coverage report