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

## Update version

Version needs to be changed in `setup.py` and `elabapy/__init__.py`.

## Create new release

~~~bash
git tag -s $version -m '$version'
git push --tags
python setup.py sdist bdist_egg bdist_wheel upload
~~~
