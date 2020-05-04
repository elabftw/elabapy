# -*- coding: utf-8 -*-
import os
import json
import logging
import requests
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

class Error(Exception):
    """Base exception class for this module"""
    pass

class SetupError(Error):
    pass

class DataReadError(Error):
    pass

class JSONReadError(Error):
    pass

class BaseAPI(object):
    """
        Basic api class for elabapy
    """
    token = ""
    endpoint = ""
    dev = False

    def __init__(self, *args, **kwargs):
        self.token = ""
        self.endpoint = ""
        self._log = logging.getLogger(__name__)
        self.dev = False

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

    def __perform_request(self, url, verb=GET, params={}):
        """
            This method will perform the real request,
            in this way we can customize only the "output" of the API call by
            using self.__call_api method.
            This method will return the request object.
        """
        # check we have a token
        if not self.token:
            raise SetupError("No token provided.")

        # check we have an endpoint
        if not self.endpoint:
            raise SetupError("No endpoint provided.")

        # check TLS cert by default
        verify = True
        if self.dev:
            # don't show warning about self-signed certificate in dev mode
            requests.packages.urllib3.disable_warnings()
            # don't check cert validity
            verify=False

        # build url
        url = urljoin(self.endpoint, url)

        # lookup table to find out the apropriate requests method and headers
        method_map = {
            GET: (requests.get, {}),
            POST: (requests.post, {}),
            DELETE: (requests.delete, {}),
        }

        requests_method, headers = method_map[verb]
        headers.update({'Authorization': self.token})
        # NOTE if data is changed to json then headers have application/json for content-type
        kwargs = {'headers': headers, 'data': params, 'verify': verify}

        # remove token from log
        headers_str = str(headers).replace(self.token.strip(), 'TOKEN')
        self._log.debug(f'{verb} {url} {params} {headers_str}')

        # execute request
        req = requests_method(url, **kwargs)

        # this will raise the appropriate HTTPError exception
        if not req.ok:
            req.raise_for_status()
        return req

    def send_req(self, url, params={}, verb=GET, binary=False):
        """ Send the request to the api endpoint. """
        req = self.__perform_request(url, verb, params)

        # 204 No Content
        if req.status_code == 204:
            return True

        if binary:
            return req.content

        try:
            return req.json()
        except ValueError as e:
            raise JSONReadError(
                'Read failed from API: %s' % str(e)
            )

    def post_file(self, url, params):
        """
            POST files
        """
        url = urljoin(self.endpoint, url)
        headers = {'Authorization': self.token}
        req = requests.post(url, headers=headers, files=params, verify=False)

        if req.status_code == 204:
            return True

        try:
            data = req.json()
        except ValueError as e:
            raise JSONReadError(
                'Read failed from API: %s' % str(e)
            )

        if not req.ok:
            msg = [data[m] for m in ("id", "message") if m in data][1]
            raise DataReadError(msg)

        return data

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __unicode__(self):
        return u"%s" % self.__str__()

    def __repr__(self):
        return str(self)
