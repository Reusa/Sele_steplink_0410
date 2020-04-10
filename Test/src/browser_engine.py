import configparser
import os.path
from selenium import webdriver
from Test.config.globalparameter import chrome_driver_path, project_path, config_file_path, img_path


class BrowserEngine(object):
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        config.read(config_file_path, encoding='utf-8')
        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        if browser == "Chrome":
            driver = webdriver.Chrome(chrome_driver_path)
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "IE":
            driver = webdriver.ie()

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        self.driver.quit()
