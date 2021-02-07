
Feature: GitHub APi validation

  Scenario: Session Management check
    Given I have gitHub auth credentials
    When I hit gitRepo API of github
    Then status code of the response should be 401
