install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff

make lint:
	poetry run flake8 gendiff

test-coverage:
	pytest --cov=gendiff --cov-report xml tests/
