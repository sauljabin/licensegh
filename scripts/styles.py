import os


def main():
    os.system("poetry run black .")
    os.system("poetry run isort .")


if __name__ == "__main__":
    main()
