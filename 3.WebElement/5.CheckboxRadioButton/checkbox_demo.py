from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Checkbox():
    def test_checkbox(self):
        base_url = 'https://the-internet.herokuapp.com/checkboxes'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        check_box1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
        check_box1_status = check_box1.is_selected()
        print(check_box1_status)

        if not check_box1_status:
            check_box1.click()
            check_box1_click_status = check_box1.is_selected()
            print(check_box1.is_selected())

            if check_box1_click_status:
                print("Test passed.")
            else:
                print("Test failed.")

        check_box2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
        check_box2_status = check_box2.is_selected()
        # print(check_box2_status)

        driver.close()


test_obj = Checkbox()
test_obj.test_checkbox()
