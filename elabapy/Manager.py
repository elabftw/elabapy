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

    def create_experiment(self):
        """
            Create an experiment
        """
        return self.post_data("experiments", params={})

    def create_item(self, id):
        """
            Create an item, the id is the items_types id
        """
        return self.post_data("items/" + str(id), params={})

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

    def get_items_types(self):
        """
            Get list of items_types
        """
        return self.get_data("items_types/")

    def get_upload(self, id):
        """
            Get an uploaded file from ID
        """
        return self.get_data("uploads/" + str(id))

    def get_status(self):
        """
            Get list of status
        """
        return self.get_data("status/")

    def post_experiment(self, id, params):
        """
            Change an experiment title/body/date
        """
        return self.post_data("experiments/" + str(id), params)

    def post_item(self, id, params):
        """
            Change an item title/body/date
            params must contain title, date and body
        """
        return self.post_data("items/" + str(id), params)

    def add_link_to_experiment(self, id, params):
        """
            Add a link to an experiment
            params must contain "link=<ITEM_ID>"
        """
        return self.post_data("experiments/" + str(id), params)

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

    def add_tag_to_experiment(self, id, params):
        """
            Add a tag to an experiment
        """
        return self.post_data("experiments/" + str(id), params)

    def add_tag_to_item(self, id, params):
        """
            Add a tag to an item
        """
        return self.post_data("items/" + str(id), params)

    def get_backup_zip(self, datespan):
        """ Get the backup zip of modified experiments during datespan """
        return self.get_data("backupzip/" + datespan, 'GET', None, True)

    def __str__(self):
        return "<Manager>"
