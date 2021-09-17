import os

import git


class LicenseGH:
    pass


class Licence:
    pass


class TemplatesRepository:
    def __init__(self):
        self.path = "~/licensegh/choosealicense"
        self.licenses_path = os.path.join(self.path, "_licenses")
        self.remote = "https://github.com/github/choosealicense.com.git"

    def init(self):
        if os.path.isdir(self.path):
            repo = git.Repo(self.path)
            repo.remotes.origin.pull()
        else:
            git.Repo.clone_from(self.remote, self.path)
