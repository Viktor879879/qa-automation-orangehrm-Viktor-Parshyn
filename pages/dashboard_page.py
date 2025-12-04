from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    PIM_MENU_ITEM = (By.XPATH, "//span[text()='PIM']/ancestor::a")

    def is_loaded(self) -> bool:
        return self.is_visible(self.DASHBOARD_HEADER)

    def go_to_pim(self):
        self.click(self.PIM_MENU_ITEM)