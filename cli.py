"""
This file exposes a command line interface
"""
import click

from app import main


@click.group()
def cli():
    """
    Create cli command group.
    See: https://click.palletsprojects.com/en/8.1.x/quickstart/#nesting-commands

    :return:
    """
    pass


@cli.command()
def hello():
    """
    Greet the user to demonstrate that the cli works

    :return:
    """
    click.echo("Hello world")


@cli.command()
def start():
    """
    Start the app from the command line

    :return:
    """
    main.main()


if __name__ == "__main__":
    cli()
