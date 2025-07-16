# copick-plugin-demo

A demonstration package showing how to create plugins for the [copick](https://github.com/copick/copick) CLI. This package serves as a template and reference for developers who want to extend copick with custom commands.

## What is copick?

**copick** is a cross-platform, storage-agnostic and server-less dataset API for cryoET datasets. It provides a unified interface for accessing and managing cryo-electron tomography data across different storage systems.

## Plugin System Overview

The copick CLI supports a plugin system that allows external Python packages to register additional commands. Commands can be added to the main CLI or organized into specialized groups:

- **`copick.commands`**: Commands added directly to the main CLI (e.g., `copick mycommand`)
- **`copick.inference.commands`**: Commands under the inference group (e.g., `copick inference mymodel`)
- **`copick.training.commands`**: Commands under the training group (e.g., `copick training mytrain`)
- **`copick.evaluation.commands`**: Commands under the evaluation group (e.g., `copick evaluation myscore`)
- **`copick.process.commands`**: Commands under the process group (e.g., `copick process mymethod`)
- **`copick.convert.commands`**: Commands under the convert group (e.g., `copick convert myconverter`)

## Demo Package Structure

This demo package demonstrates all supported entry point groups:

```
copick-plugin-demo/
├── src/
│   └── copick_plugin_demo/
│       ├── __init__.py
│       └── cli/
│           ├── __init__.py
│           └── cli.py          # All demo commands
├── pyproject.toml              # Entry point configuration
└── README.md
```

## Entry Points Configuration

The `pyproject.toml` file shows how to register commands for each supported group:

```toml
# Commands added to main CLI group
[project.entry-points."copick.commands"]
mypackage = "copick_plugin_demo.cli.cli:mypackage"

# Commands added to inference group
[project.entry-points."copick.inference.commands"]
mymodel-infer = "copick_plugin_demo.cli.cli:mymodel_infer"

# Commands added to training group
[project.entry-points."copick.training.commands"]
mymodel-train = "copick_plugin_demo.cli.cli:mymodel_train"

# Commands added to evaluation group
[project.entry-points."copick.evaluation.commands"]
myscore = "copick_plugin_demo.cli.cli:myscore"

# Commands added to process group
[project.entry-points."copick.process.commands"]
mymethod = "copick_plugin_demo.cli.cli:mymethod"

# Commands added to convert group
[project.entry-points."copick.convert.commands"]
myconverter = "copick_plugin_demo.cli.cli:myconverter"
```

## Command Implementation

Each command demonstrates proper implementation patterns:

```python
import click
from copick.cli.util import add_config_option, add_debug_option
from copick.util.log import get_logger

@click.command(short_help="A command added to the main copick CLI.")
@add_config_option
@click.option("--option", "-o", type=str, default=None, help="An example option.")
@add_debug_option
@click.pass_context
def mypackage(ctx: click.Context, config: str, option: str, debug: bool):
    """A command that serves as an example for how to implement a CLI command in copick."""
    logger = get_logger(__name__, debug=debug)
    logger.info(f"Running mypackage with config: {config}, option: {option}")
    # Add your command logic here
```

## Installation and Usage

1. **Install the demo package**:
   ```bash
   pip install copick-plugin-demo
   ```

2. **Use the commands**:
   ```bash
   # Main CLI command
   copick mypackage --config config.json --option example

   # Grouped commands
   copick inference mymodel-infer --config config.json --option example
   copick training mymodel-train --config config.json --option example
   copick evaluation myscore --config config.json --option example
   copick process mymethod --config config.json --option example
   copick convert myconverter --config config.json --option example
   ```

## Creating Your Own Plugin

To create your own copick plugin:

1. **Use this package as a template** - copy the structure and modify the commands
2. **Update the entry points** in your `pyproject.toml` to match your package and command names
3. **Implement your commands** following the patterns shown in `cli.py`
4. **Always use the required decorators**:
   - `@add_config_option` - provides the `--config` option
   - `@add_debug_option` - provides the `--debug` option
   - `@click.pass_context` - passes the click context
5. **Use the copick logger** for consistent logging across the ecosystem

## Best Practices

- Use descriptive command names that clearly indicate their purpose
- Follow existing naming conventions with hyphens for multi-word commands
- Always use `@add_config_option` and `@add_debug_option` decorators for consistency
- Add proper docstrings for your commands - they become the help text
- Use appropriate entry point groups to organize your commands logically
- Test your plugins thoroughly before releasing

## Documentation

For detailed documentation on copick and the plugin system, see:
- [Copick Documentation](https://copick.github.io/copick/)
- [CLI Plugin System Guide](https://copick.github.io/copick/cli/#plugin-system)
- [Contributing Guide](https://copick.github.io/copick/contributing/#plugin-development)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
