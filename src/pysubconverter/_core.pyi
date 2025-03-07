"""

Pybind11 _core plugin
-----------------------
.. currentmodule:: _core

"""

from __future__ import annotations

__all__ = ["init_config", "subconverter", "version"]

def init_config(dir: str) -> None:
    """
    initialize the configuration directory from subconverter.
    """

def subconverter(arguments: dict[str, str]) -> str:
    """
    convert to subscription format

    Args:
        arguments (dict): subscription conversion arguments.
    Returns:
        str: converted subscription.
    """

def version() -> str:
    """
    The _core plugin version.
    """
