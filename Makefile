install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

make lint:
	poetry run flake8 gendiff
