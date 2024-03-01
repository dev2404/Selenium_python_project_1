import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenario:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open_url()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"

    # @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_loc = driver.find_element(By.ID, "username")
        username_loc.send_keys("students")

        # Type password Password123 into Password field
        password_loc = driver.find_element(By.NAME, "password")
        password_loc.send_keys("Password123")

        # Push Submit button
        submit_button_loc = driver.find_element(By.XPATH, "//Button[@class='btn']")
        submit_button_loc.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_loc = driver.find_element(By.ID, "error")
        assert error_message_loc.is_displayed(), "error message not displayed but it should be displayed"

        # Verify error message text is Your username is invalid!
        error_message = error_message_loc.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

    @pytest.mark.login
   # @pytest.mark.negative

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_loc = driver.find_element(By.ID, "username")
        username_loc.send_keys("student")

        # Type password incorrectPassword into Password field
        password_loc = driver.find_element(By.ID, "password")
        password_loc.send_keys("123")

        # Puch Submit button
        submit_button_loc = driver.find_element(By.XPATH, "//Button[@class='btn']")
        submit_button_loc.click()

        # Verify error message is displayed
        error_message_loc = driver.find_element(By.ID, "error")
        assert error_message_loc.is_displayed(), "error should have been displayed"

        # Verify error message text is Your password is invalid!
        error_message = error_message_loc.text
        assert error_message == "Your password is invalid!", "Error message is not right"
