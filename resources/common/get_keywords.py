import requests
import pytest
import random
from robot.libraries.BuiltIn import _Variables
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from shared import generate_headers, setup_gist_session


Vars = _Variables()


# def extract_gist_id(response):
#     """Extracts the gist ID from a successful response."""
#     if response.status_code == 200 and isinstance(response.json(), list):
#         return response.json()[0].get("id")
#         logger.info("asdfgh: " +response.json()[0].get("id"))
#     return None


def test_get_gists(expected_status):
    """
    Test to fetch all public gists.
    """
    base_url = Vars.get_variable_value('${BASE_URL}')
    get_gist_uri = Vars.get_variable_value('${GET_GISTS_URI}')

    url = f"{base_url}{get_gist_uri}"

    # Request to get all gists
    session = setup_gist_session()
    response = session.get(url)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    # Assert the status code and response content
    if str(response.status_code) != str(expected_status):
        raise Error("Expected status " + str(expected_status) + ", got " + str(response.status_code))
    return  response


def test_get_single_gist(gist_id, expected_status):
    """
    Test to fetch a specific gist using a valid gist ID.
    """
    base_url = Vars.get_variable_value('${BASE_URL}')
    single_gist_uri = Vars.get_variable_value('${GET_SINGLE_GIST_URI}')
    url = f"{base_url}{single_gist_uri}{gist_id}"
    logger.write("url is: " +url)

    # Request to get a single gist by ID
    session = setup_gist_session()
    response = session.get(url)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    # Assert the status code and response content
    assert str(response.status_code) == str(expected_status), f"Expected {expected_status}, got {response.status_code}"
    if str(response.status_code) == str(expected_status):
        assert "id" in response.json(), "ID not found in response"
        assert response.json()["id"] == gist_id, f"Expected gist ID {gist_id}, got {response.json()['id']}"

def test_get_invalid_gist(expected_status):
    """
    Test to fetch a specific gist using a valid gist ID.
    """
    base_url = Vars.get_variable_value('${BASE_URL}')
    single_gist_uri = Vars.get_variable_value('${GET_SINGLE_GIST_URI}')
    gist_id = "QA-INVALID-" + str(random.randint(1, 1000))
    url = f"{base_url}{single_gist_uri}{gist_id}"
    logger.write("url is: " +url)

    # Request to get a single gist by ID
    session = setup_gist_session()
    response = session.get(url)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    # Assert the status code and response content
    assert str(response.status_code) == str(expected_status), f"Expected {expected_status}, got {response.status_code}"
    return response

