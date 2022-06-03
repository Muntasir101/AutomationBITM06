from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class firefox():
    def firefox_launch(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://google.com")
        driver.close()


test_obj = firefox()
test_obj.firefox_launch()
