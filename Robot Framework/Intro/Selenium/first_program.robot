*** Settings ***
Documentation    This is my suite documentation
Library    SeleniumLibrary

*** Test Cases ***
Test_Case_01
    [Tags]    Sanity
    Open Browser    https://www.google.com    Google Chrome
    maximize browser window
    sleep    5
    Close Browser

Test_Case_02
    [Tags]    Sanity
    Open Browser    https://www.youtube.com/    Google Chrome
    maximize browser window
    sleep    5
    Close Browser

Test_Case_03
    [Tags]    Sanity
    Open Browser    https://www.udemy.com/    Google Chrome
    maximize browser window
    sleep    5
    Close Browser

*** Keywords ***
