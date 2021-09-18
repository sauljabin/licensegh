import os
import subprocess
import sys


def main():
    poetry = subprocess.run(["poetry", "run", "python", "-m", "unittest", "-v"])
    sys.exit(poetry.returncode)


def analyze():
    os.system("poetry run black --check .")
    os.system("poetry run isort --check .")
    os.system("poetry run flake8 .")
    os.system("poetry run bandit -r licensegh/")


def multi_version_tests():
    poetry = subprocess.run(["poetry", "run", "tox", "-q"])
    sys.exit(poetry.returncode)


if __name__ == "__main__":
    main()
