*** Settings ***
Documentation     GIST - Get Gist Tests
Library           RequestsLibrary
Library           ${EXECDIR}/resources/common/get_keywords.py
Library           ${EXECDIR}/resources/common/shared.py
Resource          ${EXECDIR}/resources/common/shared.robot
#Test Setup        Setup Gist Session
#Test Teardown     Delete All Sessions



*** Variables ***
${non_existent_id}             12345abcde
${invalid_gist_msg}            Not Found


*** Test Cases ***
GIST_01 Get All Gists
    [Documentation]    This test fetches all public gists using the GET /gists endpoint.
    [Tags]             getgist    positive    getallgist
    ${response}=       Test Get Gists                 expected_status=${EXPECTED_STATUS_OK}


GIST_02 Get Single Gist
    [Documentation]    This test checks response for a single gist by ID
    [Tags]             getgist    positive    getsinglegist
    ${response}=        Test Get Gists                expected_status=${EXPECTED_STATUS_OK}
    Set Test Variable   ${gist_id}                    ${response.json()}[0][id]
    Run Keyword If     '${gist_id}' != ${NONE}
    ...         Test Get Single Gist    ${gist_id}    expected_status=${EXPECTED_STATUS_OK}


GIST_03 Get Non-Existent Gist
    [Documentation]    This test verifies response for non-existent gist
    ...                Expected Status Code 404
    [Tags]    getgist  negative   getinvalidgist
    ${response}=        Test Get Invalid Gist        expected_status=${EXPECTED_STATUS_NOT_FOUND}
    should be equal as strings                       ${response.json()}[message]           ${invalid_gist_msg}





#
#GIST_01 Get All Gists
#    [Documentation]    This test fetches all public gists
#    [Tags]    getgist  positive   getallgist
#    ${response}=      GET On Session            github        ${GET_GISTS_URI}     expected_status=200
#    Request Should Be Successful
#    Should Be Equal As Numbers    ${response.status_code}    200
#    Log To Console    ${response.json()}
#    should be equal as strings              ${response.json()}[status]           success
#
#GIST_02 Get Single Gist
#    [Documentation]    This test fetches a single gist by ID
#    [Tags]    getgist  positive   getsinglegist
#    ${response}=      Get Request    github    ${GET_SINGLE_GIST_URI}/${first_gist_id}
#    Should Be Equal As Numbers    ${response.status_code}    200
#    Log To Console    ${response.json()}
#
#GIST_03 Get Non-Existent Gist
#    [Documentation]    This test verifies response for non-existent gist
#    ...  Expected Status Code 404
#    [Tags]    getgist  negative   getinvalidgist
#    ${random}= Generate random string
#    Create Session    github    ${BASE_URL}    headers=${HEADERS}
#    ${response}=    Get Request    github    /gists/${random}
#    Assert Status Code    ${response}    404