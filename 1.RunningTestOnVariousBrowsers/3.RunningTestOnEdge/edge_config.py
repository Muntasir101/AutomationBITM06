from selenium import webdriver

class Test_Edge():
    def launch_edge(self):
        # instantiate firefox browser
        driver = webdriver.Edge(executable_path="E:\Offline_Batch_06\Projects\AutomationBITM06\Drivers\msedgedriver_101.0.exe")


chrome_obj= Test_Edge()
chrome_obj.launch_edge()