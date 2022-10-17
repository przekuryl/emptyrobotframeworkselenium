*** Settings ***
Library  SeleniumLibrary
Library  ../Resources/Generator.py
Library  ../TestKeywords/GoogleSearchPage.py

*** Variables ***
@{browser_to_test}=    Create List    Chrome    Firefox

*** Test Cases ***
Search in google
    [Documentation]  Search in google for X names
    [Tags]  search google functionality regression
    @{browser_installed}=  Install list of browsers  ${browser_to_test}
    @{list}=  Generate names  3
    FOR    ${browser}    IN    @{browser_installed}
        Get driver
        Open main page
        accept cookies
        FOR    ${item}    IN    @{list}
            search for  ${item}
            Sleep   3s
            go back browser
        END
        Sleep  5s
        Close Browser
    END
    [Teardown]    Close All Browsers


