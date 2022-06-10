import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasicAuth():

    def test_auth(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # protocol://username:password@url
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

        time.sleep(10)


test_obj = BasicAuth()
test_obj.test_auth()
