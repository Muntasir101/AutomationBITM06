from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class OrangeHRM():
    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        username = driver.find_element(By.ID, 'txtUsername')
        if username is not None:
            print("We found username by ID")
        else:
            print("We dont found username by ID")

        password = driver.find_element(By.NAME, 'txtPassword')
        if password is not None:
            print("We found Password by name")
        else:
            print("We dont found password by name")

        driver.close()


test_obj = OrangeHRM()
test_obj.login()
