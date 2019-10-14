#!/bin/env python

#################################################################
# This is an example script for showing how to use this library #
# Documentation is available at:                                #
# https://doc.elabftw.net/api.html                              #
# Licence: GNU GPLv3                                            #
# © Nicolas CARPi 2019                                          #
#################################################################

# to get the date of today
import datetime
# to display the results
import json

import elabapy


## CONFIG ##
# get your API key from your profile
API_KEY = "651cf...39be3"
ENDPOINT = "https://elabftw.example.com/api/v1/"
## END CONFIG ##


# get today's date
today = datetime.date.today()
today_date = today.strftime("%Y%m%d")

def someFunctionThatGetsDataFromSomething():
    """ This function fetches metadata from some source """
    return "Updated from API", "This is my data"

# first create the "elab" object with the token and endpoint URL
elab = elabapy.manager(token=API_KEY, endpoint=ENDPOINT)

# create an experiment
new = elab.create_experiment()
exp_id = new["id"]
print(f"New experiment created with id: {exp_id}")

# the newly created experiment is empty
my_exp = elab.get_experiment(exp_id)
print(json.dumps(my_exp, indent=4, sort_keys=True))

# let's modify it
title, body = someFunctionThatGetsDataFromSomething()
params = {"title": title, "date": today_date, "body": body}
out = elab.post_experiment(exp_id, params)
print(f"Updating experiment with id {exp_id}: {out['result']}")

# now let's create an item
# first we need to know what are the available ids to us for the item type (as these are dynamic)
items_types = elab.get_items_types()
print(json.dumps(items_types, indent=4))
print(items_types[0]["category_id"])

# create item
# the parameter here is the id of an item_type!
# for this script I'm simply using the first result of the previous query
# but you'll want to use the same "category_id" probably
my_item = elab.create_item(items_types[0]["category_id"])
item_id = my_item["id"]
print(f"New item created with id: {item_id}")

# now update it
out = elab.post_item(item_id, params)

# attach a file to it
my_file = {"file": open("example-script.py", "rb")}
elab.upload_to_item(item_id, my_file)

# now link our experiment to that database item
params = {"link": item_id}
elab.add_link_to_experiment(exp_id, params)

# and add a tag to our experiment
params = {"tag": "automated entry"}
elab.add_tag_to_experiment(exp_id, params)
