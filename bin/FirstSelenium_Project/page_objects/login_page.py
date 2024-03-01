from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username = (By.ID, "username")
    __password = (By.NAME, "password")
    __submit_button = (By.XPATH, "//Button[@class='btn']")
    __error_message = (By.ID, "error")

    def __int__(self, driver: WebDriver):
        super().__init__(driver)

    def open_url(self):
        super()._open_page(self.__url)

    def execute_login(self, username, password):
        super()._type(self.__username, username)
        super()._type(self.__password, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._text(self.__error_message, 3)
