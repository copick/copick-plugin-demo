import click
from copick.cli.util import add_config_option, add_debug_option
from copick.util.log import get_logger


@click.command(short_help="A command added to the main copick CLI.")
@add_config_option
@click.option("--option", "-o", "option", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def mypackage(ctx: click.Context, config: str, option: str, debug: bool) -> None:
    """
    A command that serves as an example for how to implement a CLI command in copick.
    """
    logger = get_logger(__name__, debug=debug)

    logger.info(f"Running mymodel with config: {config}, option: {option}, debug: {debug}")
    # Add your command logic here


@click.command(short_help="An inference command.")
@add_config_option
@click.option("--option", "-o", "option", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def mymodel_infer(ctx: click.Context, config: str, option: str, debug: bool) -> None:
    """
    A command that serves as an example for how to implement an inference CLI command in copick.
    """
    logger = get_logger(__name__, debug=debug)

    logger.info(f"Running mymodel with config: {config}, option: {option}, debug: {debug}")
    # Add your command logic here


@click.command(short_help="A training command.")
@add_config_option
@click.option("--option", "-o", "option", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def mymodel_train(ctx: click.Context, config: str, option: str, debug: bool) -> None:
    """
    A command that serves as an example for how to implement a training CLI command in copick.
    """
    logger = get_logger(__name__, debug=debug)

    logger.info(f"Running mymodel with config: {config}, option: {option}, debug: {debug}")
    # Add your command logic here


@click.command(short_help="An evaluation command.")
@add_config_option
@click.option("--option", "-o", "option", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def myscore(ctx: click.Context, config: str, option: str, debug: bool) -> None:
    """
    A command that serves as an example for how to implement an evaluation CLI command in copick.
    """
    logger = get_logger(__name__, debug=debug)

    logger.info(f"Running mymodel with config: {config}, option: {option}, debug: {debug}")
    # Add your command logic here


@click.command(short_help="A process command.")
@add_config_option
@click.option("--option", "-o", "option", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def mymethod(ctx: click.Context, config: str, option: str, debug: bool) -> None:
    """
    A command that serves as an example for how to implement a process CLI command in copick.
    """
    logger = get_logger(__name__, debug=debug)

    logger.info(f"Running mymodel with config: {config}, option: {option}, debug: {debug}")
    # Add your command logic here


@click.command(short_help="A convert command.")
@add_config_option
@click.option("--option", "-o", "option", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def myconverter(ctx: click.Context, config: str, option: str, debug: bool) -> None:
    """
    A command that serves as an example for how to implement a convert CLI command in copick.
    """
    logger = get_logger(__name__, debug=debug)

    logger.info(f"Running mymodel with config: {config}, option: {option}, debug: {debug}")
    # Add your command logic here


@click.group()
@click.pass_context
def _cli(ctx: click.Context) -> None:
    """
    The main command group for the standalone copick-plugin-demo CLI.

    This group serves as a container for all subcommands contained in copick-plugin-demo.
    """
    pass


def add_commands(cmd: click.Group) -> click.Group:
    """
    Add commands to the main CLI group.

    This function registers all the commands defined in this module to the main CLI group.
    """
    cmd.add_command(mymodel_train)
    cmd.add_command(mymodel_infer)
    cmd.add_command(myscore)
    cmd.add_command(mymethod)
    cmd.add_command(myconverter)

    return cmd


# CLI group for testing purposes
tests_cli = add_commands(_cli)


# Main entry point for the standalone copick-plugin-demo CLI
def main():
    """
    Main entry point for the copick-plugin-demo CLI.

    This function initializes the CLI and adds all commands to it.
    """
    cli = add_commands(_cli)
    cli(prog_name="copick")


if __name__ == "__main__":
    main()
