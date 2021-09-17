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

Runing tests:
```sh
poetry run tox -q
```

Applying code styles:
```sh
poetry run styles
```

Running using `python3`:
```sh
python3 -m licensegh
```

Running using `poetry`:
```sh
poetry run licensegh
```