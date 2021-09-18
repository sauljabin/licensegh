import unittest
from unittest.mock import MagicMock

from faker import Faker

from licensegh.cli import Cli

faker = Faker()


class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.licensegh = MagicMock()

    def test_cli_call_licensegh_init(self):
        self.cli.run(False, False, False, None)

        self.cli.licensegh.init.assert_called_once()

    def test_cli_print_all_licenses(self):
        self.cli.run(False, False, True, None)

        self.cli.licensegh.print_all_licenses.assert_called_once()

    def test_cli_print_license_by_id(self):
        license_id = faker.word()
        self.cli.run(False, True, False, license_id)

        self.cli.licensegh.print_licenses_by_id.assert_called_once_with(license_id)
