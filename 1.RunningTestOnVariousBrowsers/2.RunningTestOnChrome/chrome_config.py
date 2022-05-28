from selenium import webdriver

class Test_Chrome():
    def launch_chrome(self):
        # instantiate firefox browser
        driver = webdriver.Chrome(executable_path="E:\Offline_Batch_06\Projects\AutomationBITM06\Drivers\chromedriver_102.0.exe")


chrome_obj= Test_Chrome()
chrome_obj.launch_chrome()