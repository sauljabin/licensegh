# licensegh

`licensegh` is a command line tool that generates a license file for a project from the github open source lincese templates

## Installation

## Usage

## Development

Install development tools:

- make sure you have `python3.7`, `python3.8`, `python3.9` aliases installed
- install [poetry](https://python-poetry.org/docs/#installation)

Installing development dependencies:
```sh
poetry install
```

Running multi version tests (`3.7`, `3.8`, `3.9`):
```sh
poetry run multi-version-tests
```

Running unit tests:
```sh
poetry run tests
```

Running code analysis:
```sh
poetry run analyze
```

Applying code styles:
```sh
poetry run styles
```

Running cli using `python3`:
```sh
python3 -m licensegh
```

Running cli using `poetry`:
```sh
poetry run licensegh
```

Runniging code coverage:
```sh
poetry run tests-coverage
```