import unittest
from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service


class AlertDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        sleep(2)

    # Go to https://chercher.tech/practice/practice-pop-ups-selenium-webdriver and click on alert and click ok
    def test01_simple_alert(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")
        sleep(5)

        # Locate the element and switch to the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        sleep(2)
        # Opens an alertbox()
        alert = driver.switch_to.alert
        sleep(5)

        # Get the text of the alert
        print("The message on alert is: ", alert.text)

        # clicks 'OK' button
        alert.accept()


    # Go to https://chercher.tech/practice/practice-pop-ups-selenium-webdriver and select the confirmation alert button
    # and cancel the alert
    def test02_confirmation_alert(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")
        sleep(5)

        # Locate the element and switch to the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        sleep(2)
        # Opens an alertbox()
        alert = driver.switch_to.alert
        sleep(5)


        # Get the text of the alert
        print("The message on alert is: ", alert.text)

        # clicks 'X' button
        alert.dismiss()

    # Go to https://chercher.tech/practice/practice-pop-ups-selenium-webdriver and input your firstname in it
    def test03_prompt_alert(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")
        sleep(5)

        # Locate the element and switch to the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        sleep(2)
        # Opens an alertbox()
        alert = driver.switch_to.alert
        sleep(5)


        # Get the text of the alert
        print("The message on alert is: ", alert.text)

        # Input your name in the text box
        alert.send_keys("Alexander")

        # clicks OK button
        alert.accept()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
