import base
import pytest


@pytest.mark.required
def test_add_api():
    response, response_body = base.get_api_response('todo/add')
    assert(response_body['message'], "New todo is added successfully"), "Some issue while adding data"


@pytest.mark.required
def test_listing_api():
    response, response_body = base.get_api_response('todo/listing')
    response_validator = False
    mandatory_keys = ['id', 'content', 'created_at']
    if response_body['data']:
        for each in response_body['data']:
            response_validator = base.validate_response_keys(each.keys(),
                                                             mandatory_keys)
            if not response_validator:
                break

    assert response_validator, "Some mandatory keys are not present in listing api response"

