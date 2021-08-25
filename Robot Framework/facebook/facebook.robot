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

    input text    id:u_14_b_xv    Tyrion
    #input text    xpath://input[@id='u_14_b_xv']    Tyrion
    sleep    1

    input text    id:u_14_d_ZO    Lannister
    #input text    xpath://input[@id='u_14_d_ZO']    Lannister
    sleep    1

    input text    id:u_14_g_91    gameofthrones@hbo.com
    #input text    xpath://input[@id='u_14_g_91']    gameofthrones@hbo.com
    sleep    1

    input text    id:password_step_input    winteriscoming
    #input text    xpath://input[@id='password_step_input']    winteriscoming
    sleep    1

    Select From List By Value    xpath://select[@id='day']    8
    sleep    1

    Select From List By Value    xpath://select[@id='month']    Jan
    sleep    1

    Select From List By Value    xpath://select[@id='year']    1992
    sleep    1

    click element    xpath://input[@id='u_u_5_cX']
    sleep    2

Close the browser
    [Tags]    value

    Close Browser

*** Keywords ***
