# elabapy

[![release](https://img.shields.io/pypi/v/elabapy.svg)](https://pypi.org/project/elabapy/)
[![wheel](https://img.shields.io/pypi/wheel/elabapy.svg)](https://pypi.org/project/elabapy/)
[![license](https://img.shields.io/pypi/l/elabapy.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

This Python 3 library provides easy access to [eLabFTW](https://www.elabftw.net)'s [API](https://doc.elabftw.net/api.html) to list or update experiments or items.


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

### Example script

~~~python
import elabapy
import json
from requests.exceptions import HTTPError
# initialize the manager with an endpoint and your token
manager = elabapy.Manager(endpoint="https://elab.example.org/api/v1/", token="3ca8...e14b")
# get experiment with id 42
try:
    exp = manager.get_experiment(42)
    print(json.dumps(exp, indent=4, sort_keys=True))
# if something goes wrong, the corresponding HTTPError will be raised
except HTTPError as e:
    print(e)
~~~

Use `verify=False` in the Manager initialization to disable TLS certificate verification.

## Dev stuff

### Create new release

Version needs to be changed in `setup.py` and `elabapy/__init__.py`.

Edit changelog.

Tag, push, build, upload:

~~~bash
git tag -s $version -m '$version'
git push --tags
rm dist/*
python setup.py sdist bdist_egg bdist_wheel
twine upload dist/*
~~~

Create release on GitHub.
