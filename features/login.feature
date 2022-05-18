Feature: Test the browserstack application Login Page
  Scenario: Verify login functionality
    Given Launch the App
    When Enter login credentials
    Then Screenshot login
    Then Handle logout
    And Close the App

  Scenario: Testing of a User Signup Form
    Given Launch the App Signup
    When enter Signup credentials
    Then accept cookie notification
    Then validate signup form
    Then click signup
    Then verify the page title and screenshot Signup
    And close the App Signup
