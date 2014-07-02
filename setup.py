# pylint: disable=all

from setuptools import setup, find_packages
from version import get_git_version
from subprocess import check_output


setup(
    name="nist_lookup",
    version=get_git_version(),
    packages=find_packages(exclude='test'),
    scripts=[
        "bin/delta_beta_table.py",
    ],

    install_requires=[
        'scipy',
        'beautifulsoup4',
    ],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author="TOMCAT DPC group",
    author_email="",
    description="Download table from the NIST database",
    license="GNU GPL 3",
    keywords="",
    # project home page, if any
    url="https://bitbucket.org/psitomcat/nist_lookup",
    # could also include long_description, download_url, classifiers, etc.
)
