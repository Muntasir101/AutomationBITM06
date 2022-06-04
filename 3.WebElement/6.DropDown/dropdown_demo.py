from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Dropdown():
    def test_dropdown(self):
        base_url = 'https://the-internet.herokuapp.com/dropdown'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        time.sleep(5)

        dropdown_opt = driver.find_element(By.ID, 'dropdown')
        sel = Select(dropdown_opt)
        #sel.select_by_visible_text('Option 1')
       # sel.select_by_index(2)
        sel.select_by_value('1')
        time.sleep(5)


test_obj = Dropdown()
test_obj.test_dropdown()