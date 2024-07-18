"""o	Invoke Chrome Browser
o	Open URL: https://www.google.co.in/
o	Get Page Title name and Title length
o	Print Page Title and Title length on Pycharm console
o	Get page URL and verify whether it is the desired page or not
o	Get page Source and Page Source length
o	Print page source Length on console
o	Close the Browser
"""
from time import sleep
import unittest
from selenium import webdriver
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

    def test_page_search(self):
        browser = self.browser
        browser.get('https://www.google.co.in/')

        # Printing Title & Title length in the Console window
        print("Title of the page is : " + browser.title)
        print("Length of the title is : ", len(browser.title))

        #  Storing URL in String variable
        actualurl = browser.current_url
        print("The actual URL of the webpage is " + actualurl)

        assert actualurl == browser.current_url     # Success Case

        # compareurl = "https://www.rediff.com/"
        # # change it to https://www.google.com/ to find true case
        # print("The actual URL of the webpage is " + compareurl)
        # assert compareurl == browser.current_url    # Failure case

        # Storing Page Source in String variable
        pagesource = browser.page_source
        print("The Page Source is : ", pagesource)

        #  Storing Page Source length in Int variable
        pagesource_length = len(pagesource)

        #  Printing length of the Page Source on console
        print("Total length of the Page Source is : ", pagesource_length)

    @classmethod
    def tearDownClass(cls):
        # closes the chrome session
        cls.browser.quit()
