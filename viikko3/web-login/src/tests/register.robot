*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  test
    Set Password    testing1
    Set Password confirmation  testing1
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testing111
    Set Password confirmation  testing111
    Submit Register
    Register Should Fail With Message  Username invalid

Register With Valid Username And Invalid Password
    Set Username  moi
    Set Password  moi1
    Set Password Confirmation  moi1
    Submit Register
    Register Should Fail With Message  Password invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  moimoi123
    Set Password confirmation  moimoi321
    Submit Register
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  heii
    Set Password  testi12345
    Set Password confirmation  testi12345
    Submit Register
    Register Should Succeed
    Go To Login Page
    Set Username  heii
    Set Password  testi12345
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  a
    Set Password  testi1234
    Set Password confirmation  testi1234
    Submit Register
    Register Should Fail With Message  Username invalid
    Go To Login Page
    Set Username  a
    Set Password  testi1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
