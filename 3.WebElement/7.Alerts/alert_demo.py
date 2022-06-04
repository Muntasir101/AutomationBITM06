from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Alert():
    def test_alert(self):
        base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        time.sleep(5)

        normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
        normal_alert.click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(5)

        confirm_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
        confirm_alert.click()
        driver.switch_to.alert.dismiss()
        time.sleep(3)

        prompt_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
        prompt_alert.click()
        driver.switch_to.alert.send_keys("Test Automation Rocksszzz")
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(5)

        driver.close()


test_obj = Alert()
test_obj.test_alert()
