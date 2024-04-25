.PHONY: docs

test:
	python -m unittest discover -s tests

docs:
	sphinx-apidoc -o docs/ src/
	sphinx-build -b html docs/ build/