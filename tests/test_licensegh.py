import unittest
from unittest.mock import MagicMock, patch

from licensegh import __version__
from licensegh.licensegh import TemplatesRepository


class TestLicenseGH(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.path = "~/licensegh/choosealicense"
        self.licenses_path = "~/licensegh/choosealicense/_licenses"
        self.remote = "https://github.com/github/choosealicense.com.git"

    def test_repository_attributes(self):
        repo = TemplatesRepository()
        self.assertEqual(repo.remote, self.remote)
        self.assertEqual(repo.path, self.path)
        self.assertEqual(repo.licenses_path, self.licenses_path)

    @patch("licensegh.licensegh.git")
    @patch("licensegh.licensegh.os")
    def test_repository_clone_if_does_not_exist(self, os_mock, git_mock):
        template_repo = TemplatesRepository()
        os_mock.path.isdir = MagicMock(return_value=False)

        template_repo.init()

        git_mock.Repo.clone_from.assert_called_with(self.remote, self.path)

    @patch("licensegh.licensegh.git")
    @patch("licensegh.licensegh.os")
    def test_repository_does_not_clone_if_does_exist(self, os_mock, git_mock):
        template_repo = TemplatesRepository()
        os_mock.path.isdir = MagicMock(return_value=True)

        template_repo.init()

        git_mock.Repo.clone_from.assert_not_called()

    @patch("licensegh.licensegh.git")
    @patch("licensegh.licensegh.os")
    def test_repository_does_pull_if_exists(self, os_mock, git_mock):
        template_repo = TemplatesRepository()
        os_mock.path.isdir = MagicMock(return_value=True)
        repo_mock = MagicMock()
        git_mock.Repo = MagicMock(return_value=repo_mock)

        template_repo.init()

        repo_mock.remotes.origin.pull.assert_called()
