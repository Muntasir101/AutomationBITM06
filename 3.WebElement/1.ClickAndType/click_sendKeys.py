from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class OrangeHRM():
    def test_login_valid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Element
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn= driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        time.sleep(5)

    def test_login_Invalid(self):
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()

            driver.get("https://opensource-demo.orangehrmlive.com/")

            # Find Element
            username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
            password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
            login_btn = driver.find_element(By.ID, 'btnLogin')

            # Login Action
            username.clear()
            username.send_keys('Admin213334')

            password.clear()
            password.send_keys('admin123')

            login_btn.click()

            time.sleep(5)

            driver.close()


test_obj = OrangeHRM()
test_obj.test_login_valid()
test_obj.test_login_Invalid()