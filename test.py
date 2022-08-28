import unittest

from constants_api import SUCCESS, UNAUTHORIZED, BAD_REQUEST, METHOD_NOT_ALLOWED, NOT_FOUND
from pages import post_login, LoginGetAPI, IncorrectEndpoint
from test_data import VALID_LOGIN, INVALID_LOGIN, INCORRECT_DATA


class TestAPI(unittest.TestCase):

    def test_login_api_valid(self):
        assert post_login.send(VALID_LOGIN) == SUCCESS

    def test_login_api_invalid(self):
        assert post_login.send(INVALID_LOGIN) == UNAUTHORIZED

    def test_login_api_incorrect_data(self):
        assert post_login.send(INCORRECT_DATA) == BAD_REQUEST

    def test_login_api_incorrect_method(self):
        login_get_api = LoginGetAPI()
        assert login_get_api.send(VALID_LOGIN) == METHOD_NOT_ALLOWED

    def test_incorrect_endpoint(self):
        incorrect_endpoint = IncorrectEndpoint()
        assert incorrect_endpoint.send(VALID_LOGIN) == NOT_FOUND
