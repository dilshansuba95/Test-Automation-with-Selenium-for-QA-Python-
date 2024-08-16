Feature: Registration Page

  Scenario Outline: Valid registration
    Given I am on the registration page
    When I enter "<name>" in the Name field
    And I enter "<company>" in the Company field
    And I enter "<email>" in the E-Mail Address field
    And I enter "<password>" in the Password field
    And I enter "<confirm_password>" in the Confirm Password field
    And I submit the registration form
    Then I should see a success message

    Examples:
      | name     | company | email                | password | confirm_password |
      | John Doe | ABC Inc | john.doe@example.com | Pass1234 | Pass1234         |

  Scenario Outline: Invalid registration
    Given I am on the registration page
    When I enter "<name>" in the Name field
    And I enter "<company>" in the Company field
    And I enter "<email>" in the E-Mail Address field
    And I enter "<password>" in the Password field
    And I enter "<confirm_password>" in the Confirm Password field
    And I submit the registration form
    Then I should see an error message

     Examples:
      | name     | company | email                | password | confirm_password |
      |          | ABC Inc | john.doe@example.com | Pass1234 | Pass1234         |  
      | John Doe |         | john.doe@example.com | Pass1234 | Pass1234         |  
      | John Doe | ABC Inc | doe.@.com            | Pass1234 | Pass1234         |  
      | John Doe | ABC Inc | john.doe@example.com | Pass     | Pass             |  
      | John Doe | ABC Inc | john.doe@example.com | Pass1234 | Pass4321         |  

  Scenario Outline: Edge case registration
    Given I am on the registration page
    When I enter "<name>" in the Name field
    And I enter "<company>" in the Company field
    And I enter "<email>" in the E-Mail Address field
    And I enter "<password>" in the Password field
    And I enter "<confirm_password>" in the Confirm Password field
    And I submit the registration form
    Then I should see an appropriate message

     Examples:
      | name                                   | company | email                | password | confirm_password |
      | A very long name                       | ABC Inc | john.doe@example.com | Pass1234 | Pass1234         |
      | A very long name#1#1#################  | ABC Inc | john.doe@example.com | Pass1234 | Pass1234         |
      | John Doe                               | ABC Inc | john.doe@example.com |          |                  |
      | John Doe                               | ABC Inc | john.doe@example.com | Pass1234 |                  |