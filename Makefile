V=$(shell git describe --tags --abbrev=0 | sed "s/v//")
USERNAME='__token__'
PASSWORD='foo'

poetry.install:
	poetry install

poetry.config.test_pypi_repo:
	poetry config repositories.testpypi https://test.pypi.org/legacy/

poetry.config.test_pypi_token:
	poetry config pypi-token.testpypi $(TOKEN)

poetry.config.native:
	poetry config virtualenvs.create false

poetry.config.venv:
	poetry config virtualenvs.create true
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.path .

bump.version:
	poetry version $(V)
	sed 's/=.*/= "$(V)"/' -i py_bdd_context/__init__.py

test:
	python -m unittest $(args)

test.failure:
	python -m unittest examples.failure

fmt:
	black .
	make fmt.check

fmt.check:
	black --check .
	flake8

package.build: bump.version
	poetry build

package.publish.test:
	poetry publish -r testpypi

package.publish:
	poetry publish -u $(USERNAME) -p $(PASSWORD)

package.build_and_publish: package.build package.publish

install.test:
	pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ py-bdd-context==$(V)
