import subprocess
import sys


def main():
    unittest = subprocess.run(["poetry", "run", "python", "-m", "unittest", "-v"])
    sys.exit(unittest.returncode)


def analyze():
    print(">>> black")
    black = subprocess.run(["poetry", "run", "black", "--check", "."])

    print(">>> isort")
    isort = subprocess.run(["poetry", "run", "isort", "--check", "."])

    print(">>> flake8")
    flake8 = subprocess.run(["poetry", "run", "flake8", "."])

    print(">>> bandit")
    bandit = subprocess.run(["poetry", "run", "bandit", "-r", "licensegh/"])

    sys.exit(
        black.returncode or isort.returncode or flake8.returncode or bandit.returncode
    )


def multi_version_tests():
    tox = subprocess.run(["poetry", "run", "tox", "-q"])
    sys.exit(tox.returncode)


if __name__ == "__main__":
    main()
