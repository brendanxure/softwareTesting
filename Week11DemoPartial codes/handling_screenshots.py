import unittest
from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.service import Service


class ScreenshotDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        sleep(2)

    def test01_multiple_windows_input(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://www.google.com")
        sleep(5)

        # Save the screenshot as a file in a "Screenshots" directory of the project
        driver.get_screenshot_as_file("Screenshots/firstscreenshot.png")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
