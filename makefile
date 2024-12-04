#bash/sh
up:
	python -m project run

up-prod:
	export FLASK_ENV=production && export FLASK_ENV=production && gunicorn -w 4 -b 0.0.0.0:5000 "project:create_app()"

up-homologacao:
	export FLASK_APP=project && export FLASK_ENV=homologacao && python -m project run

db-init:
	flask db init

migrate:
	flask db migrate

upgrade:
	flask db upgrade

env-default:
	export FLASK_ENV=default && export FLASK_APP=project && python -m project run

env-development:
	export FLASK_APP=project && export FLASK_ENV=development && python -m project run

env-production:
	export FLASK_APP=project && export FLASK_ENV=production && python -m project run

env-testing:
	export FLASK_APP=project && export FLASK_ENV=testing && python -m project run

test:
	coverage run -m pytest && coverage report && coverage html

format:
	pylint project && ruff check && ruff format