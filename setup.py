#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages
import versioneer

with open("README.rst") as readme_file:
    readme = readme_file.read()

# The requirements section should be kept in sync with the environment.yml file
requirements = [
    "click>=7.0",
    "click-plugins",
    "entrypoints",
]

setup_requirements = [
    "pytest-runner",
    "wheel",
]

test_requirements = [
    "pytest>=3",
    "pytest-cov",
]

setup(
    author="Patrick Sodré",
    author_email="sodre@elasticdag.com",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="The EDAG CLI",
    # fmt: off
    entry_points={
        "console_scripts": [
            "edag=edag.cli.cli:main",
        ],
    },
    # fmt: on
    install_requires=requirements,
    license="Proprietary",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="cli edag",
    name="edag-cli",
    packages=find_namespace_packages(include=["edag.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/sodre/cli",
    zip_safe=False,
)
