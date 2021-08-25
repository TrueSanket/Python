*** Settings ***
Documentation    This is test suite to validate links on Selenium Website
Library    SeleniumLibrary

*** Test Cases ***
Test_Case_01
    [Tags]    Sanity
    Open Browser    https://www.selenium.dev/    Google Chrome
    maximize browser window
    sleep    2

    click link    Downloads
    sleep    2

    click link    Documentation
    sleep    2

    click link    Projects
    sleep    2

    click link    Support
    sleep    2

    click link    Blog
    sleep    2

    Close Browser

*** Keywords ***