#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = """This library provides easy access to eLabFTW's API."""

setup(
    name='elabapy',
    version='0.3.0',
    description='elabftw API to manage experiments and items',
    author='Nicolas CARPi',
    author_email='nicolas.carpi@curie.fr',
    url='https://github.com/elabftw/elabapy',
    packages=['elabapy'],
    install_requires=['requests'],
    test_suite='elabapy.tests',
    license='GPL v3',
    long_description=long_description
)
