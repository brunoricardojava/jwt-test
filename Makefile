install:
	uv venv
	uv sync

run:
	manage.py runserver localhost:8000

test:
	pytest -vv

coverage_report:
	coverage run -m pytest -vv
	coverage xml
	coverage html
	coverage report