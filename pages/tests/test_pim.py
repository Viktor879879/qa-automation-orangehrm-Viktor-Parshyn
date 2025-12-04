import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from config import ADMIN_USERNAME, ADMIN_PASSWORD


@pytest.mark.regression
def test_pim_menu_is_accessible_after_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    dashboard_page = login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    assert dashboard_page.is_loaded(), "Dashboard should be loaded after login"

    dashboard_page.go_to_pim()

    pim_header = (By.XPATH, "//h6[text()='PIM']")
    assert dashboard_page.is_visible(pim_header), "PIM page should be visible after navigation"