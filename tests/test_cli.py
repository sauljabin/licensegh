import unittest
from unittest.mock import MagicMock

from licensegh.cli import Cli


class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.licensegh = MagicMock()

    def test_cli_call_licensegh_init(self):
        self.cli.run(False, False, False, None)

        self.cli.licensegh.init.assert_called_once()
