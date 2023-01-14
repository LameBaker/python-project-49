install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games

.PHONY: install brain-games
