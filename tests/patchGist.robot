*** Settings ***
Documentation     Gits - Patch or Update a newly created Gist
Library           String
Library           RequestsLibrary
Library           ${EXECDIR}/resources/common/post_keywords.py
Library           ${EXECDIR}/resources/common/shared.py
Resource          ${EXECDIR}/resources/common/shared.robot



*** Variables ***
${Updated_descrption}    New description for the latest Gist


*** Test Cases ***
PATCH_01 This test checks patch
    [Documentation]   This test checks patch gist
    [Tags]   patch
    ${description} =   Generate Random String    20                      [LETTERS]
    ${gist_id}=        Test Create Gist          ${description}          expected_status=${EXPECTED_STATUS_CREATED}

    ${response}=       Update Gist               ${gist_id}     ${Updated_descrption}     expected_status=${EXPECTED_STATUS_OK}
    Should Be Equal       ${response.json()}[id]                            ${gist_id}
    Should Be Equal       ${response.json()}[public]                        ${FALSE}
    Should Be Equal       ${response.json()}[description]                   ${Updated_descrption}
