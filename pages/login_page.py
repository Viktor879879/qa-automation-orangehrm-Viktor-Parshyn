from selenium.webdriver.common.by import By
from .base_page import BasePage
from .dashboard_page import DashboardPage
from config import BASE_URL


class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

    def open_login_page(self):
        self.open(BASE_URL)

    def login(self, username: str, password: str) -> DashboardPage:
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return DashboardPage(self.driver)

    def get_error_message(self) -> str:
        if self.is_visible(self.ERROR_MESSAGE):
            return self.find(self.ERROR_MESSAGE).text
        return ""