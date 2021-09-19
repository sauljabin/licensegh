import os
import re
import shutil

import git
import yaml
from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


class Licensegh:
    def __init__(self):
        self.repository = TemplatesRepository()
        self.licenses = []

    def init(self):
        self.repository.init()
        self.load_licenses()

    def load_licenses(self):
        for dirpath, dirnames, filenames in os.walk(self.repository.licenses_path):
            filenames = [
                filename for filename in filenames if filename.endswith(".txt")
            ]
            filenames.sort()
            for license_path in filenames:
                self.licenses.append(License(os.path.join(dirpath, license_path)))

    def print_all_licenses(self):
        self.print_licenses(self.licenses)

    def print_license_by_id(self, license_id):
        licenses = [license for license in self.licenses if license_id == license.id]

        if len(licenses) == 0:
            console = Console()
            console.print("[red]License not found[red]")
        else:
            licenses[0].load()
            licenses[0].print()

    def print_licenses_by_id(self, license_id):
        licenses = [
            license
            for license in self.licenses
            if re.match(".*({}).*".format(license_id), license.id)
        ]

        if len(licenses) == 0:
            console = Console()
            console.print("[red]Licenses not found[red]")
        else:
            self.print_licenses(
                licenses,
                True,
            )

    def print_licenses(self, licenses, print_description=False):
        console = Console()

        table = Table(box=box.HORIZONTALS)
        table.add_column("Id", style="cyan", justify="right")
        table.add_column("Name", style="magenta")

        for license in licenses:
            license.load()
            if print_description:
                table.add_row(
                    license.id,
                    "{}\n[white]{}[white]".format(license.name, license.description),
                )
            else:
                table.add_row(license.id, license.name)

        console.print(table)

    def save_license_by_id(self, license_id):
        licenses = [license for license in self.licenses if license_id == license.id]

        if len(licenses) == 0:
            console = Console()
            console.print("[red]License not found[red]")
        else:
            licenses[0].load()
            licenses[0].save()

    def reset_repository(self):
        self.repository.remove()


class License:
    def __init__(self, path):
        self.path = path
        self.directory, self.file_name = os.path.split(self.path)
        self.id = self.file_name.replace(".txt", "")

        self.description = ""
        self.name = ""
        self.text = ""
        self.arguments = []

    def load(self):
        with open(self.path, "r") as file:
            full_text = file.read()
            cut_index = full_text.find("---", 3)
            file_parts = {
                "metadata": full_text[:cut_index],
                "text": full_text[cut_index + 3 :],
            }

            metadata = yaml.safe_load(file_parts["metadata"])
            self.description = metadata["description"].strip()
            self.name = metadata["title"].strip()
            self.text = file_parts["text"].strip()
            self.arguments = list(set(re.findall(r"\[([a-z]+)\]", self.text)))

    def print(self):
        console = Console()
        console.print(
            "[green]Name:[green]\t[magenta bold]{}[magenta bold]".format(self.name)
        )
        console.print(
            "[green]Id:[green]\t[magenta bold]{}[magenta bold]".format(self.id)
        )
        console.rule()
        console.print(self.text.replace("[", r"\["))

    def save(self):
        text_to_save = self.text

        for argument in self.arguments:
            value = Prompt.ask(
                f"[magenta]Enter argument[magenta] [cyan]{argument}[cyan]"
            )
            text_to_save = text_to_save.replace(f"[{argument}]", value)

        with open("LICENSE", "w") as file:
            file.write(text_to_save)

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

    def remove(self):
        shutil.rmtree(self.path)
