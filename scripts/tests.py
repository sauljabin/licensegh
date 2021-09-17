import os


def main():
    os.system("poetry run python -m unittest -v")


def analyze():
    os.system("poetry run black --check .")
    os.system("poetry run isort --check .")
    os.system("poetry run flake8 .")
    os.system("poetry run bandit -r licensegh/")


def multi_version_tests():
    os.system("poetry run tox -q")


if __name__ == "__main__":
    main()
