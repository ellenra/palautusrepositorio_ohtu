*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    testaaja    testaaja123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  salasana12
    Output Should Contain    User with username testi already exists

Register With Too Short Username And Valid Password
    Input Credentials    mm    testi3211
    Output Should Contain    Username invalid

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    HuoNo1    numeroita1
    Output Should Contain    Username invalid

Register With Valid Username And Too Short Password
    Input Credentials    testaaja    sal1
    Output Should Contain    Password invalid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    testaajaa    salasana
    Output Should Contain    Password invalid

*** Keywords ***
Input New Command And Create User
    Create User  testi  testi321
    Input New Command
