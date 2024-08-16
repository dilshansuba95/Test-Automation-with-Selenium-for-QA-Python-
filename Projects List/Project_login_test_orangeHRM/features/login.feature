Feature: Login Functionality of expandtesting.com

    Scenario: Valid login test (Positive)
        Given I Open login page
        When  I Type username 'Admin' into Username field
        When  I Type password '@6f@D7@jnSPN' into Password field
        When I Push Login button
        And I Verify new page URL contains orangehrm.com/dashboard/index
        And I Verify new page contains expected text ('Dashboard' or 'successfully logged in')
        Then I Verify button Log out is displayed on the new page

    Scenario: Invalid login test - Username (Negative)
        Given I Open login page
        When I Type username 'incorrectUser' into Username field
        When I Type password '@6f@D7@jnSPN' into Password field
        And I Push Login button
        Then I Verify error message for username is displayed
        

    Scenario: Invalid login test - password (Negative)
        Given I Open login page
        When I Type username 'Admin' into Username field
        When I Type password 'incorrectPassword' into Password field
        And I Push Login button
        Then I Verify error message for password is displayed
        








