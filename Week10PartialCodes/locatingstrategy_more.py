"""
Test case 1: To check about link and partial link test on http://demo.guru99.com/test/link.html
first link will take you to Google.com and second link will take to facebook.com. But then there is a
problem too. Watch it and correct it in below code
"""

from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager


class GoogleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setting the property for chromedriver.exe
        service = Service(executable_path="chromedriver.exe")
        cls.browser = webdriver.Chrome(service=service)
        cls.browser.maximize_window()
        sleep(2)

    def test_01_link_locators(self):
        browser = self.browser
        browser.get('http://demo.guru99.com/test/link.html')

        # click on a link on the browser using link text locator
        browser.find_element(By.LINK_TEXT, "click here").click()
        print("The website opened after the first click is ", browser.current_url)
        wait = WebDriverWait(browser, 5)


        # Take the browser back to original
        browser.back()
        print("The website  after coming back is ", browser.current_url)

        # click on a link on the browser using partial_link text locator
        browser.find_element(By.PARTIAL_LINK_TEXT, "click he").click()
        print("The website opened after using partial link text is ", browser.current_url)
        wait = WebDriverWait(browser, 5)


        # So, how to get around the above problem? In cases where there are multiple links with the
        # same link text, and we want to access the links other than the first one, how do we go about it?
        # In such cases, generally, different locators viz... By.xpath(), By.cssSelector() or
        # By.tagName() are used. Most commonly used is By.xpath(). It is the most reliable one but
        # it looks complex and non-readable too.
        browser.back()
        print("The website  after coming back is ", browser.current_url)


        # click on a link on the browser using partial_link text locator
        # The tag name happens to be the same for both
        browser.find_element(By.XPATH, "/html[1]/body[1]/a[2]").click()
        print("The website after using tag name on the link is ", browser.current_url)


    @classmethod
    def tearDownClass(cls):
        # closes the chrome session
        cls.browser.quit()
