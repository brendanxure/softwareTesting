import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

class MultipleWindowsDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        sleep(2)

    # Go to http://demo.guru99.com/popup.php and click on "click here" . A pop up window will appear
    # to input your email id. Get and print window title
    def test_multiple_windows(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/popup.php")
        sleep(5)

        # Find the link test and Click on it
        driver.find_element(By.LINK_TEXT, "Click Here").click()
        sleep(5)
        # Get all window handles
        handler = driver.window_handles

        # Get the number of window opened
        size = len(handler)
        print(size)

        # Switch to the window using driver.switch_to.window(handles)
        # Get and print window title
        for x in range(size):
            driver.switch_to.window(handler[x])
            print(driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
