from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()
        return element

    def type(self, locator, text: str, clear: bool = True):
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    def is_visible(self, locator) -> bool:
        try:
            self.find(locator)
            return True
        except Exception:
            return False