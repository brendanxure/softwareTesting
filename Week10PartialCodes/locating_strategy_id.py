""" Locator Strategies using selenium webdriver with python

1.Import WebDriver from selenium.
2.Maximize the browser window.
3.Open the Facebook.com
4.Perform Valid and invalid test cases
5. Assert the error texts
7.Close the Browser.
Follow the unit test framework with fixtures- setUpClass(),tearDownClass() and test methods
"""
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# from webdriver_manager.chrome import ChromeDriverManager


class FacebookTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setting the property for chromedriver.exe
        service = Service(executable_path="chromedriver.exe")
        cls.browser = webdriver.Chrome(service=service)
        cls.browser.maximize_window()
        sleep(2)

    def test_01_page_locator_id_invalidlogin(self):
        # Navigate to Facebook
        self.browser.get('https://www.facebook.com/')

        # Search & Enter the Email or Phone field & Enter Password
        self.browser.find_element(By.ID, "email").send_keys("ctopher22@hotmail.com")
        # Enter the right username
        self.browser.find_element(By.ID, "pass").send_keys("Topher213")
        # Enter the incorrect password
        # Introduced sleep just to check the browser behaviour, not needed everytime
        sleep(5)
        # Click Login
        self.browser.find_element(By.NAME, "login").click()

        WebDriverWait(self.browser, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "_9ay7"))
        )

        # check and assert for error message
        element = self.browser.find_element(By.CLASS_NAME, "_9ay7")
        # Print the actual text to debug
        actual_text = element.text
        print(f"Actual text: '{actual_text}'")
        assert element.text == "The password that you've entered is incorrect.\nForgotten password?"


       # Here in order to execute the 2nd test case, either you should be taking back to login page
        sleep(5)
        self.browser.back()


    def test_02_page_locator_id_validlogin(self):
        # Navigate to Facebook
        self.browser.get('https://www.facebook.com/')

        # Search & Enter the Email or Phone field & Enter Password(wrong)
        self.browser.find_element(By.ID, "email").send_keys("ctopher22@hotmail.com")
        # Enter the right username
        self.browser.find_element(By.ID, "pass").send_keys("Topher213")
        sleep(5)

        # Click Login
        self.browser.find_element(By.NAME, "login").click()


        #check and assert for successful case
        self.assertIn("Facebook", self.browser.title)
        sleep(5)


    @classmethod
    def tearDownClass(cls):
        # closes the chrome session
        cls.browser.quit()
