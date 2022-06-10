from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Upload:
    def test_upload(self):
        file = "C:\\Users\\Asus\\Downloads\\th.jpg"

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Element
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # My_Info Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My_info link click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # click contact details
        driver.find_element(By.LINK_TEXT, 'Contact Details').click()
        # Input field

        #Add Attachment

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys(file)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('hello')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(2)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()

        driver.save_screenshot('E:\\Offline_Batch_06\\Projects\\AutomationBITM06\\ScreenshotFiles\\Orange.png')

        driver.close()


test_obj = Upload()
test_obj.test_upload()
