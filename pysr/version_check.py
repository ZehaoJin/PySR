"""Code for checking whether the PySR version is up-to-date"""
import subprocess
import sys
from typing import List


def run_pip_command(*commands: List[str]):
    """Run a pip command and return the output

    Parameters
    ----------
    commands : list[str]
        List of commands to run. For example,
        `["install", "pysr"]` will run `pip install pysr`.

    Returns
    -------
    output : str
        Output of the command.
    """
    raw_output = subprocess.run(
        [sys.executable, "-m", "pip", *commands],
        capture_output=True,
        text=True,
    )
    return str(raw_output)


def is_up_to_date(name: str):
    """Checks if a particular Python package is up-to-date.

    Credit to
    https://stackoverflow.com/questions/58648739/how-to-check-if-python-package-is-latest-version-programmatically

    Parameters
    ----------
    name : str
        Name of the package to check.

    Returns
    -------
    flag : bool
        True if the package is up-to-date, False otherwise.
    """

    latest_version = run_pip_command("install", f"{name}==random")
    latest_version = latest_version[latest_version.find("(from versions:") + 15 :]
    latest_version = latest_version[: latest_version.find(")")]
    latest_version = latest_version.replace(" ", "").split(",")[-1]

    current_version = run_pip_command("show", name)
    current_version = current_version[current_version.find("Version:") + 8 :]
    current_version = current_version[: current_version.find("\\n")].replace(" ", "")

    if latest_version == current_version:
        return True
    else:
        return False


def is_pysr_up_to_date():
    """Checks if PySR is up-to-date"""
    return is_up_to_date("pysr")
