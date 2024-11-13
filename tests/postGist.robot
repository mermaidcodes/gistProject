*** Settings ***
Documentation     GIST - Post Gist Tests
Library           String
Library           RequestsLibrary
Library           ${EXECDIR}/resources/common/post_keywords.py
Library           ${EXECDIR}/resources/common/get_keywords.py
Library           ${EXECDIR}/resources/common/shared.py
Resource          ${EXECDIR}/resources/common/shared.robot




*** Test Cases ***
GIST_03 Create Gist from JSON File
    [Documentation]    This test creates a new gist using data from a JSON file (valid_create_gist.json).
    [Tags]             postgist    positive    postvalidgist
    ${description} =      Generate Random String    20                      [LETTERS]
    ${gist_id}=           Test Create Gist          ${description}          expected_status=${EXPECTED_STATUS_CREATED}
    Log To Console        Created Gist ID:          ${gist_id}

    #Verify if gist is created with its content
    ${response}=          Test Get Single Gist      ${gist_id}              expected_status=${EXPECTED_STATUS_OK}
    Should Be Equal       ${response.json()}[id]                            ${gist_id}
    Should Be Equal       ${response.json()}[public]                        ${FALSE}
    Should Be Equal       ${response.json()}[description]                   ${description}
