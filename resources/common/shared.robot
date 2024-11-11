*** Settings ***
Library             RequestsLibrary
Library             OperatingSystem
Library             Collections
Resource            ${EXECDIR}/resources/configs/gistvariables.robot


*** Keywords ***
Setup Gist Session
    [Documentation]    Sets up the Gist connection with authentication token
    ${GITHUB_TOKEN}=   Get Environment Variable     GITHUB_TOKEN
    Create Session    github    ${BASE_URL}    headers={"Authorization": "Bearer %{GITHUB_TOKEN}", "Accept": "application/vnd.github+json"}


Assert Status Code
    [Arguments]    ${response}    ${expected_status}
    ${status_code}=    Get From Dictionary    ${response}    status_code
    Should Be Equal As Numbers    ${status_code}    ${expected_status}
