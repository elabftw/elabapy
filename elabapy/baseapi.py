# -*- coding: utf-8 -*-
import json
import logging
import os
from typing import Dict, Tuple
from urllib.parse import urljoin

import requests


class Error(Exception):
    """Base exception class for this module"""

    pass


class SetupError(Error):
    pass


class BaseAPI(object):
    """
        Basic api class for elabapy
    """

    token: str = ""
    endpoint: str = ""
    # verify TLS cert?
    verify: bool = True

    def __init__(self, *args, **kwargs):
        self._log = logging.getLogger(__name__)
        self.verify = True

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

        # check we have a token
        if not self.token:
            raise SetupError("No token provided.")

        # check we have an endpoint
        if not self.endpoint:
            raise SetupError("No endpoint provided.")

    def send_req(
        self,
        url: str,
        params: Dict = {},
        verb: str = 'GET',
        binary: bool = False,
        param_name: str = 'data',
    ):
        """ Send the request to the api endpoint. """
        # don't show warnings if we chose to disable certificate verification
        if self.verify == False:
            requests.packages.urllib3.disable_warnings()

        # build url
        url = urljoin(self.endpoint, url)

        # lookup table to find out the apropriate requests method and headers
        method_map: Dict[str, Tuple] = {
            'GET': (requests.get, {}),
            'POST': (requests.post, {}),
            'DELETE': (requests.delete, {}),
        }

        requests_method, headers = method_map[verb]
        headers.update({'Authorization': self.token})
        # NOTE if data is changed to json then headers have application/json for content-type
        kwargs = {'headers': headers, param_name: params, 'verify': self.verify}

        # remove token from log
        headers_str = str(headers).replace(self.token.strip(), 'TOKEN')
        self._log.debug(f'{verb} {url} {params} {headers_str}')

        # execute request
        req = requests_method(url, **kwargs)

        # this will raise the appropriate HTTPError exception
        if not req.ok:
            req.raise_for_status()

        # 204 No Content
        if req.status_code == 204:
            return True

        if binary:
            return req.content

        return req.json()
