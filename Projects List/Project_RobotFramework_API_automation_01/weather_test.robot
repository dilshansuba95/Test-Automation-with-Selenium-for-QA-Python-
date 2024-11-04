*** Settings ***
Library           RequestsLibrary
Library           CustomKeywords.py

*** Variables ***
${API_KEY}    a873024698c088ef8ecbceb087f13bb2
${BASE_URL}      https://api.openweathermap.org
${Relative_URL}     /data/2.5/weather?q=Sri%20Lanka&appid=${API_KEY}   

*** Test Cases ***
Get Weather Data for Sri Lanka
    [Documentation]    Get weather data for Sri Lanka
    disable_warnings    # Call the custom keyword to disable warnings
    Create Weather API Session
    ${response}    GET On Session    weather_api    ${Relative_URL}
    Should Be Equal As Strings    ${response.status_code}    200
    Log To Console    ${response.status_code}

    # Convert response content to pretty JSON and log it
    ${pretty_json}    Evaluate    json.dumps(json.loads('''${response.content}'''), indent=4)    json
    Log To Console    ${pretty_json}
    Log    Weather data: ${pretty_json}

*** Keywords ***
Create Weather API Session
    Create Session    weather_api    ${BASE_URL}
