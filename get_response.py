import json

from constants_api import BASE_URL


def get_response(request_method, method, end_point, params):
    headers = {"Content-Type": "application/json"}

    if request_method == 'GET':
        return method(BASE_URL + end_point, headers=headers)

    elif request_method in ["PATCH", "POST", "DELETE"]:
        return method(BASE_URL + end_point, data=json.dumps(params), headers=headers)
