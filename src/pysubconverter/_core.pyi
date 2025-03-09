"""

Pybind11 _core plugin
-----------------------
.. currentmodule:: _core

"""

from __future__ import annotations

__all__ = [
    "flush_cache",
    "get",
    "get_local",
    "get_profile",
    "get_ruleset",
    "init_config",
    "render",
    "sub_to_clashr",
    "subconverter",
    "surge_to_clashr",
    "update_config",
    "version",
]

def flush_cache() -> None:
    """
    flush the cache.
    """

def get(arguments: dict[str, str]) -> str:
    """
    get from the url.
    """

def get_local(arguments: dict[str, str]) -> str:
    """
    get from the local file.
    """

def get_profile(arguments: dict[str, str]) -> str:
    """
    get the profile from subconverter.
    """

def get_ruleset(arguments: dict[str, str]) -> str:
    """
    get the ruleset from subconverter.
    """

def init_config(dir: str) -> None:
    """
    initialize the configuration directory from subconverter.
    """

def render(arguments: dict[str, str]) -> str:
    """
    render the subscription.
    """

def sub_to_clashr(arguments: dict[str, str]) -> str:
    """
    convert subscription to clashroyale format

    Args:
        arguments (dict): subscription conversion arguments.
    Returns:
        str: converted clashroyale subscription.
    """

def subconverter(arguments: dict[str, str]) -> str:
    """
    convert to subscription format

    Args:
        arguments (dict): subscription conversion arguments.
    Returns:
        str: converted subscription.
    """

def surge_to_clashr(arguments: dict[str, str]) -> str:
    """
    convert surge to clashroyale format

    Args:
        arguments (dict): surge conversion arguments.
    Returns:
        str: converted clashroyale subscription.
    """

def update_config(arguments: dict[str, str]) -> None:
    """
    update the configuration from subconverter.
    """

def version() -> str:
    """
    The _core plugin version.
    """
