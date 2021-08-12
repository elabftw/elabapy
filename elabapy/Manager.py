# -*- coding: utf-8 -*-
from .baseapi import BaseAPI


class Manager(BaseAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_experiment(self):
        """
            Create an experiment
        """
        return self.send_req("experiments", verb='POST')

    def create_item(self, id):
        """
            Create an item, the id is the items_types id
        """
        return self.send_req("items/" + str(id), verb='POST')

    def create_template(self):
        """
            Create a template
        """
        return self.send_req("templates", verb='POST')

    def get_all_experiments(self, params={'limit':15,'offset':0}):
        """
            This function returns a list of all experiments.
            params is a dict with keys 'limit' and/or 'offset'
            param_name has to be 'params' to be in accordance with the current requests documentation (https://2.python-requests.org/en/master/api/#requests.get)
        """
        return self.send_req("experiments/", params, param_name='params')

    def get_experiment(self, id):
        """
            This function returns data from an experiment.
        """
        return self.send_req("experiments/" + str(id))

    def get_all_items(self, params={'limit':15,'offset':0}):
        """
            Return all items
            params is a dict with keys 'limit' and/or 'offset'
            param_name has to be 'params' to be in accordance with the current requests documentation (https://2.python-requests.org/en/master/api/#requests.get)
        """
        return self.send_req("items/" , params, param_name='params')

    def get_item(self, id):
        """
            Get data from an item
        """
        return self.send_req("items/" + str(id))

    def get_items_types(self):
        """
            Get list of items_types
        """
        return self.send_req("items_types/")

    def get_tags(self):
        """
            Get tags from the team
        """
        return self.send_req("tags/")

    def get_upload(self, id):
        """
            Get an uploaded file from ID
        """
        return self.send_req("uploads/" + str(id), verb='GET', binary=True)

    def get_status(self):
        """
            Get list of status
        """
        return self.send_req("status/")

    def get_all_templates(self):
        """
            This function returns a list of all templates.
        """
        return self.send_req("templates/")

    def get_template(self, id):
        """
            This function returns data from a template.
        """
        return self.send_req("templates/" + str(id))

    def post_experiment(self, id, params):
        """
            Change an experiment title/body/date
        """
        return self.send_req("experiments/" + str(id), params, verb='POST')

    def post_item(self, id, params):
        """
            Change an item title/body/date
            params must contain title, date and body
        """
        return self.send_req("items/" + str(id), params, verb='POST')

    def post_template(self, id, params):
        """
            Change a template title/body/metadata
        """
        return self.send_req("templates/" + str(id), params, verb='POST')

    def add_link_to_experiment(self, id, params):
        """
            Add a link to an experiment
            params must contain "link=<ITEM_ID>"
        """
        return self.send_req("experiments/" + str(id), params, verb='POST')

    def add_link_to_item(self, id, params):
        """
            Add a link to a database item
            params must contain "link=<ITEM_ID>"
        """
        return self.send_req("items/" + str(id), params, verb='POST')

    def upload_to_experiment(self, id, params):
        """
            Upload a file to an experiment
        """
        return self.send_req(
            "experiments/" + str(id), params, verb='POST', param_name='files'
        )

    def upload_to_item(self, id, params):
        """
            Upload a file to an item
        """
        return self.send_req(
            "items/" + str(id), params, verb='POST', param_name='files'
        )

    def add_tag_to_experiment(self, id, params):
        """
            Add a tag to an experiment
        """
        return self.send_req("experiments/" + str(id), params, verb='POST')

    def add_tag_to_item(self, id, params):
        """
            Add a tag to an item
        """
        return self.send_req("items/" + str(id), params, verb='POST')

    def get_backup_zip(self, datespan):
        """ Get the backup zip of modified experiments during datespan """
        return self.send_req("backupzip/" + datespan, verb='GET', binary=True)

    def get_bookable(self):
        """ Get list of bookable items """
        return self.send_req("bookable")

    def create_event(self, id, params):
        """ Create an event in the scheduler for a bookable item """
        return self.send_req("events/" + str(id), params, verb='POST')

    def get_event(self, id):
        """ Get info about an event """
        return self.send_req("events/" + str(id))

    def get_all_events(self):
        """ Get info about all events """
        return self.send_req("events/")

    def destroy_event(self, id):
        """ Destroy an event from the scheduler """
        return self.send_req("events/" + str(id), params={}, verb='DELETE')

    def __str__(self):
        return "<Manager>"
