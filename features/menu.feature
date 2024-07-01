Feature: opening menu links
  @search
  Scenario: user clicks on more button inside header menu
    Given I am on the home page
    When I click on the more button inside header menu
    And I click on photos text hyperlink
    Then I should be navigated to the photos page
