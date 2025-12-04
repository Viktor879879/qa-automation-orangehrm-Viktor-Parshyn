import pytest
from pages.login_page import LoginPage
from config import ADMIN_USERNAME, ADMIN_PASSWORD


@pytest.mark.smoke
def test_login_with_valid_admin_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    dashboard_page = login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    assert dashboard_page.is_loaded(), "Dashboard should be visible after valid login"


@pytest.mark.negative
def test_login_with_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.login(ADMIN_USERNAME, "wrong_password")
    error_text = login_page.get_error_message()

    assert error_text != "", "Error message should be displayed for invalid login"


@pytest.mark.negative
def test_login_with_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    # Login with empty credentials
    dashboard_page = login_page.login("", "")

    assert not dashboard_page.is_loaded(), "Dashboard must not be visible with empty credentials"