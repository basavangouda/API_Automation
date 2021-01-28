Feature: OrangeHRM login

  Scenario: Login to OrangeHRM with Valid credentials
    Given  Launch the Chrome browser
    When Open a orange HRM homepage
    And Enter username "admin" and password "admin123"
    And click on login button
    Then User must successfully login to the dashboard page

  Scenario Outline: Login to OrangeHRM with Valid credentials
    Given  Launch the Chrome browser
    When Open a orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And click on login button
    Then User must successfully login to the dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adimni   | admin234 |
      | admin    | admin123 |