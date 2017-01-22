# elabapy

This library provides easy access to eLabFTW's API to list or update experiments or items.

## How to install

You can install elabapy using **pip**

    pip install -U elabapy

or via sources:

    python setup.py install

## Features

elabapy support all the features provided via
eLabFTW API, such as:

-  Get user's Experiments/Items
-  Update an Experiment/Item
-  Upload a file to an Experiment/Item

## Examples

### Initialization

```python
    import elabapy
    import json
    # get your token from your profile page
    manager = elabapy.Manager(token="def502005a0f...", endpoint="https://elab.example.org/api/v1/")
```

### Listing the experiments

This example shows how to list all the experiments:

```python
    experiments = manager.get_all_experiments()
```

### Get info for an experiment

This example shows how to print data from experiment with ID 1:

```python
    # get data for experiment 1
    exp = manager.get_experiment(1)
    # show the title
    print(exp["title"])
    # pretty print everything
    print(json.dumps(exp, indent=4, sort_keys=True))
```

### Links

-  GitHub: https://github.com/elabftw/elabapy
-  PyPI page: https://pypi.python.org/pypi/elabapy
-  Website: https://www.elabftw.net
