import json

import requests

from constants_api import END_POINT, REQUEST_METHOD, INVALID_ENDPOINT
from get_response import get_response
from test_data import VALID_LOGIN


class APIRequest:
    def send(self, params):
        resp = get_response(request_method=self.request_method,
                            method=self.method,
                            end_point=self.end_point,
                            params=params)
        return resp.status_code


class LoginAPI(APIRequest):

    def __init__(self):
        self.request_method = "POST"
        self.method = REQUEST_METHOD['POST']
        self.end_point = END_POINT['login']


post_login = LoginAPI()


class LoginGetAPI(APIRequest):

    def __init__(self):
        self.request_method = "GET"
        self.method = REQUEST_METHOD['GET']
        self.end_point = END_POINT['login']


class IncorrectEndpoint(APIRequest):

    def __init__(self):
        self.request_method = "GET"
        self.method = REQUEST_METHOD['GET']
        self.end_point = INVALID_ENDPOINT['login']
