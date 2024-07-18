"""o	Launch Chrome browser.
o	Maximize the browser.
o	Open URL: www.javatpoint.com
o	Scroll down through the web page
o	Click on "AWS" link from the Java Technology section.

"""
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




class GoogleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setting the property for chromedriver.exe
        service = Service(executable_path="chromedriver.exe")
        cls.browser = webdriver.Chrome(service=service)
        cls.browser.maximize_window()
        sleep(2)

    def test_01_scroll(self):
        print("Hello")

    @classmethod
    def tearDownClass(cls):
        # closes the chrome session
        cls.browser.quit()
