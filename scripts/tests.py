import subprocess
import sys
from functools import reduce


def main():
    poetry = subprocess.run(["poetry", "run", "python", "-m", "unittest", "-v"])
    sys.exit(poetry.returncode)


def analyze():
    results = [
        subprocess.run(["poetry", "run", "black", "--check", "."]).returncode,
        subprocess.run(["poetry", "run", "isort", "--check", "."]).returncode,
        subprocess.run(["poetry", "run", "flake8", "."]).returncode,
        subprocess.run(["poetry", "run", "bandit", "-r", "licensegh/"]).returncode,
    ]
    sys.exit(reduce(lambda x, y: x or y, results))


def multi_version_tests():
    poetry = subprocess.run(["poetry", "run", "tox", "-q"])
    sys.exit(poetry.returncode)


if __name__ == "__main__":
    main()
