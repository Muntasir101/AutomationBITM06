from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Screenshot():

    def test_screenshot(self, url, file_name):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)
        file_extension = '.png'
        file_destination_path = "E:\\Offline_Batch_06\\Projects\\AutomationBITM06\\ScreenshotFiles\\"

        try:
            driver.save_screenshot(file_destination_path+file_name+file_extension)
            print("2.Screenshot save to Directory --> " + file_destination_path)

        except:
            print("2.Screenshot Capture Failed.")

        driver.close()


test_obj = Screenshot()
test_obj.test_screenshot('https://jqueryui.com/', 'New2')
