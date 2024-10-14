Feature: Login

  @debug @smoke @regression @login
  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter "standard_user" as username
    And I enter "secret_sauce" as password
    And I click on login button
    Then The url of the current page is "https://www.saucedemo.com/inventory.html"

    @tag2
  Scenario: Login with locked out user
    Given I am on the login page
    When I enter "locked_out_user" as username
    And I enter "secret_sauce" as password
    And I click on login button
    Then The url of the current page is "https://www.saucedemo.com/"
    And I see login error with text "Epic sadface: Sorry, this user has been locked out."
