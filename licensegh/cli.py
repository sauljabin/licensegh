import click

from licensegh import __version__

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--print", "-p", is_flag=True, help="Print the license file")
@click.option("--search", "-s", is_flag=True, help="Search license, shows a list")
@click.option("--list", "-l", is_flag=True, help="List all found licenses")
@click.version_option(__version__)
@click.argument("id", metavar="<id>", nargs=1, required=False)
def main(id, print, search, list):
    """
    licensegh is a command line tool that generates a license file for a project
    from the github open source lincese templates.

    licensegh <id> generates a LICENSE file using the license id listed in the
    github open source license templates.
    """
    click.echo(f"Generating license for {id}")
    click.echo(f"Printing license: {print}")
    click.echo(f"Searching license: {search}")
    click.echo(f"Listing licenses: {list}")


if __name__ == "__main__":
    main()
