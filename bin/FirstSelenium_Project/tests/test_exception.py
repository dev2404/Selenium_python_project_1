import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.exception_page import ExceptionPage


class TestExceptionScenario:

    @pytest.mark.exception
    # @pytest.mark.debug
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_url()
        exception_page.add_second_row()
        assert exception_page.row_2_element(), "row2 not displayed"

    @pytest.mark.exception
    # @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_url()
        exception_page.add_second_row()
        exception_page.row_2_element()
        exception_page.add_second_food("fries")
        assert exception_page.confirmation_message() == "Row 2 was saved", "confirmation not expected"

    @pytest.mark.exception
    #@pytest.mark.debug
    def test_timeout_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_url()
        exception_page.add_second_row()
        assert exception_page.row_2_element(), "row 2 not dispalyed"

    @pytest.mark.exception
    # @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_url()
        exception_page.add_first_row("fries")
        assert exception_page.confirmation_message() == "Row 1 was saved", "confirmation message is not expected"

    @pytest.mark.exception
    # @pytest.mark.debug
    def test_invalid_element_state_exception_2(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open_url()
        exception_page.add_second_row()
        assert not exception_page.are_instruction_displayed(), "instruction not displayed"
