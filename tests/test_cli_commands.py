"""
Tests to verify that copick-plugin-demo commands are properly registered with the copick CLI.
"""
import subprocess
import sys
from unittest.mock import patch

import pytest
from click.testing import CliRunner
from copick.cli.cli import cli


class TestCopickPluginDemoCommands:
    """Test that all copick-plugin-demo commands are available through the copick CLI."""

    def setup_method(self):
        """Set up test runner."""
        self.runner = CliRunner()

    def test_main_command_mypackage_available(self):
        """Test that 'mypackage' command is available in main copick CLI."""
        result = self.runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "mypackage" in result.output

    def test_inference_command_mymodel_infer_available(self):
        """Test that 'mymodel-infer' command is available in inference group."""
        result = self.runner.invoke(cli, ["inference", "--help"])
        assert result.exit_code == 0
        assert "mymodel-infer" in result.output

    def test_training_command_mymodel_train_available(self):
        """Test that 'mymodel-train' command is available in training group."""
        result = self.runner.invoke(cli, ["training", "--help"])
        assert result.exit_code == 0
        assert "mymodel-train" in result.output

    def test_evaluation_command_myscore_available(self):
        """Test that 'myscore' command is available in evaluation group."""
        result = self.runner.invoke(cli, ["evaluation", "--help"])
        assert result.exit_code == 0
        assert "myscore" in result.output

    def test_process_command_mymethod_available(self):
        """Test that 'mymethod' command is available in process group."""
        result = self.runner.invoke(cli, ["process", "--help"])
        assert result.exit_code == 0
        assert "mymethod" in result.output

    def test_convert_command_myconverter_available(self):
        """Test that 'myconverter' command is available in convert group."""
        result = self.runner.invoke(cli, ["convert", "--help"])
        assert result.exit_code == 0
        assert "myconverter" in result.output

    def test_mypackage_command_execution(self):
        """Test that 'mypackage' command can be executed with help."""
        result = self.runner.invoke(cli, ["mypackage", "--help"])
        assert result.exit_code == 0
        assert "A command that serves as an example" in result.output

    def test_mymodel_infer_command_execution(self):
        """Test that 'mymodel-infer' command can be executed with help."""
        result = self.runner.invoke(cli, ["inference", "mymodel-infer", "--help"])
        assert result.exit_code == 0
        assert "A command that serves as an example for how to implement an inference CLI" in result.output

    def test_mymodel_train_command_execution(self):
        """Test that 'mymodel-train' command can be executed with help."""
        result = self.runner.invoke(cli, ["training", "mymodel-train", "--help"])
        assert result.exit_code == 0
        assert "A command that serves as an example for how to implement a training CLI" in result.output

    def test_myscore_command_execution(self):
        """Test that 'myscore' command can be executed with help."""
        result = self.runner.invoke(cli, ["evaluation", "myscore", "--help"])
        assert result.exit_code == 0
        assert "A command that serves as an example for how to implement an evaluation CLI" in result.output

    def test_mymethod_command_execution(self):
        """Test that 'mymethod' command can be executed with help."""
        result = self.runner.invoke(cli, ["process", "mymethod", "--help"])
        assert result.exit_code == 0
        assert "A command that serves as an example for how to implement a process CLI command" in result.output

    def test_myconverter_command_execution(self):
        """Test that 'myconverter' command can be executed with help."""
        result = self.runner.invoke(cli, ["convert", "myconverter", "--help"])
        assert result.exit_code == 0
        assert "A command that serves as an example for how to implement a convert CLI command" in result.output

    @patch("copick_plugin_demo.cli.cli.get_logger")
    def test_mypackage_command_with_options(self, mock_logger):
        """Test that 'mypackage' command can be executed with options."""
        mock_logger.return_value.info = lambda x: None

        # Test command with options
        result = self.runner.invoke(cli, ["mypackage", "--config", "/tmp/test-config.json", "--option", "test"])
        assert result.exit_code == 0

    @patch("copick_plugin_demo.cli.cli.get_logger")
    def test_mymodel_infer_command_with_options(self, mock_logger):
        """Test that 'mymodel-infer' command can be executed with options."""
        mock_logger.return_value.info = lambda x: None

        # Test command with options
        result = self.runner.invoke(
            cli,
            ["inference", "mymodel-infer", "--config", "/tmp/test-config.json", "--option", "test"],
        )
        assert result.exit_code == 0


class TestCopickPluginDemoCommandsIntegration:
    """Integration tests that verify commands work through actual CLI invocation."""

    def test_copick_cli_contains_plugin_commands(self):
        """Test that running 'copick --help' shows plugin commands."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "copick.cli.cli", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "mypackage" in result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Could not run copick CLI - may not be installed or accessible")

    def test_copick_inference_contains_plugin_commands(self):
        """Test that running 'copick inference --help' shows plugin commands."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "copick.cli.cli", "inference", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "mymodel-infer" in result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Could not run copick CLI - may not be installed or accessible")

    def test_copick_training_contains_plugin_commands(self):
        """Test that running 'copick training --help' shows plugin commands."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "copick.cli.cli", "training", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "mymodel-train" in result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Could not run copick CLI - may not be installed or accessible")

    def test_copick_evaluation_contains_plugin_commands(self):
        """Test that running 'copick evaluation --help' shows plugin commands."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "copick.cli.cli", "evaluation", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "myscore" in result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Could not run copick CLI - may not be installed or accessible")

    def test_copick_process_contains_plugin_commands(self):
        """Test that running 'copick process --help' shows plugin commands."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "copick.cli.cli", "process", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "mymethod" in result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Could not run copick CLI - may not be installed or accessible")

    def test_copick_convert_contains_plugin_commands(self):
        """Test that running 'copick convert --help' shows plugin commands."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "copick.cli.cli", "convert", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "myconverter" in result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Could not run copick CLI - may not be installed or accessible")
