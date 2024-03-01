from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_loc = (By.ID, "add_btn")
    __row_1_element_loc = (By.XPATH, "//div[@id='row1']/input")
    __row_2_element_loc = (By.XPATH, "//div[@id='row2']/input")
    __row_1_save_button_loc = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button_loc = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_element_loc = (By.ID, "confirmation")
    __row_1_edit_button = (By.ID, "edit_btn")
    __instruction_loc = (By.ID, "instructions")

    def __int__(self, driver: WebDriver):
        super().__init__(driver)

    def open_url(self):
        super()._open_page(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_loc)
        super()._wait_until_element_is_visible(self.__row_2_element_loc)

    def row_2_element(self) -> bool:
        return super()._is_displayed(self.__row_2_element_loc)

    def add_second_food(self, food: str):
        super()._type(self.__row_2_element_loc, food)
        super()._click(self.__row_2_save_button_loc)
        super()._wait_until_element_is_visible(self.__confirmation_element_loc)

    def confirmation_message(self):
        return super()._text(self.__confirmation_element_loc)

    def add_first_row(self, food):
        super()._click(self.__row_1_edit_button)
        super()._wait_until_element_is_clickable(self.__row_1_element_loc)
        super()._clear(self.__row_1_element_loc)
        super()._type(self.__row_1_element_loc, food)
        super()._click(self.__row_1_save_button_loc)
        super()._wait_until_element_is_visible(self.__confirmation_element_loc)

    def are_instruction_displayed(self):
        return super()._is_displayed(self.__instruction_loc)




