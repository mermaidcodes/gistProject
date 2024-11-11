*** Settings ***
Documentation     GIST - Get Gist Tests
Library           RequestsLibrary
Resource          ${EXECDIR}/resources/common/shared.robot
Library           ${EXECDIR}/resources/common/get_keywords.py
Test Setup        Setup Gist Session      ${GITHUB_TOKEN}
#Test Teardown     Delete All Sessions

*** Variables ***
${DESCRIPTION}   "QA-CREATENEWGIST" + str(random.randint(1, 10000))

*** Test Cases ***
GIST_03 Create Gist from JSON File
    [Documentation]    This test creates a new gist using data from a JSON file (valid_create_gist.json).
    [Tags]             postgist    positive    postvalidgist
    ${gist_id}=        Test Create Gist    expected_status=${EXPECTED_STATUS_CREATED}
    Log To Console     Created Gist ID: ${gist_id}

    #Verify if gist is created
    ${response}=        Test Get Gists    expected_status=${EXPECTED_STATUS_OK}
    Set Test Variable    ${gist_id}
    Should Contain       ${response}      ${DESCRIPTION}


#GIST_04 Create Gist (Invalid Data)
#    [Documentation]    This test attempts to create a gist with invalid data, expecting a validation error.
#    [Tags]             postgist    negative    postinvalidgist
#    ${response}=       Test Create Gist Invalid    expected_status=${EXPECTED_STATUS_UNPROCESSABLE}    payload=${INVALID_PAYLOAD}
#    Log To Console     ${response}
