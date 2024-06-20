Feature: Search for Python Tutorial in w3school
    Scenario Outline: search for tutorial in global search
        Given we go to w3school site
        When we search for "<search_text>" in global search
        Then we check for "<tutorial_text>" in the page
        Examples:
        | search_text|tutorial_text|
        | python|Learn Python|