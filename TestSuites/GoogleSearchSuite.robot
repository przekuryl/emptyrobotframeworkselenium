*** Settings ***
Library  SeleniumLibrary
Library  ../Resources/Generator.py
Library  ../TestKeywords/GoogleSearchPage.py

*** Test Cases ***
Search in google
    [Documentation]  Search in google for X names
    [Tags]  search google functionality regression
    Open main page
    accept cookies
    @{list}=  Generate names  10
    FOR    ${item}    IN    @{list}
        search for  ${item}
        Sleep   3s
        go back browser
    END
    Sleep  5s
    [Teardown]    Close Browser


