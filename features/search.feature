Feature: Search functionality

  Scenario Outline: User searches for various queries
    Given I am on the home page
    When I click on the search button
    And I enter the search query "<query>"
    Then I should see the search results

    Examples:
      | query    |
      | news     |
      | sports   |
      | cricket  |
      | football |
