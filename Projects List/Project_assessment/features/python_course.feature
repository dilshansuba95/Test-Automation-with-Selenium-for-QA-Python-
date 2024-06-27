Feature: Search for the python course
    Scenario: Search for the python course
        Given User goes to google.lk site
        When User types "eLearning.lk" in Google and clicks the "eLearning.lk" link
        Then User searches for the Python course in the eLearning.lk search bar
        Then User clicks on the Python course and generate a report of the course content after checking 
