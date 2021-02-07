
Feature: verify if user is added and deleted using library API
  @library
  Scenario: Verify add user API functionality
    Given the user details which are need to be added to Library
    When  we execute the addUser PostAPI Method
    Then user is successfully added
    And status code of the response should be 200

  @library
  Scenario Outline:Verify add user API functionality
    Given the user details which is given <user>
    When  we execute the addUser PostAPI Method
    Then user is successfully added
      Examples:
      | user          |
      | basavanagowda |
      | Jadeyappa     |
