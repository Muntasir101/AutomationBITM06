from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Headless():
    def test_headless_chrome(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get('https://google.com')

        print('Title : ' + driver.title)
        print('Headless on Chrome Done.')

        driver.close()

    def test_headless_firefox(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
        driver.get('https://jqueryui.com/')

        print('Title : ' + driver.title)
        print('Headless on Firefox Done.')

        driver.close()


test_obj = Headless()
test_obj.test_headless_chrome()
test_obj.test_headless_firefox()
