Feature: Search for new source
    Scenario Outline: check for new source
        Given we go to python.org site
        When we click source code from Downloads menu
        Then we search for the "<latest_relase>" in source

        Examples:
        | latest_relase|
        | Python 3.12.4|
