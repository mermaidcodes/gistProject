import requests
import pytest
import random
import json
from robot.libraries.BuiltIn import _Variables
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from shared import generate_headers, setup_gist_session


Vars = _Variables()



def load_json_data(description):
    valid_post_gist_file_path = 'resources/data/valid_create_gist.json'
    with open(valid_post_gist_file_path) as f:
        create_gist = json.load(f)
        create_gist['description'] = create_gist['description'].replace(create_gist['description'], str(description))
        create_gist['public'] = False
    return create_gist

def test_create_gist(description, expected_status):

    base_url =  Vars.get_variable_value('${BASE_URL}')
    create_gist_uri = Vars.get_variable_value('${GET_GISTS_URI}')

    payload = load_json_data(description)
    url = f"{base_url}{create_gist_uri}"

    # Request to create a gist
    session = setup_gist_session()
    response = session.post(url, json=payload)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    # Assert the status code and response content
    assert str(response.status_code) == str(expected_status), \
        f"Expected {expected_status}, got {response.status_code}"
    if int(response.status_code) == 201:
        assert "id" in response.json(), "ID not found in response"
    return response.json()["id"]



def update_gist(gist_id, updated_description, expected_status):
    base_url = Vars.get_variable_value('${BASE_URL}')
    single_gist_uri = Vars.get_variable_value('${GET_SINGLE_GIST_URI}')
    url = f"{base_url}{single_gist_uri}{gist_id}"

    payload = load_json_data(updated_description)

    # Request to get a single gist by ID
    session = setup_gist_session()
    response = session.patch(url, json=payload)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    assert str(response.status_code) == str(expected_status), \
        f"Expected {expected_status}, got {response.status_code}"

    return   response


