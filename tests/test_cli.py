import unittest
from unittest.mock import MagicMock, patch

from faker import Faker

from licensegh.cli import Cli

faker = Faker()


class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.licensegh = MagicMock()

    @patch("licensegh.cli.click")
    def test_cli_call_licensegh_init(self, click_mock):
        self.cli.run(False, False, False, False, None)

        self.cli.licensegh.init.assert_called_once()

    def test_cli_print_all_licenses(self):
        self.cli.run(False, False, True, False, None)

        self.cli.licensegh.print_all_licenses.assert_called_once()

    def test_cli_print_licenses_by_id(self):
        license_id = faker.word()
        self.cli.run(False, True, False, False, license_id)

        self.cli.licensegh.print_licenses_by_id.assert_called_once_with(license_id)

    def test_cli_print_license_by_id(self):
        license_id = faker.word()
        self.cli.run(True, False, False, False, license_id)

        self.cli.licensegh.print_license_by_id.assert_called_once_with(license_id)

    def test_save_license_by_id(self):
        license_id = faker.word()
        self.cli.run(False, False, False, False, license_id)

        self.cli.licensegh.save_license_by_id.assert_called_once_with(license_id)

    @patch("licensegh.cli.click")
    def test_cli_shows_help_when_license_id_does_not_exists(self, click_mock):
        self.cli.run(False, False, False, False, None)

        self.cli.licensegh.save_license_by_id.assert_not_called()
        click_mock.get_current_context.assert_called_once()
        click_mock.echo.assert_called_once()

    def test_reset_repository(self):
        self.cli.run(False, False, False, True, None)

        self.cli.licensegh.reset_repository.assert_called_once()
        self.cli.licensegh.init.assert_not_called()
