# Created by spenserhardin at 2/21/18
Feature: Search for given word

  Scenario: Verify we can search horizontally
    Given a "SCOTTY" to find
    When I search
    Then I find the word horizontally