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
    # to input your email id and submit the page and user credentials will get generated
    def test_multiple_windows_input(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/popup.php")
        sleep(5)

        # Find the link test and Click on it
        driver.find_element(By.LINK_TEXT, "Click Here").click()
        print("The main website is: ", driver.current_url)
        sleep(5)

        # Get all window handles
        handler = driver.window_handles

        # Get the number of window opened
        size = len(handler)


        # Write the logic for working with multiple windows as per stated in the problem
        for x in range(size):
            if handler[x] != driver.current_window_handle:
                driver.switch_to.window(handler[x])
                print(driver.current_window_handle)
                print("The website on second tab", driver.current_url)
                sleep(5)
                driver.find_element(By.NAME, "emailid").send_keys("abc@gmail.com")
                sleep(5)
                driver.find_element(By.NAME, "btnLogin").click()
                sleep(5)

                print("The website after clicking on second tab", driver.current_url)
                driver.switch_to.window(handler[x])
                driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) p:nth-child(13) > a:nth-child(1)").click()
                sleep(5)
                driver.close()
                break


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
