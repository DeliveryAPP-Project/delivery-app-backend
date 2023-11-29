#bash/sh
up:
	python -m project run

db-init:
	flask db init

migrate:
	flask db migrate

upgrade:
	flask db upgrade

env-default:
	export FLASK_ENV=default
	export FLASK_APP=project
	python main.py

env-development:
	export FLASK_APP=project
	export FLASK_ENV=development
	python main.py

env-production:
	export FLASK_APP=project
	export FLASK_ENV=production
	python main.py

env-testing:
	export FLASK_APP=project
	export FLASK_ENV=testing
	python main.py