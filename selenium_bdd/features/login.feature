Feature: Login

  Background: Open login page
    Given I am on the login page

  @smoke @regression @login
  Scenario: Login with valid credentials
    When I enter "standard_user" as username
    And I enter "secret_sauce" as password
    And I click on login button
    Then The url of the current page is "https://www.saucedemo.com/inventory.html"

    @tag2
  Scenario: Login with locked out user
    When I enter "locked_out_user" as username
    And I enter "secret_sauce" as password
    And I click on login button
    Then The url of the current page is "https://www.saucedemo.com/"
    And I see login error with text "Epic sadface: Sorry, this user has been locked out."

  Scenario Outline: Login with inexistent user
    When I enter "<username>" as username
    And I enter "<password>" as password
    And I click on login button
    Then The url of the current page is "https://www.saucedemo.com/"
    And I see login error with text "Epic sadface: Username and password do not match any user in this service"
    Examples:
      | username          | password    |
      | user1@yahoo.com   | parola12345 |
      | user2@gmail.com   | parola1     |
      | user3@hotmail.com | asdsfsdfdsf |
      | user4@yahoo.com   | asdfghjkkll |

