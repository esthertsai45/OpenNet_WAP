.PHONY: format
format:
	isort --atomic --profile black pages tests
	black pages tests

.PHONY: check
check:
	flake8 pages tests --max-line-length 140
	black --check pages tests
	mypy --ignore-missing-imports --check-untyped-defs --no-namespace-packages pages tests
