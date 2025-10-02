from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from test_settings import Settings

class CoreApi:

    def __init__(self):
        self.settings = Settings()

    def install_webdriver(self, browser):
        global driver_path
        if browser.lower() == "chrome":
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager
            self.settings.driver_path = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            # browser_version = webdriver.Chrome().capabilities['browserVersion']
            # driver_version = webdriver.Chrome().capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            # print("Browser Version:", browser_version[:5])
            # print("Driver Version:", driver_version[:5])
            # if browser_version[:5] != driver_version[:5]:
            #     driver_path = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            # else:
            # driver_path = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_manager=cache_manager)))
        if browser.lower() == "firefox":
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from webdriver_manager.firefox import GeckoDriverManager

            driver_path = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        return self.settings.driver_path

    def close_browser(self, driver_path):
        driver_path.quit()

    def get_element_by_xpath(self, path):
        pass

    def get_element_by_css(self, path):
        pass

    def get_element_by_id(self, id):
        pass

    def get_element_by_name(self, name):
        pass


if __name__ == "__main__":
    driver_path = CoreApi().install_webdriver("chrome")
    driver_path.get("https://www.thetestingworld.com/testings")

