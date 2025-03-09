"""
Copyright (c) 2025 l.feng. All rights reserved.

pysubconverter: A wrapper from subconverter
"""

from __future__ import annotations

import shutil
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator

from appdirs import user_cache_dir
from filelock import FileLock
from importlib_metadata import distribution

from pysubconverter._core import (
    flush_cache,
    get,
    get_local,
    get_profile,
    get_ruleset,
    init_config,
    render,
    settings,
    sub_to_clashr,
    subconverter,
    surge_to_clashr,
    update_config,
)

from ._version import version as __version__

__all__ = [
    "__version__",
    "flush_cache",
    "get",
    "get_local",
    "get_profile",
    "get_ruleset",
    "init_config",
    "render",
    "settings",
    "sub_to_clashr",
    "subconverter",
    "surge_to_clashr",
    "update_config",
]


def default_cache_dir() -> str:
    """
    Get the default cache directory for pysubconverter.
    """
    return str(user_cache_dir("pysubconverter"))


@contextmanager
def config_context(
    cache_dir: str = default_cache_dir(),
    renew: bool = False,
) -> Generator[None, Any, None]:
    """
    A context manager to initialize and configure the config directory.
    """
    config_lock = FileLock(Path(cache_dir) / "config.lock")
    config_dir = Path(cache_dir) / "config"
    with config_lock:
        pkg_config = distribution(__package__).locate_file(__package__) / "config"
        if not config_dir.exists():
            shutil.copytree(str(pkg_config), config_dir)

        if renew:
            shutil.rmtree(config_dir)
            shutil.copytree(str(pkg_config), config_dir)

        init_config(str(config_dir))
        try:
            yield
        finally:
            pass
