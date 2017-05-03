# -*- coding: utf-8 -*-
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

from .baseapi import BaseAPI
from .baseapi import GET

class Manager(BaseAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_all_experiments(self):
        """
            This function returns a list of all experiments.
        """
        return self.get_data("experiments/")

    def get_experiment(self, id):
        """
            This function returns data from an experiment.
        """
        return self.get_data("experiments/" + str(id))

    def get_all_items(self):
        """
            Return all items
        """
        return self.get_data("items/")

    def get_item(self, id):
        """
            Get data from an item
        """
        return self.get_data("items/" + str(id))

    def post_experiment(self, id, params):
        """
            Change an experiment title/body/date
        """
        return self.post_data("experiments/" + str(id), params)

    def post_item(self, id, params):
        """
            Change an item title/body/date
        """
        return self.post_data("items/" + str(id), params)

    def upload_to_experiment(self, id, params):
        """
            Upload a file to an experiment
        """
        return self.post_file("experiments/" + str(id), params)

    def upload_to_item(self, id, params):
        """
            Upload a file to an item
        """
        return self.post_file("items/" + str(id), params)

    def __str__(self):
        return "<Manager>"
