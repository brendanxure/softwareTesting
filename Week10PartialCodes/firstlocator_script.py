""" First Script of locator using selenium webdriver with python
    Follows from the lecture presentation test case
1.Import WebDriver from selenium.
2.Open the Google Chrome browser.
3.Maximize the browser window.
4.Navigate to the Google home page.
5.Identify the Google search text box and pass the value.
6.Click on the Google search button.
7.Close the Browser.
Follow the unit test framework with fixtures- setUpClass(),tearDownClass() and test methods
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

    def test_page_search(self):
        self.browser.get('https://www.google.com/')
        # Search Google Input text by id locator
        self.browser.find_element(By.NAME, "q").send_keys("Quantum Computing")
        # sleep(5)    # Introduced sleep just to check the browser behaviour, not needed everytime

        wait = WebDriverWait( self.browser, 5)
        # Search Google Search button by Tag name
        self.browser.find_element(By.NAME, "btnK").click()

        # sleep(5)

    @classmethod
    def tearDownClass(cls):
        # closes the chrome session
        cls.browser.quit()
