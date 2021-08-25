*** Settings ***
Documentation    Sauce Labs Demo
Library    SeleniumLibrary

*** Test Cases ***
Open Browser and Webpage
    [Tags]    Value
    Open Browser    https://www.saucedemo.com/    Chrome
    Maximize Browser Window
    sleep    2

Login to Account
    [Tags]    Value
    input text    id:user-name    standard_user
    sleep    1

    input text    id:password    secret_sauce
    sleep    1

    click element    xpath://input[@id='login-button']
    sleep    2

Select all the items, add to the cart and checkout
    [Tags]    Value
    click element    xpath://button[@id='add-to-cart-sauce-labs-backpack']
    sleep    1

    click element    xpath://button[@id='add-to-cart-sauce-labs-bike-light']
    sleep    1

    click element    xpath://button[@id='add-to-cart-sauce-labs-bolt-t-shirt']
    sleep    1

    click element    xpath://button[@id='add-to-cart-sauce-labs-fleece-jacket']
    sleep    1

    click element    xpath://button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']
    sleep    1

    click element    xpath://*[@class='shopping_cart_link']
    sleep    1

    Execute Javascript    window.scrollBy(0,document.body.scrollHeight)
    sleep    2

    click element    xpath://button[@id='checkout']
    sleep    1

Fill information in Checkout and continue
    [Tags]    Value
    input text    id:first-name    Tyrion
    sleep    1

    input text    id:last-name    Lannister
    sleep    1

    input text    id:postal-code    77095
    sleep    1

    click element    xpath://input[@id='continue']
    sleep    2

Review checkout, scroll to the end and finish order
    [Tags]    Value
    click element    xpath://button[@id='finish']
    sleep    2

    Execute Javascript    window.scrollBy(0,document.body.scrollHeight)
    sleep    2

Verify Thank you
    [Tags]    Value
    Element Should Be Visible    //h2[contains(text(),'THANK YOU FOR YOUR ORDER')]

Logout successfully and exit browser
    [Tags]    Value
    click element    xpath://button[@id='react-burger-menu-btn']
    sleep    2

    click element    xpath://a[@id='logout_sidebar_link']
    sleep    2

    close browser

*** Keywords ***