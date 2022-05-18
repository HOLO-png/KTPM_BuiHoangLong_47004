Feature: Test the browserstack application Home Page
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Search Automation in Home Page
    Given Launch the browser search
    When identify search box & enter search text
    Then check title and screenShots search
    And close the browser search
