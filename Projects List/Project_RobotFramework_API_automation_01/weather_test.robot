*** Settings ***
Library           RequestsLibrary
Library           CustomKeywords.py

*** Variables ***
${API_KEY}    a873024698c088ef8ecbceb087f13bb2
${BASE_URL}      https://api.openweathermap.org/data/2.5/weather?q=Sri%20Lanka&appid=${API_KEY}

*** Test Cases ***
Get Weather Data for Sri Lanka
    [Documentation]    Get weather data for Sri Lanka
    Disable Warnings    # Call the custom keyword to disable warnings
    Create Weather API Session
    ${response}    GET On Session    weather_api    /
    Should Be Equal As Strings    ${response.status_code}    200
    Log    Weather data: ${response.json()}

*** Keywords ***
Create Weather API Session
    Create Session    weather_api    ${BASE_URL}