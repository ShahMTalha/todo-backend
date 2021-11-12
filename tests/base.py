import json
import requests
import routes

response_body = ""
default_success_codes = [200, 201]
default_content_type = "application/json"


def get_api_response(route_endpoint, success_codes=default_success_codes,
                     status='success', content_type=default_content_type):
    request_content = routes.routing_mapper[route_endpoint]
    endpoint = routes.base_url + request_content['route']

    payload = request_content['payload']
    method = request_content['method']
    if method == 'get':
        response = requests.get(url=endpoint, data=payload)
    elif method == 'post':
        response = requests.post(url=endpoint, data=payload)
    elif method == 'put':
        response = requests.put(url=endpoint, data=payload)
    else:
        response = requests.post(url=endpoint, data=payload)
    response_body = load_response_body(response)
    assert check_content_type(response.headers['Content-Type'], content_type), "Content type not matching"
    assert check_response_code(response_body['code'], success_codes), "Response code not matching"
    assert check_response_status(response_body['status'], status), "Response status not matching"
    return response, response_body


def check_content_type(response_header_content, content_type=default_content_type):
    return True if response_header_content == content_type else False


def check_response_code(response_code, success_codes=default_success_codes):
    success_codes = success_codes if type(success_codes) is list else [success_codes]
    return True if response_code in success_codes else False


def check_response_status(response_status, status='success'):
    return True if response_status == status else False


def check_response_message(response_message, success_case_message):
    return True if response_message == success_case_message else False


def load_response_body(response):
    return json.loads(response.text)

def validate_response_keys(response_keys, mandatory_keys):
    flag = False
    if all(x in response_keys for x in mandatory_keys):
        flag = True
    return flag


