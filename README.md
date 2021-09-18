# licensegh

![GitHub](https://img.shields.io/github/license/sauljabin/licensegh)
![GitHub branch checks state](https://img.shields.io/github/checks-status/sauljabin/licensegh/main?label=tests)
![Codecov](https://img.shields.io/codecov/c/github/sauljabin/licensegh)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/licensegh)
![PyPI](https://img.shields.io/pypi/v/licensegh)
![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/licensegh)

`licensegh` is a command line tool that generates a license file for a project from the github open source lincese templates

## Installation

```sh
pip install licensegh
```

## Usage

Generate a LICENSE file from a github template (`mit` example):
```sh
licensegh mit
```

Help:
```sh
Usage: licensegh [OPTIONS] <license id>

Options:
  -p, --print   Print the license file
  -s, --search  Search license, shows a list
  -l, --list    List all found licenses
  --version     Show the version and exit.
  -h, --help    Show this message and exit.
```

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