from enum import Enum


class ResponseMessages(Enum):
    todo_listing_found = "Listing data found"
    todo_listing_not_found = "No listing data found"
    todo_add = "New todo is added successfully"
    todo_content_empty = "Todo content is submitted as empty."


class ResponseCodes(Enum):
    success = 200
    created = 201
    bad_request = 400
    un_authorized = 401
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    conflict = 409
    precondition_failed = 412
    server_error = 500
    service_unavailable = 503


class Response:
    @staticmethod
    def success(code=ResponseCodes.success.value, message="success", data=[], key='data'):
        return {
            'code': code,
            'status': "success",
            'message': message,
            key: data
        }

    @staticmethod
    def error(code=ResponseCodes.server_error.value, message="error"):
        return {
            'code': code,
            'status': "error",
            'message': message
        }

