# elabapy

[![release](https://img.shields.io/pypi/v/elabapy.svg)](https://pypi.org/project/elabapy/)
[![wheel](https://img.shields.io/pypi/wheel/elabapy.svg)](https://pypi.org/project/elabapy/)
[![license](https://img.shields.io/pypi/l/elabapy.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

This Python 3 library provides easy access to [eLabFTW](https://www.elabftw.net)'s API to list or update experiments or items.


## Install

You can install elabapy using **pip**

~~~bash
pip install --user elabapy
~~~

or via **conda**:

~~~bash
conda skeleton pypi elabapy
conda-build elabapy
~~~

or via sources:

~~~bash
git clone https://github.com/elabftw/elabapy
cd elabapy
python setup.py install
~~~

## Update

    pip install -U elabapy

## Use

### [API page on eLabFTW's documentation](https://doc.elabftw.net/api.html)
### [Full API doc with examples](https://doc.elabftw.net/api/)

## Links

- Documentation: https://doc.elabftw.net/api.html
- PyPI page: https://pypi.org/project/elabapy/

## Dev stuff

### Create new release

Version needs to be changed in `setup.py` and `elabapy/__init__.py`.

Edit changelog.

Tag, push, build, upload:

~~~bash
git tag -s $version -m '$version'
git push --tags
python setup.py sdist bdist_egg bdist_wheel
twine upload dist/*
~~~
