from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class OrangeHRM():
    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        if username is not None:
            print("We found username by Xpath")
        else:
            print("We dont found username by Xpath")

        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        if password is not None:
            print("We found password by CSS")
        else:
            print("We dont found password by CSS")

        driver.close()


test_obj = OrangeHRM()
test_obj.login()