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
        # Navigate to javatpoint
        self.browser.get('https://www.javatpoint.com/')

        self.browser.execute_script("window.scrollTo(0,880)")
        WebDriverWait(self.browser, 2).until(
            ec.presence_of_element_located(
                (By.XPATH, "//div[@id='city']/table/tbody/tr/td/fieldset[2]/div[2]/a[2]/div"))
        )
        self.browser.find_element(By.XPATH,
                                  "//div[@id='city']/table/tbody/tr/td/fieldset[2]/div[2]/a[2]/div").click()

    @classmethod
    def tearDownClass(cls):
        # closes the chrome session
        cls.browser.quit()
