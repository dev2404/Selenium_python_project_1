from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_loc = (By.TAG_NAME, "h1")
    __exit_button = (By.LINK_TEXT, "Log out")

    def __int__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def actual_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super()._text(self.__header_loc)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__exit_button)



