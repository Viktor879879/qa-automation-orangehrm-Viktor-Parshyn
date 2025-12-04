
# OrangeHRM UI Test Automation (Python + Selenium)

Small UI automation project for the OrangeHRM demo application.

The goal of this project is to demonstrate basic UI test automation skills:
- Python + Selenium WebDriver
- Page Object Model (POM)
- pytest as a test runner
- Simple smoke, regression and negative tests for login and PIM modules

## Tech Stack

- Python 3.x
- Selenium WebDriver
- pytest
- webdriver-manager

## Target Application

- OrangeHRM demo: https://opensource-demo.orangehrmlive.com/

## Project Structure

```text
qa-automation-orangehrm-Viktor-Parshyn
├── tests/
│   ├── test_login.py
│   └── test_pim.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── config.py
├── conftest.py
├── requirements.txt
└── README.md