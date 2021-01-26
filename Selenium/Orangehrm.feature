
Feature: Orange HRM


  Scenario: Logo Presence on OrangeHRM homepage
    Given  launch Chrome Browser
    When open Orange HRM HomePage
    Then verify the logo present on the home page
    And close browser
