*** Settings ***
Documentation    Testing Facebook Page
Library    SeleniumLibrary

*** Test Cases ***
Navigate to Facebook
    [Tags]    value
    Open Browser    https://en-gb.facebook.com/    Chrome
    Maximize Browser Window
    sleep    2

Verify Facebook logo
    [Tags]    value
    Element Should Be Visible    xpath://img[@class='fb_logo _8ilh img']

Create account with information
    [Tags]    value
    Click Element    xpath://*[contains(text(), "Create New Account")]
    sleep    2

    Click Element    xpath://div[@class='_n3']
    sleep    1

    input text    xpath://input[@name='firstname']    Tyrion
    sleep    1

    input text    xpath://input[@name='lastname']    Lannister
    sleep    1

    input text    xpath://input[@name='reg_email__']    gameofthrones@hbo.com
    sleep    2

    input text    xpath://input[@name='reg_email_confirmation__']    gameofthrones@hbo.com
    sleep    1

    input text    xpath://input[@name='reg_passwd__']    winteriscoming
    sleep    1

    Select From List By Value    xpath://select[@id='day']    8
    sleep    1

    Select From List By Label    id:month    Jan
    sleep    1

    Select From List By Value    xpath://select[@id='year']    1992
    sleep    1

    click element    xpath://input[@value='2']
    sleep    2

Close the browser
    [Tags]    value

    Close Browser

*** Keywords ***
