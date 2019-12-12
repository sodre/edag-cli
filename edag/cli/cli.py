"""Console script for edag-cli."""
import sys
import click
from click_plugins import with_plugins
from entrypoints import get_group_named


@with_plugins(get_group_named("edag.cli"))
@click.group()
def main(args=None):
    """edag command-line-interface"""
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
