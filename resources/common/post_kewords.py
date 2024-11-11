import random
import shared.py
import requests
import pytest
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import json

def get_robot_variable(var_name):
    return BuiltIn().get_variable_value(var_name)

def load_json_data(file_path):
    # Get file path
    description = get_robot_variable('${DESCRIPTION}')
    valid_post_gist_file_path = './gistProject/data/valid_post_gist_file.json'

    with open(valid_post_gist_file_path) as f:
        create_gist = json.load(f)
        create_gist['description'] = create_gist['description'].replace(create_gist['description'], description)
        create_gist['origin'] = create_gist['origin'].replace(create_gist['origin'], entity + '.bob')

    return json.dumps(create_gist)

def test_create_gist(expected_status):
    """
    Test to create a new gist using data from a JSON file.
    """
    # Load the JSON data for creating the gist
    json_file_path = os.path.join(get_robot_variable('${PROJECT_ROOT}'), 'data', 'valid_create_gist.json')
    payload = load_json_data(json_file_path)

    # Fetch URL and headers from Robot Framework variables
    base_url = get_robot_variable('${BASE_URL}')
    create_gist_uri = get_robot_variable('${CREATE_GIST_URI}')
    headers = json.loads(get_robot_variable('${HEADERS}'))
    url = f"{base_url}{create_gist_uri}"

    # Request to create a gist
    response = requests.post(url, headers=headers, json=payload)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    # Assert the status code and response content
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    if response.status_code == 201:
        assert "id" in response.json(), "ID not found in response"
        return response.json()["id"]



def test_create_gist_invalid(expected_status, payload):
    """
    Test to attempt creating a new gist with invalid data.
    """
    base_url = get_robot_variable('${BASE_URL}')
    create_gist_uri = get_robot_variable('${CREATE_GIST_URI}')
    headers = json.loads(get_robot_variable('${HEADERS}'))
    url = f"{base_url}{create_gist_uri}"

    # Request to create a gist with invalid data
    response = requests.post(url, headers=headers, json=payload)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    # Assert the status code and error message
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    if response.status_code == 422:
        assert "message" in response.json(), "Error message not found in response"
        assert response.json()["message"] == "Validation Failed"
