"""Top-level package for EDAG Command Line Interface."""

__author__ = """Patrick Sodré"""
__email__ = "sodre@elasticdag.com"
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
