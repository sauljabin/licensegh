import click

from licensegh import __version__
from licensegh.licensegh import Licensegh


class Cli:
    def __init__(self):
        self.licensegh = Licensegh()

    def run(self, print, search, list, license_id):
        self.licensegh.init()

        if list:
            self.licensegh.print_all_licenses()
            return

        if search:
            self.licensegh.print_licenses_by_id(license_id)
            return

        if print:
            self.licensegh.print_license_by_id(license_id)
            return

        if license_id:
            self.licensegh.save_license_by_id(license_id)
            return

        with click.get_current_context() as context:
            click.echo(context.get_help())


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--print", "-p", is_flag=True, help="Print the found license file.")
@click.option("--search", "-s", is_flag=True, help="Search licenses and shows a list.")
@click.option("--list", "-l", is_flag=True, help="List all found licenses.")
@click.version_option(__version__)
@click.argument("license_id", metavar="<license id>", nargs=1, required=False)
def main(print, search, list, license_id):
    cli = Cli()
    cli.run(print, search, list, license_id)


if __name__ == "__main__":
    main()
