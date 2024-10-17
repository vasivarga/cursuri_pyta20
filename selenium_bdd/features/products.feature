Feature: Products

  Background: Login with existing user
    Given I am on the products page

  Scenario: Products are sorted alphabetically
    Then Product names are sorted alphabetically


  Scenario: Products are sorted in inverse alphabetical order
    When I sort the products "Name (Z to A)"
    Then Product names are sorted in inverse alphabetical order

  @debug
  Scenario: Products are sorted by price (low to high)
    When I sort the products "Price (low to high)"
    Then Products are sorted by price (low to high)

    #Tema: Test pentru sortare inversa dupa pret
    # + puteti implementa celelalte teste de pe products page (din frameworkul cu unittest)



