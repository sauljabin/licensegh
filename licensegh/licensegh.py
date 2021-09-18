import os

import git
import yaml


class Licensegh:
    def __init__(self):
        self.repository = TemplatesRepository()
        self.licenses = []

    def init(self):
        self.repository.init()
        self.load_licenses()

    def load_licenses(self):
        for dirpath, dirnames, filenames in os.walk(self.repository.licenses_path):
            for license_path in filenames:
                self.licenses.append(License(os.path.join(dirpath, license_path)))


class License:
    def __init__(self, path):
        self.path = path
        self.directory, self.file_name = os.path.split(self.path)
        self.id = self.file_name.replace(".txt", "")

        self.description = ""
        self.name = ""
        self.text = ""

    def load(self):
        with open(self.path, "r") as file:
            full_text = file.read()
            file_parts = full_text.split("---")
            self.text = file_parts[-1].strip()

            yaml_data = yaml.safe_load(file_parts[-2])
            self.description = yaml_data["description"].strip()
            self.name = yaml_data["title"].strip()

    def __eq__(self, o):
        return self.id == o.id


class TemplatesRepository:
    def __init__(self):
        self.path = os.path.expanduser("~/.licensegh/choosealicense")
        self.licenses_path = os.path.join(self.path, "_licenses")
        self.remote = "https://github.com/github/choosealicense.com.git"

    def init(self):
        if os.path.isdir(self.path):
            repo = git.Repo(self.path)
            repo.remotes.origin.pull()
        else:
            git.Repo.clone_from(self.remote, self.path)
