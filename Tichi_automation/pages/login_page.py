from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL = (By.XPATH, "//input[@type='email']")
    CONTINUE = (By.XPATH, "//button[@type='submit']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://tichi-app-webapp-stage.web.app/home")

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).clear()

        self.driver.find_element(*self.EMAIL).send_keys(email)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE)
        ).click()

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).clear()

        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )