import os
import unittest
from unittest.mock import MagicMock, call, mock_open, patch

from faker import Faker

from licensegh import __version__
from licensegh.licensegh import License, Licensegh, TemplatesRepository

faker = Faker()
license_text = """
---
title: MIT License
spdx-id: MIT
featured: true
hidden: false

description: The description.

---

MIT License

Copyright (c) [year] [fullname]

"""

license_text_with_more_dashes = """
---
title: SIL Open Font License 1.1
description: The description.

---

Copyright (c) [year] [fullname] ([email])

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:
http://scripts.sil.org/OFL

-----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
-----------------------------------------------------------

"""


class TestLicense(unittest.TestCase):
    def setUp(self):
        self.license = License(faker.file_path(depth=5, extension="txt"))

    def test_license_get_id_file_name_and_directory(self):
        head, tail = os.path.split(self.license.path)

        self.assertEqual(tail.replace(".txt", ""), self.license.id)
        self.assertEqual(tail, self.license.file_name)
        self.assertEqual(head, self.license.directory)

    @patch("builtins.open", new_callable=mock_open, read_data=license_text)
    def test_license_calls_open_file_read_only(self, open_mock):
        self.license.load()

        open_mock.assert_called_with(self.license.path, "r")

    @patch("builtins.open", new_callable=mock_open, read_data=license_text)
    def test_license_get_text_from_file(self, open_mock):
        self.license.load()

        self.assertEqual(
            self.license.text, "MIT License\n\nCopyright (c) [year] [fullname]"
        )

    @patch("builtins.open", new_callable=mock_open, read_data=license_text)
    def test_license_get_yaml_data_from_file(self, open_mock):
        self.license.load()

        self.assertEqual(self.license.name, "MIT License")
        self.assertEqual(self.license.description, "The description.")

    @patch(
        "builtins.open", new_callable=mock_open, read_data=license_text_with_more_dashes
    )
    def test_license_get_yaml_data_from_file_with_multiple_dashes(self, open_mock):
        self.license.load()

        self.assertEqual(self.license.name, "SIL Open Font License 1.1")
        self.assertEqual(self.license.description, "The description.")

    @patch("licensegh.licensegh.Console")
    def test_print_license_text(self, console_class_mock):
        self.license.text = faker.text()

        console_mock = MagicMock()
        console_class_mock.return_value = console_mock

        self.license.print()

        console_mock.print.called_once_with(self.license.text)


class TestLicensegh(unittest.TestCase):
    def setUp(self):
        self.licensegh = Licensegh()
        self.licensegh.repository = MagicMock()

    def test_version(self):
        self.assertEqual(__version__, "0.1.0")

    def test_it_starts_templates_repository(self):
        self.licensegh.repository.licenses_path = faker.file_path()

        self.licensegh.init()

        self.licensegh.repository.init.assert_called_once()

    @patch("licensegh.licensegh.os.walk")
    def test_it_loads_all_template_list_when_init(self, walk_mock):
        walk_mock.return_value = [
            ("/foo", ["bar"], ["baz.txt"]),
            ("/foo/bar", [], ["spam.txt", "eggs.txt"]),
        ]
        self.licensegh.repository.licenses_path = faker.file_path()

        self.licensegh.init()

        walk_mock.assert_called_once_with(self.licensegh.repository.licenses_path)
        self.assertListEqual(
            self.licensegh.licenses,
            [
                License("/foo/baz.txt"),
                License("/foo/bar/eggs.txt"),
                License("/foo/bar/spam.txt"),
            ],
        )

    def test_print_licenses_by_id(self):
        license1 = License("/foo/bar/spam.txt")
        license2 = License("/foo/bar/spam-2.0.txt")

        self.licensegh.licenses = [
            License("/foo/bar/baz.txt"),
            License("/foo/bar/eggs.txt"),
            license1,
            license2,
        ]

        self.licensegh.print_licenses = MagicMock()

        self.licensegh.print_licenses_by_id("spam")

        self.licensegh.print_licenses.assert_called_once_with(
            [license1, license2],
            True,
        )

    def test_print_license_by_id(self):
        license1 = MagicMock()
        license1.id = "spam"

        self.licensegh.licenses = [
            License("/foo/bar/baz.txt"),
            License("/foo/bar/eggs.txt"),
            license1,
            License("/foo/bar/spam-2.0.txt"),
        ]

        self.licensegh.print_license_by_id("spam")

        license1.load.assert_called_once()
        license1.print.assert_called_once()

    @patch("licensegh.licensegh.Console")
    def test_print_license_not_found(self, console_class_mock):
        self.licensegh.licenses = []

        console_mock = MagicMock()
        console_class_mock.return_value = console_mock

        self.licensegh.print_license_by_id(faker.word())

        console_mock.print.called_once_with("[red]License not found[red]")

    def test_print_all_licenses(self):
        self.licensegh.licenses = MagicMock()
        self.licensegh.print_licenses = MagicMock()

        self.licensegh.print_all_licenses()

        self.licensegh.print_licenses.assert_called_once_with(self.licensegh.licenses)

    @patch("licensegh.licensegh.Console")
    @patch("licensegh.licensegh.Table")
    def test_it_prints_table(self, table_class_mock, console_class_mock):
        table_mock = MagicMock()
        table_class_mock.return_value = table_mock

        license1 = MagicMock()
        license1.id = faker.word()
        license1.name = faker.name()

        license2 = MagicMock()
        license2.id = faker.word()
        license2.name = faker.name()

        licenses = [license1, license2]

        self.licensegh.print_licenses(licenses)

        expected = [call(license1.id, license1.name), call(license2.id, license2.name)]
        self.assertEqual(table_mock.add_row.call_args_list, expected)

    @patch("licensegh.licensegh.Console")
    @patch("licensegh.licensegh.Table")
    def test_it_prints_table_with_description(
        self, table_class_mock, console_class_mock
    ):
        table_mock = MagicMock()
        table_class_mock.return_value = table_mock

        license = MagicMock()
        license.id = faker.word()
        license.name = faker.name()
        license.description = faker.sentence()

        licenses = [license]

        self.licensegh.print_licenses(licenses, True)

        table_mock.add_row.assert_called_once_with(
            license.id, "{}\n[white]{}[white]".format(license.name, license.description)
        )


class TestTemplateRepository(unittest.TestCase):
    def setUp(self):
        self.path = os.path.expanduser("~/.licensegh/choosealicense")
        self.licenses_path = os.path.join(self.path, "_licenses")
        self.remote = "https://github.com/github/choosealicense.com.git"
        self.templates_repository = TemplatesRepository()

    def test_repository_attributes(self):
        self.assertEqual(self.templates_repository.remote, self.remote)
        self.assertEqual(self.templates_repository.path, self.path)
        self.assertEqual(self.templates_repository.licenses_path, self.licenses_path)

    @patch("licensegh.licensegh.git")
    @patch("licensegh.licensegh.os")
    def test_repository_clone_if_does_not_exist(self, os_mock, git_mock):
        os_mock.path.isdir = MagicMock(return_value=False)

        self.templates_repository.init()

        git_mock.Repo.clone_from.assert_called_with(self.remote, self.path)

    @patch("licensegh.licensegh.git")
    @patch("licensegh.licensegh.os")
    def test_repository_does_not_clone_if_does_exist(self, os_mock, git_mock):
        os_mock.path.isdir = MagicMock(return_value=True)

        self.templates_repository.init()

        git_mock.Repo.clone_from.assert_not_called()

    @patch("licensegh.licensegh.git")
    @patch("licensegh.licensegh.os")
    def test_repository_does_pull_if_exists(self, os_mock, git_mock):
        os_mock.path.isdir = MagicMock(return_value=True)
        repo_mock = MagicMock()
        git_mock.Repo = MagicMock(return_value=repo_mock)

        self.templates_repository.init()

        repo_mock.remotes.origin.pull.assert_called()
