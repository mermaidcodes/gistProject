*** Variables ***
${BASE_URL}                         https://api.github.com
${GET_GISTS_URI}                    /gists
${GET_SINGLE_GIST_URI}              /gists/
${CREATE_GIST_URI}
${PROJECT_ROOT}                     ${EXECDIR}/gistProject

#status codes
${EXPECTED_STATUS_OK}               200
${EXPECTED_STATUS_NOT_FOUND}        404
${EXPECTED_STATUS_CREATED}          201
${EXPECTED_STATUS_UNPROCESSABLE}    422
${EXPECTED_STATUS_NOT_OK}           401
