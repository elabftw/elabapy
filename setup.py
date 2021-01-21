#!/usr/bin/env python
from setuptools import setup

long_description = """This library provides easy access to eLabFTW's API."""

setup(
    name='elabapy',
    version='0.7.0',
    description='elabftw API to manage experiments and items',
    author='Nicolas CARPi',
    author_email='nico-git@deltablot.email',
    url='https://github.com/elabftw/elabapy',
    packages=['elabapy'],
    install_requires=['requests'],
    test_suite='elabapy.tests',
    license='GPL v3',
    long_description=long_description
)
