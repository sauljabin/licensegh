import subprocess
import sys


def main():
    unittest = subprocess.run(["poetry", "run", "python", "-m", "unittest", "-v"])
    sys.exit(unittest.returncode)


def tests_coverage():
    print(">>> coverage", flush=True)
    coverage = subprocess.run(
        [
            "poetry",
            "run",
            "coverage",
            "run",
            "--source",
            "licensegh",
            "-m",
            "unittest",
            "-v",
        ]
    )

    print(">>> coverage report", flush=True)
    coverage_report = subprocess.run(["poetry", "run", "coverage", "report", "-m"])

    print(">>> coverage html", flush=True)
    coverage_html = subprocess.run(["poetry", "run", "coverage", "html"])

    print(">>> coverage xml", flush=True)
    coverage_xml = subprocess.run(["poetry", "run", "coverage", "xml"])
    sys.exit(
        coverage.returncode
        or coverage_html.returncode
        or coverage_xml.returncode
        or coverage_report.returncode
    )


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
