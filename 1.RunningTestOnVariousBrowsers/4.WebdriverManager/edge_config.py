from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class edge():
    def edge_launch(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get('https://google.com')
        driver.close()


test_obj = edge()
test_obj.edge_launch()
