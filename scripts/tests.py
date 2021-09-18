import subprocess
import sys


def main():
    unittest = subprocess.run(["poetry", "run", "python", "-m", "unittest", "-v"])
    sys.exit(unittest.returncode)


def analyze():
    print(">>> black", flush=True)
    black = subprocess.run(["poetry", "run", "black", "--check", "."])

    print(">>> isort", flush=True)
    isort = subprocess.run(["poetry", "run", "isort", "--check", "."])

    print(">>> flake8", flush=True)
    flake8 = subprocess.run(["poetry", "run", "flake8", "."])

    print(">>> bandit", flush=True)
    bandit = subprocess.run(["poetry", "run", "bandit", "-r", "licensegh/"])

    sys.exit(
        black.returncode or isort.returncode or flake8.returncode or bandit.returncode
    )


def multi_version_tests():
    tox = subprocess.run(["poetry", "run", "tox", "-q"])
    sys.exit(tox.returncode)


if __name__ == "__main__":
    main()
