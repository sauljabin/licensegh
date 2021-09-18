import os
import unittest
from unittest.mock import MagicMock, patch

from faker import Faker

from licensegh import __version__
from licensegh.licensegh import Licence, Licensegh, TemplatesRepository

faker = Faker()


class TestLicense(unittest.TestCase):
    def setUp(self):
        self.license = Licence(faker.file_path(depth=5, extension="txt"))

    def test_license_get_id_file_name_and_directory(self):
        head, tail = os.path.split(self.license.path)

        self.assertEqual(tail.replace(".txt", ""), self.license.id)
        self.assertEqual(tail, self.license.file_name)
        self.assertEqual(head, self.license.directory)


class TestLicensegh(unittest.TestCase):
    def setUp(self):
        self.licensegh = Licensegh()
        self.licensegh.repository = MagicMock()

    def test_version(self):
        self.assertEqual(__version__, "0.1.0")

    def test_it_starts_templates_repository(self):
        self.licensegh.init()

        self.licensegh.repository.init.assert_called_once()

    def test_it_loads_all_template_list_when_init(self):
        self.licensegh.init()


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
