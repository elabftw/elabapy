# elabapy

This library provides easy access to eLabFTW's API to list or update experiments or items.

## How to install

You can install elabapy using **pip**

    pip install -U elabapy

or via sources:

    python setup.py install

## How to use

### [Read the docs](https://elabftw.readthedocs.io/en/latest/api.html)

## Links

- Documentation: https://elabftw.readthedocs.io/en/latest/api.html
- PyPI page: https://pypi.python.org/pypi/elabapy

## Update version

Version needs to be changed in `setup.py` and `elabapy/__init__.py`.

## Create new release

~~~bash
git tag -s $version -m '$version'
git push --tags
python setup.py sdist bdist_egg bdist_wheel
~~~

## Update PIP

Go to https://pypi.python.org/pypi?%3Aaction=submit_form and upload the PKG-INFO, then upload the .tar.gz, egg and wheel in `dist/`.
