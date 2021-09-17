import unittest

from licensegh import __version__


class TestLicenseGH(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
