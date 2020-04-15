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

ACCESS_FORBIDDEN_MSG = "You don't have permission to access this resource!"

class Error(Exception):
    """Base exception class for this module"""
    pass

class SetupError(Error):
    pass

class DataReadError(Error):
    pass

class JSONReadError(Error):
    pass


class NotFoundError(Error):
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

    def __perform_request(self, url, type=GET, params=None):
        """
            This method will perform the real request,
            in this way we can customize only the "output" of the API call by
            using self.__call_api method.
            This method will return the request object.
        """
        if params is None:
            params = {}

        # check we have a token
        if not self.token:
            raise SetupError("No token provided.")

        # check we have an endpoint
        if not self.endpoint:
            raise SetupError("No endpoint provided.")

        # don't show warning about self-signed certificate in dev mode
        if self.dev:
            requests.packages.urllib3.disable_warnings()

        url = urljoin(self.endpoint, url)

        # lookup table to find out the apropriate requests method,
        # headers and payload type (json or query parameters)
        identity = lambda x: x
        json_dumps = lambda x: json.dumps(x)
        lookup = {
            GET: (requests.get, {}, 'params', identity),
            POST: (requests.post, {'Content-type': 'application/json'}, 'data',
                   json_dumps),
            PUT: (requests.put, {'Content-type': 'application/json'}, 'data',
                  json_dumps),
            DELETE: (requests.delete,
                     {'content-type': 'application/json'},
                     'data', json_dumps),
        }

        requests_method, headers, payload, transform = lookup[type]
        headers.update({'Authorization': self.token})
        kwargs = {'headers': headers, payload: transform(params)}

        # remove token from log
        headers_str = str(headers).replace(self.token.strip(), 'TOKEN')
        self._log.debug('%s %s %s:%s %s' %
                        (type, url, payload, params, headers_str))

        return requests_method(url, verify=False, **kwargs)

    def get_data(self, url, type=GET, params=None, binary=False):
        """
            This method is a basic implementation of __call_api that checks
            errors too. In cas of success the method will return True or the
            content of the response to the request.
        """
        if params is None:
            params = dict()

        req = self.__perform_request(url, type, params)
        if req.status_code == 204:
            return True

        if req.status_code == 404:
            raise NotFoundError()

        if req.status_code == 403:
            return ACCESS_FORBIDDEN_MSG

        if binary:
            data = req.content
        else:
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

    def post_data(self, url, params):
        """
            POST some stuff to change title/date/body or create experiment
        """
        url = urljoin(self.endpoint, url)
        headers = {'Authorization': self.token}
        req = requests.post(url, headers=headers, data=params, verify=False)

        if req.status_code == 204:
            return True

        if req.status_code == 404:
            raise NotFoundError()

        if req.status_code == 403:
            return ACCESS_FORBIDDEN_MSG

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

    def post_file(self, url, params):
        """
            POST files
        """
        url = urljoin(self.endpoint, url)
        headers = {'Authorization': self.token}
        req = requests.post(url, headers=headers, files=params, verify=False)

        if req.status_code == 204:
            return True

        if req.status_code == 404:
            raise NotFoundError()

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
