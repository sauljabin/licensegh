import click

from licensegh import __version__
from licensegh.licensegh import Licensegh


class Cli:
    def __init__(self):
        self.licensegh = Licensegh()

    def run(self, print, search, list, license_id):
        self.licensegh.init()

    def print_license_table(self, licenses_list):
        pass


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--print", "-p", is_flag=True, help="Print the license file")
@click.option("--search", "-s", is_flag=True, help="Search license, shows a list")
@click.option("--list", "-l", is_flag=True, help="List all found licenses")
@click.version_option(__version__)
@click.argument("license_id", metavar="<license id>", nargs=1, required=False)
def main(print, search, list, license_id):
    cli = Cli()
    cli.run(print, search, list, license_id)


if __name__ == "__main__":
    main()
