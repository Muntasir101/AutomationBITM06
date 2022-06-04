from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Navigate():
    def test_navigate(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        print('Base title ' + driver.title)

        # Navigate
        driver.get('https://google.com')
        time.sleep(10)
        print('After open Google ' + driver.title)

        # back
        driver.back()  # demo
        time.sleep(5)
        print('After back ' + driver.title)

        # forward
        driver.forward()  # google
        time.sleep(5)
        print('After forward ' + driver.title)

        driver.find_element(By.NAME, 'q').send_keys("Automation")

        # refresh
        driver.refresh()
        time.sleep(5)

        driver.close()


test_obj = Navigate()
test_obj.test_navigate()
