import pytest
import allure

from pages.login_page import LoginPage
from utils.excel_reader import get_login_data


@allure.feature("Login")
@allure.story("Login Validation")

@pytest.mark.parametrize(
    "email,password,expected",
    get_login_data()
)
def test_login(driver, email, password, expected):

    login = LoginPage(driver)

    with allure.step("Open Login Page"):
        login.open()

    with allure.step("Enter Email"):
        if email:
            login.enter_email(email)

    with allure.step("Click Continue"):
        login.click_continue()

    if expected == "Pass":

        with allure.step("Enter Password"):
            login.enter_password(password)

        with allure.step("Click Login"):
            login.click_login()

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )