import time

from selenium.webdriver.common.by import By


class LoginPage():
    def __int__(self, driver):
        self.driver = driver

    def login(self, email, password):
        _email_field = self.driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        _password_field = self.driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        _login_btn = self.driver.find_element(By.ID, 'btnLogin')

        _email_field.clear(email)
        _email_field.send_keys()
        time.sleep(2)

        _password_field.clear()
        _password_field.send_keys(password)
        time.sleep(2)

        _login_btn.click()
        time.sleep(2)
