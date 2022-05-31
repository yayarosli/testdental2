Feature: Login
    Scenario: 1
        Given launch the Chrome browser
        When I open the login page
        And I fill in the Email "dd_test_1@outlook.com" and I fill in the Password "}krK,gdC6"
        And I click the login button
        Then I must successfully login to the dashboard page