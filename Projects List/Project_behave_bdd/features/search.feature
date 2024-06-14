#Scenarios in behave are written using the Gherkin syntax

Feature: download Python latest version
    Scenario: download python latest version
        Given we go to python.org site
        When we click downloads
        Then we should download python 3.12.4

