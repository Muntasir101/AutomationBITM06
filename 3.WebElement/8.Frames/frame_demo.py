from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class iFrame():

    def test_iframe(self):
        base_url = 'https://the-internet.herokuapp.com/iframe'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        time.sleep(5)

        # Switch to frame
        driver.switch_to.frame('mce_0_ifr')
        time.sleep(3)

        input_field = driver.find_element(By.ID, 'tinymce')
        input_field.clear()
        input_field.send_keys("Test Automation")
        time.sleep(5)

        driver.close()


test_obj = iFrame()
test_obj.test_iframe()
