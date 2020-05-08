# elabapy

[![release](https://img.shields.io/pypi/v/elabapy.svg)](https://pypi.org/project/elabapy/)
[![wheel](https://img.shields.io/pypi/wheel/elabapy.svg)](https://pypi.org/project/elabapy/)
[![license](https://img.shields.io/pypi/l/elabapy.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

This Python 3 library provides easy access to [eLabFTW](https://www.elabftw.net)'s API to list or update experiments or items.


## How to install

You can install elabapy using **pip**

    pip install -U elabapy

or via sources:

    python setup.py install

## How to use

### [Read the docs](https://doc.elabftw.net/api.html)

## Links

- Documentation: https://doc.elabftw.net/api.html
- PyPI page: https://pypi.org/project/elabapy/

## Dev stuff

### Update version

Version needs to be changed in `setup.py` and `elabapy/__init__.py`.

### Check typing

~~~bash
# mypy type hinting check
pipenv run python -m mypy elabapy
~~~

## Create new release

Edit changelog.

Tag, push, build, upload:

~~~bash
git tag -s $version -m '$version'
git push --tags
python setup.py sdist bdist_egg bdist_wheel
twine upload dist/*
~~~
