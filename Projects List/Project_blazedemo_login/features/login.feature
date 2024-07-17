Feature: Login functionality

  Scenario: Valid login
    Given I am on the login page
    When I enter a valid email and password
    And I click remember me
    And I click the login button
    Then I should be logged in successfully

  Scenario: Invalid login
    Given I am on the login page
    When I enter an invalid email and password
    And I click the login button
    Then I should see an error message

  Scenario: Edge case login
    Given I am on the login page
    When I enter edge case email and password
    And I click the login button
    Then I should see an appropriate error message