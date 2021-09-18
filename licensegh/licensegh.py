import os

import git
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Licensegh:
    def __init__(self):
        self.repository = TemplatesRepository()
        self.licenses = []

    def init(self):
        self.repository.init()


class Licence:
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

            yaml_data = yaml.load(file_parts[-2], Loader=Loader)
            self.description = yaml_data["description"]
            self.name = yaml_data["title"]


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
