# licensegh

<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-python-success?logo=python&logoColor=white"></a>
<a href="https://github.com/sauljabin/licensegh"><img alt="GitHub" src="https://img.shields.io/badge/status-active-brightgreen"></a>
<a href="https://github.com/sauljabin/licensegh/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/github/license/sauljabin/licensegh"></a>
<a href="https://github.com/sauljabin/licensegh/actions"><img alt="GitHub Actions" src="https://img.shields.io/github/checks-status/sauljabin/licensegh/main?label=tests"></a>
<a href="https://app.codecov.io/gh/sauljabin/licensegh"><img alt="Codecov" src="https://img.shields.io/codecov/c/github/sauljabin/licensegh"></a>
<a href="https://pypi.org/project/licensegh"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/licensegh"></a>
<a href="https://pypi.org/project/licensegh"><img alt="Version" src="https://img.shields.io/pypi/v/licensegh"></a>
<a href="https://libraries.io/pypi/licensegh"><img alt="Dependencies" src="https://img.shields.io/librariesio/release/pypi/licensegh"></a>
<a href="https://pypi.org/project/licensegh"><img alt="Platform" src="https://img.shields.io/badge/platform-linux%20%7C%20osx-blueviolet"></a>

`licensegh` is a command line tool that generates a `LICENSE` file for a project from the [github license templates repository](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses).

![https://raw.githubusercontent.com/sauljabin/licensegh/main/screenshots/options.png](https://raw.githubusercontent.com/sauljabin/licensegh/main/screenshots/options.png)

## Installation

Install with pip:
```sh
pip install licensegh
```

Upgrade with pip:
```sh
pip install --upgrade licensegh
```

## Usage

Help:
```sh
licensegh -h
```

Version:
```sh
licensegh --version
```

List all licenses:
```sh
licensegh -l
```

Search licenses:
```sh
licensegh -s
```

Print a license: 
```sh
licensegh -p
```

Reset github template repository:
```sh
licensegh --reset
```

Save a license:
```sh
licensegh mit
```

## Development

Installing poetry:
```sh
pip install poetry
```

Installing development dependencies:
```sh
poetry install
```

Running unit tests:
```sh
poetry run python -m scripts.tests
```

Running multi version tests (`3.7`, `3.8`, `3.9`):

> Make sure you have `python3.7`, `python3.8`, `python3.9` aliases installed

```sh
poetry run python -m scripts.multi-version-tests
```

Applying code styles:
```sh
poetry run python -m scripts.styles
```

Running code analysis:
```sh
poetry run python -m scripts.analyze
```

Running code coverage:
```sh
poetry run python -m scripts.tests-coverage
```

Running cli using `poetry`:
```sh
poetry run licensegh
```
