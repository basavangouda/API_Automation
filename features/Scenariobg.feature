'''Feature: OrangeHRM Login

  Background: common steps
    Given  launch the Chrome browser
    When Open a orange HRM homepage
    And Enter username  and password
    And click on login button

  Scenario: Login to OrangeHRM with Valid credentials
    Then User must login to the dashboard page

  Scenario: Search user
    When navigate to search page
    Then search page should be displayed

  Scenario: Advanced Search user
    When navigate to advanced search page
    Then advanced search page should be displayed'''