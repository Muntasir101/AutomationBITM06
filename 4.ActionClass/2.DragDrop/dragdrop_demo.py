from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class DragDrop():

    def test_dragdrop(self):
        base_url = 'https://jqueryui.com/droppable/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        driver.switch_to.frame(0)
        from_element = driver.find_element(By.ID, 'draggable')
        to_element = driver.find_element(By.ID, 'droppable')
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(from_element, to_element).perform()
            time.sleep(2)

        except:
            print("Drag and Drop Failed.")

        driver.close()


test_obj = DragDrop()
test_obj.test_dragdrop()
