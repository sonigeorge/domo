import requests

BASE_URL = "https://api.signableapi.com"

END_POINT = {'login' : '/login'}
INVALID_ENDPOINT = {'login': '/login123'}

REQUEST_METHOD = {
    'GET': requests.get,
    'POST': requests.post,
    'DELETE' : requests.delete
}

SUCCESS = 200
CREATED = 201
DELETE = 204
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
INTERNAL_SERVER_ERROR = 500