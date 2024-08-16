# Name:         Brendan Obilo
#               Ritik Sharma
#               Amisha Gharti Magar
#               Surakshya Pokharel
#               Mehak kapur
# Reg No:       100952871
#               100952840
#               100944725
#               100951538
#               100951743
# Description:  A program that automatically open Chrome browser, navigates
#               to a demo Banking Site and test all required fields to confirm required result
#               with actual result
# Type of Document: Group 5 Project
# Date:         15/08/2024
##########################################################################

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TestGroup5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method is called once before all tests are executed. It initializes the WebDriver instance.
        print("setUpClass")
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def test_NC1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Get the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Get the new customer link by link text and click
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        print("\nTest NC1 : Name cannot be empty")
        # Get the name input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message")
        # print the actual result gotten
        print(f"Actual result NC1: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Customer name must not be blank"

    def test_NC2(self):
        sleep(2)
        print("\nTest NC2: Name cannot be numeric")
        # Get the name input element by xpath and clear input then input 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").send_keys("1234")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message")
        # print the actual result gotten
        print(f"Actual result NC2_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"
        # Get the name input element by xpath and clear input then input name123
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").send_keys("name123")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message")
        # print the actual result gotten
        print(f"Actual result NC2_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"

    def test_NC3(self):
        sleep(2)
        print("\nTest NC3: Name cannot have special characters")
        # Get the name input element by xpath and clear input then input name!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").send_keys("name!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message")
        # print the actual result gotten
        print(f"Actual result NC3_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the name input element by xpath and clear input then input !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").send_keys("!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message")
        # print the actual result gotten
        print(f"Actual result NC3_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NC4(self):
        sleep(2)
        print("\nTest NC4: Name cannot have first character as blank space")
        # Get the name input element by xpath and clear input an empty space as first character
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'name\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message")
        # print the actual result gotten
        print(f"Actual result NC4: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character can not have space"

    def test_NC5(self):
        sleep(2)
        print("\nTest NC5: Address cannot be empty")
        # Get the address input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//textarea[@name=\'addr\']").click()
        self.driver.find_element(By.XPATH, "//textarea[@name=\'addr\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message3")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message3")
        # print the actual result gotten
        print(f"Actual result NC5: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "ADDRESS Field must not be blank"

    def test_NC6(self):
        sleep(2)
        print("\nTest NC6: Address cannot have first blank space")
        # Get the address input element by xpath and clear then put the first character as a blank space
        self.driver.find_element(By.XPATH, "//textarea[@name=\'addr\']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@name=\'addr\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message3")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message3")
        # print the actual result gotten
        print(f"Actual result NC6: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character can not have space"

    def test_NC7(self):
        sleep(2)
        print("\nTest NC7: City cannot be empty")
        # Get the city input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result NC7: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "City Field must be not blank"

    def test_NC8(self):
        sleep(2)
        print("\nTest NC8: City cannot be numeric")
        # Get the city input element by xpath and clear the input field, then input 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("1234")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result NC8_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"
        # Get the city input element by xpath and clear the input field, then input city123
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("city123")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result NC8_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"

    def test_NC9(self):
        sleep(2)
        print("\nTest NC9: City cannot have special character")
        # Get the city input element by xpath and clear the input field, then input City!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("City!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result NC9_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the city input element by xpath and clear the input field, then input !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result NC9_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NC_10(self):
        sleep(2)
        print("\nTest NC10: City cannot have first blank space")
        # Get the city input element by xpath and clear the input field, then input first character as blank space
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result NC10: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character can not have space"

    def test_NC_11(self):
        sleep(2)
        print("\nTest NC11: State cannot be empty")
        # Get the state input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result NC11: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "State must not be blank"

    def test_NC_12(self):
        sleep(2)
        print("\nTest NC12: State cannot be numeric")
        # Get the state input element by xpath and clear the input field, then input 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("1234")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result NC12_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"
        # Get the state input element by xpath and clear the input field, then input State123
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("State123")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result NC12_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"

    def test_NC_13(self):
        sleep(2)
        print("\nTest NC13: State cannot have special character")
        # Get the state input element by xpath and clear the input field, then input State!@#"
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("State!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result NC13_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the state input element by xpath and clear the input field, then input !@#"
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result NC13_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NC_14(self):
        sleep(2)
        print("\nTest NC14: State cannot have first blank space")
        # Get the state input element by xpath and clear the input field, then input !@#"
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result NC14: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character cannot have space"

    def test_NC_15(self):
        sleep(2)
        print("\nTest NC15: PIN must be numeric")
        # Get the pin input element by xpath and clear the input field, then input 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("1234")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC15_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"
        # Get the pin input element by xpath and clear the input field, then input 1234PIN
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("1234PIN")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC15_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_NC_16(self):
        sleep(2)
        print("\nTest NC16: PIN cannot be empty")
        # Get the pin input element by xpath and clear the input field, then press TAB Key
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC16: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "PIN code must not be blank"

    def test_NC_17(self):
        sleep(2)
        print("\nTest NC17: PIN must have 6 digits")
        # Get the pin input element by xpath and clear the input field, then input 12
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("12")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC17_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "PIN Code must have 6 Digits"
        # Get the pin input element by xpath and clear the input field, then input 123
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("123")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC17_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "PIN Code must have 6 Digits"

    def test_NC_18(self):
        sleep(2)
        print("\nTest NC18: PIN cannot have special character")
        # Get the pin input element by xpath and clear the input field, then input !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC18_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the pin input element by xpath and clear the input field, then input 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("123!@#")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC18_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NC_19(self):
        sleep(2)
        print("\nTest NC19: PIN cannot have first blank space")
        # Get the pin input element by xpath and clear the input field, then first blank space
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC19: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character cannot have space"

    def test_NC_20(self):
        sleep(2)
        print("\nTest NC20: PIN cannot have blank space")
        # Get the pin input element by xpath and clear the input field, then blank space
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result NC20: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_NC_21(self):
        sleep(2)
        print("\nTest NC21: Mobile number cannot be empty")
        # Get the telephone input element by xpath and clear the input field, then press TAB Key
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result NC21: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Mobile no must not be blank"

    def test_NC_22(self):
        sleep(2)
        print("\nTest NC22: Mobile number Telephone cannot have first character as blank space")
        # Get the telephone input element by xpath and clear the input field, then input first character blank space
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result NC22: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character can not have space"

    def test_NC_23(self):
        sleep(2)
        print("\nTest NC23: Mobile number cannot have spaces")
        # Get the telephone input element by xpath and clear the input field, then input 123 123
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("123 123")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result NC23: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_NC_24(self):
        sleep(2)
        print("\nTest NC24: Mobile number cannot have special character")
        # Get the telephone input element by xpath and clear the input field, then input 886636!@12
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("886636!@12")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result NC24_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the telephone input element by xpath and clear the input field, then input !@88662682
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("!@88662682")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result NC24_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the telephone input element by xpath and clear the input field, then input 88663682!@
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("88663682!@")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result NC24_03: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NC_25(self):
        sleep(2)
        print("\nTest NC25: Email cannot be empty")
        # Get the email input element by xpath and click the input field, then Press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC25: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email ID must not be blank"

    def test_NC_26(self):
        sleep(2)
        print("\nTest NC26: Email must be in correct format")
        # Get the email input element by xpath and clear the input field, then input guru99@gmail
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("guru99@gmail")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC26_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear the input field, then input guru99
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("guru99")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC26_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear the input field, then input Guru99@
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("Guru99@")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC26_03: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear the input field, then input guru99@gmail.
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("guru99@gmail.")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC26_04: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear the input field, then input guru99gmail.com
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("guru99gmail.com")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC26_05: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"

    def test_NC_27(self):
        sleep(2)
        print("\nTest NC27: Email cannot have space")
        # Get the email input element by xpath and clear the input field, then input blank space
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys(" ")
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result NC27: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"

    def test_NC_28(self):
        sleep(2)
        print("\nTest NC28: Password cannot be empty")
        # Get the password input element by xpath and clear the input field and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'password\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys(Keys.TAB)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message18")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message18")
        # print the actual result gotten
        print(f"Actual result NC28: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Password must not be blank"

    def test_EC1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Get the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        self.driver.find_element(By.NAME, "password").click()
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Get the Edit customer link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        print("\nTest EC1: Customer id cannot be empty")
        # Get the customer ID input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result EC1 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Customer ID is required"

    def test_EC2(self):
        sleep(2)
        print("\nTest EC2: Customer id must be numeric")
        # Get the customer ID input element by xpath and clear then input 1234Acc
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("1234Acc")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result EC2_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"
        # Get the customer ID input element by xpath and clear then input Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("Acc123")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result EC2_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_EC3(self):
        sleep(2)
        print("\nTest EC3: Customer id cannot have special character")
        # Get the customer ID input element by xpath and clear then input 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result EC3_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the customer ID input element by xpath and clear then input !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result EC3_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_EC4(self):
        sleep(2)
        print("\nTest EC4: Valid Customer Id")
        # Get the customer ID input element by xpath and clear then input valid customer ID
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("60854")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(
          ec.presence_of_element_located((By.XPATH, "//p[contains(.,\'Edit Customer\')]")))
        # Get the error message element by ID
        element = self.driver.find_element(By.XPATH, "//p[contains(.,\'Edit Customer\')]")
        # print the actual result gotten
        print(f"Actual result EC4 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Edit Customer"

    def test_EC5(self):
        sleep(2)
        print("\nTest EC5: Address cannot be empty")
        # Get the address input element by xpath and clear then press the TAB key
        self.driver.find_element(By.XPATH, "//textarea[@name=\'addr\']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@name=\'addr\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message3")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message3")
        # print the actual result gotten
        print(f"Actual result EC5 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Address Field must be blank"

    def test_EC6(self):
        sleep(2)
        print("\nTest EC6: City cannot be empty")
        # Get the address city element by xpath and clear then press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result EC6 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "City Field must not be blank"

    def test_EC7(self):
        sleep(2)
        print("\nTest EC7: City cannot be numeric")
        # Get the city input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("1234")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result EC7_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are allowed"
        # Get the city input element by xpath and clear then type city123
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("city123")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result EC7_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are allowed"

    def test_EC8(self):
        sleep(2)
        print("\nTest EC8: City cannot have special character")
        # Get the city input element by xpath and clear then type City!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("City!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        element = self.driver.find_element(By.ID, "message4")
        print(f"Actual result EC8_01 is: {element.text}")
        assert element.text == "Special characters are not allowed"
        # Get the city input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'city\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message4")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message4")
        # print the actual result gotten
        print(f"Actual result EC8_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_EC9(self):
        sleep(2)
        print("\nTest EC9: state cannot be empty")
        # Get the state input element by xpath and clear then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result EC9 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "State must be blank"

    def test_EC_10(self):
        sleep(2)
        print("\nTest EC10: State cannot be numeric")
        # Get the state input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("1234")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result EC10_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"
        # Get the state input element by xpath and clear then type State123
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("State123")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result EC10_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Numbers are not allowed"

    def test_EC_11(self):
        sleep(2)
        print("\nTest EC11: State cannot have special character")
        # Get the state input element by xpath and clear then type State!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("State!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result EC11_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the state input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'state\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message5")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message5")
        # print the actual result gotten
        print(f"Actual result EC11_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_EC_12(self):
        sleep(2)
        print("\nTest EC12: PIN must be numeric")
        # Get the pin input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("1234")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC12_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"
        # Get the pin input element by xpath and clear then type 1234PIN
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("1234PIN")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC12_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_EC_13(self):
        sleep(2)
        print("\nTest EC13: PIN cannot be empty")
        # Get the pin input element by xpath and clear then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC13 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "PIN Code must not be blank"

    def test_EC_14(self):
        sleep(2)
        print("\nTest EC14: PIN must have 6 digits")
        # Get the pin input element by xpath and clear then type 1234567
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("1234567")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC14_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "PIN Code must have 6 Digits"
        # Get the pin input element by xpath and clear then type 123
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("123")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC14_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "PIN Code must have 6 Digits"

    def test_EC_15(self):
        sleep(2)
        print("\nTest EC15: PIN cannot have special character")
        # Get the pin input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC15_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the pin input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'pinno\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message6")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message6")
        # print the actual result gotten
        print(f"Actual result EC15_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_EC_16(self):
        sleep(2)
        print("\nTest EC16: Mobile No. cannot be empty")
        # Get the mobile number input element by xpath and clear then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result EC16 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Telephone no must not be blank"

    def test_EC_17(self):
        sleep(2)
        print("\nTest EC17: Mobile No. cannot have special character")
        # Get the mobile number input element by xpath and clear then type 886636!@12
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("886636!@12")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result EC17_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the mobile number input element by xpath and clear then type !@88662682
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("!@88662682")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result EC17_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the mobile number input element by xpath and clear then type 88663682!@
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'telephoneno\']").send_keys("88663682!@")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message7")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message7")
        # print the actual result gotten
        print(f"Actual result EC17_03 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_EC_18(self):
        sleep(2)
        print("\nTest EC18: Email cannot be empty")
        # Get the email input element by xpath and clear then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result EC18 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID must not be blank"

    def test_EC_19(self):
        sleep(2)
        print("\nTest EC19: Email must be in format career@guru99.com")
        # Get the email input element by xpath and clear then type guru99@gmail
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("guru99@gmail")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result EC19_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear then type guru99
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("guru99")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result EC19_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear then type Guru99@
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("Guru99@")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result EC19_03 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"
        # Get the email input element by xpath and clear then type gurugmail.com
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'emailid\']").send_keys("gurugmail.com")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message9")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message9")
        # print the actual result gotten
        print(f"Actual result EC19_04 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Email-ID is not valid"

    def test_EC_20(self):
        sleep(2)
        print("\nTest EC20: After every update ")
        # Get the submit button element and click it
        self.driver.find_element(By.NAME, "sub").click()
        sleep(2)
        # Switch to the alert box
        alert = self.driver.switch_to.alert
        # To print the message from the alert box
        print(f"Actual error EC_20 is: {alert.text}")
        try:
            # Assert the text on the alert box with the message provided
            assert alert.text == "Update done successfully"
            # Click ok on the alert box
            alert.accept()
        except AssertionError:
            # If assert fails, catch the error and click ok on the alert box
            alert.accept()
            # raise the alert error to record the testcase as failed
            raise

    def test_DC1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Get the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        print("\n Test DC1: Customer ID cannot be empty")
        # Get the Delete customer link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        # Get the customer ID input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC1: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Customer ID can not be blank"

    def test_DC2(self):
        sleep(2)
        print("\n Test DC2: Customer ID must be numeric")
        # Get the customer ID input element by xpath and clear input then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("1234")
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC2_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"
        # Get the customer ID input element by xpath and clear input then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("Acc123")
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC2_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_DC3(self):
        sleep(2)
        print("\n Test DC3: Customer ID cannot have special character")
        # Get the customer ID input element by xpath and clear input then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123!@#")
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC3_01: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the customer ID input element by xpath and clear input then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("!@#")
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC3_02: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_DC4(self):
        sleep(2)
        print("\n Test DC4: Customer ID cannot have blank space")
        # Get the customer ID input element by xpath and clear input then type 123 12 and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC4: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_DC5(self):
        sleep(2)
        print("\n Test DC5: First Character cannot be space")
        # Get the customer ID input element by xpath and clear input then first character a space, and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(1)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result DC5: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character cannot have space"

    def test_DC6(self):
        sleep(2)
        print("\n Test DC6: Incorrect Customer ID")
        # Get the customer ID input element by xpath and clear input then type 123456, and click submit
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123456")
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        sleep(2)
        # switch to an alert box that a if you want to delete the customer
        alert_1 = self.driver.switch_to.alert
        # click ok to delete the customer
        alert_1.accept()
        sleep(2)
        # switch to another alert box for further information
        alert_2 = self.driver.switch_to.alert
        # print the actual result gotten
        print(f"Actual result DC6 is: {alert_2.text}")
        try:
            # Assert the text on the alert box element with the message provided
            assert alert_2.text == "Customer does not exist!!"
            # click ok
            alert_2.accept()
        except AssertionError:
            # catch assertion error if assertion fails
            # click ok to remove alert box
            alert_2.accept()
            # raise error to read as failed
            raise

    def test_DC7(self):
        sleep(2)
        print("\n Test DC7: Correct Customer ID")
        # Get the customer ID input element by xpath and clear input then type correct customer ID, and click submit
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("58625")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        # switch to an alert box that a if you want to delete the customer
        alert_1 = self.driver.switch_to.alert
        # click ok to delete the customer
        alert_1.accept()
        sleep(2)
        # switch to another alert box for further information
        alert_2 = self.driver.switch_to.alert
        # print the actual result gotten
        print(f"Actual result DC7 is: {alert_2.text}")
        try:
            # Assert the text on the alert box element with the message provided
            assert alert_2.text == ("Customer does not existcould not be deleted!! First delete all"
                                    " accounts of this customer then delete the customer")
            # click ok
            alert_2.accept()
        except AssertionError:
            # catch assertion error if assertion fails
            # click ok to remove alert box
            alert_2.accept()
            # raise error to read as failed
            raise

    def test_DC8(self):
        sleep(2)
        print("\n Test DC8: Reset Button")
        # Get the customer ID input element by xpath and clear input then type qwer and click reset
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("qwer")
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        sleep(1)
        # Get the customer input text box
        text_box = self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']")
        # Print the value of the value on the text box
        print(f"Actual error DC8_01 is: {text_box.text}")
        # Assert the text on the text box element with the message provided
        assert text_box.text == ""
        # Get the customer ID input element by xpath and clear input then type 123456 and click reset
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123456")
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        sleep(1)
        # Get the customer input text box
        text_box = self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']")
        # Print the value of the value on the text box
        print(f"Actual error DC8_02 is: {text_box.text}")
        # Assert the text on the text box element with the message provided
        assert text_box.text == ""

    def test_NA1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Get the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Get the new Account link by link text and click
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        print("\nTest NA1: Customer id cannot be empty")
        # Get the customer ID input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA1 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Customer ID is required"

    def test_NA2(self):
        sleep(2)
        print("\nTest NA2: Customer id must be numeric")
        # Get the customer ID input element by xpath and clear then type 1234Acc
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("1234Acc")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA2_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"
        # Get the customer ID input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("Acc123")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA2_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_NA3(self):
        sleep(2)
        print("\nTest NA3: Customer id cannot have special character")
        # Get the customer ID input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA3_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the customer ID input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA3_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NA4(self):
        sleep(2)
        print("\nTest NA4: Customer id cannot have blank space")
        # Get the customer ID input element by xpath and clear then type 123 12 and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA4 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_NA5(self):
        sleep(2)
        print("\nTest NA5: First Character cannot be space")
        # Get the customer ID input element by xpath and clear then type First character as space and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message14")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message14")
        # print the actual result gotten
        print(f"Actual result NA5 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character cannot have space"

    def test_NA6(self):
        sleep(2)
        print("\nTest NA6: Cannot be empty")
        # Get the initial deposit input element by xpath and click then press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA6 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Initial Deposit must not be blank"

    def test_NA7(self):
        sleep(2)
        print("\nTest NA7: Must be numeric")
        # Get the initial deposit input element by xpath and clear then type 1234Acc
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("1234Acc")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA7_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"
        # Get the initial deposit input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("Acc123")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA7_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Characters are not allowed"

    def test_NA8(self):
        sleep(2)
        print("\nTest NA8: Cannot have special character")
        # Get the initial deposit input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA8_01 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"
        # Get the initial deposit input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA8_02 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NA9(self):
        sleep(2)
        print("\nTest NA9: Initial Deposit cannot have blank space")
        # Get the initial deposit input element by xpath and clear then type 123 12 then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA9 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "Special characters are not allowed"

    def test_NA_10(self):
        sleep(2)
        print("\nTest NA10: First Character cannot be space")
        # Get the initial deposit input element by xpath and clear then first character as space and then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 seconds to time out or until the error element is located by ID
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message19")))
        # Get the error message element by ID
        element = self.driver.find_element(By.ID, "message19")
        # print the actual result gotten
        print(f"Actual result NA10 is: {element.text}")
        # Assert the text on the error message element with the message provided
        assert element.text == "First character cannot have space"

    def test_NA_11(self):
        sleep(2)
        print("\nTest NA11: Savings Account Type")
        # Get the select account dropdown element by xpath and click
        self.driver.find_element(By.XPATH, "//select[@name=\'selaccount\']").click()
        # Select the drop down element and select the value "Savings"
        dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
        dropdown.select_by_value("Savings")
        # Get the value of the select account drop down
        value = self.driver.find_element(By.NAME, "selaccount").get_attribute("value")
        # print the actual value gotten
        print(f"Actual result NA11 is: {value}")
        # Assert the actual value with the value provided
        assert value == "Savings"

    def test_NA_12(self):
        sleep(2)
        print("\nTest NA12: Current Account Type")
        # Get the select account dropdown element by xpath and click
        self.driver.find_element(By.XPATH, "//select[@name=\'selaccount\']").click()
        # Select the drop down element and select the value "Current"
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Current']").click()
        # Get the value of the select account drop down
        value = self.driver.find_element(By.XPATH, "//select[@name=\'selaccount\']").get_attribute("value")
        # print the actual value gotten
        print(f"Actual result NA12 is: {value}")
        # Assert the actual value with the value provided
        assert value == "Current"

    def test_NA_13(self):
        sleep(2)
        print("\nTest NA13: Reset Button")
        # Get the customer ID input element by xpath and clear then type qwer
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("qwer")
        # Get the initial deposit input element by xpath and clear then type qwer
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("qwer")
        # Get the reset button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'reset\']").click()
        # Get the customer ID input element by xpath
        customer_id_element = self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']")
        # Get the initial deposit input element by xpath
        deposit_element = self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']")
        # print the actual value gotten in customer ID element input field
        print(f"Actual result NA13_01 is: {customer_id_element.text}")
        # print the actual value gotten in initial deposit input field
        print(f"Actual result NA13_01 is: {deposit_element.text}")
        # Assert the actual value with the value provided
        assert customer_id_element.text == ""
        # Assert the actual value with the value provided
        assert deposit_element.text == ""
        # Get the customer ID input element by xpath and clear then type 123456
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123456")
        # Get the initial deposit input element by xpath and clear then type 123456
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("123456")
        # Get the reset button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'reset\']").click()
        # Get the customer ID input element by xpath
        customer_id_element = self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']")
        # Get the initial deposit input element by xpath
        deposit_element = self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']")
        # print the actual value gotten in customer ID element input field
        print(f"Actual result NA13_02 is: {customer_id_element.text}")
        # print the actual value gotten in initial deposit input field
        print(f"Actual result NA13_02 is: {deposit_element.text}")
        # Assert the actual value with the value provided
        assert deposit_element.text == ""
        # Assert the actual value with the value provided
        assert customer_id_element.text == ""

    def test_NA_14(self):
        sleep(2)
        print("\nTest NA14: Incorrect Customer ID")
        # Get the customer ID input element by xpath and clear then type 123456
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("123456")
        sleep(2)
        # Get the submit button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'button2\']").click()
        sleep(2)
        # switch to the alert box
        alert = self.driver.switch_to.alert
        # print the actual result gotten on the alert box
        print(f"Actual result NA14 is: {alert.text}")
        try:
            # Assert the actual value with the value provided
            assert alert.text == "Customer does not exist!!"
            # Click ok to close alert box
            alert.accept()
        except AssertionError:
            # Click ok to close alert box
            alert.accept()
            # Raise error to mark as failed
            raise

    def test_NA_15(self):
        sleep(2)
        print("\nTest NA15: Correct Customer ID and correct amount")
        # Get the customer ID input element by xpath and clear then type valid customer ID
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'cusid\']").send_keys("60854")
        # Get the initial deposit input element by xpath and clear then type  a correct amount
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'inideposit\']").send_keys("1000")
        # Get the submit button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'button2\']").click()
        sleep(2)
        # Wait for 10 seconds to time out or for the header element indicating it is successful
        WebDriverWait(self.driver, 10).until(
          ec.presence_of_element_located((By.XPATH, "//p[contains(.,\'Account Generated Successfully!!!\')]")))
        # Get header element by xpath that indicates the account was generated successfully
        element = self.driver.find_element(By.XPATH, "//p[contains(.,\'Account Generated Successfully!!!\')]")
        # Print actual result gotten from the element
        print(f"Actual result NA15 is: {element.text}")
        # Assert the text on the element with provided expected output
        assert element.text == "Account Generated Successfully!!!"

    def test_NA_16(self):
        sleep(2)
        print("\nTest NA16: click on Continue")
        # Get the "continue" link element by link text and click
        self.driver.find_element(By.LINK_TEXT, "Continue").click()
        sleep(2)
        # Wait for 10 seconds to time out or for the element that indicates the manager welcome page
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//marquee")))
        # Get the element in the manager welcome page
        element = self.driver.find_element(By.XPATH, "//marquee")
        # Print actual result gotten from the element
        print(f"Actual result NA16 is: {element.text}")
        # Assert the text on the element with provided expected output
        assert element.text == "Welcome To Manager's Page of Guru99 Bank"

    def test_EA1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Get the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        print("\nTest EA1: Account number cannot be empty")
        # Get the Edit Account link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Get the account number input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").click()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(Keys.TAB)
        # Wait for 10sec to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual result EA1: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == 'Account Number must not be empty'

    def test_EA2(self):
        sleep(2)
        print("\nTest EA2: Account number must be numeric")
        # Get the account number input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("1234")
        # Wait for 10sec to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual EA2_01 result: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"
        # Get the account number input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("Acc123")
        # Wait for 10 sec to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual EA2_02 result: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_EA3(self):
        sleep(2)
        print("\nTest EA3: Account number cannot have special character")
        # Get the account number input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("123!@#")
        # Wait for 10sec to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual EA3_01 result: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"
        # Get the account number input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("!@#")
        # Wait for 10 sec to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual EA3_02 result: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"

    def test_EA4(self):
        sleep(2)
        print("\nTest EA4: Account number cannot have blank space")
        # Get the account number input element by xpath and clear then type 123 12 and press TAB key
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(Keys.TAB)
        # Wait for 10 sec to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual EA4 result: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_EA5(self):
        sleep(2)
        print("\nTest EA5: First Character cannot be space")
        # Get the account number input element by xpath and clear then enter first character blank and press TAB key
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys(Keys.TAB)
        # Wait for 10 secs to timeout or for element message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result message
        print(f"Actual EA5 result: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "First character can not have space"

    def test_EA6(self):
        sleep(2)
        print("\nTest EA6: Valid Account Number")
        # Find the account number input element by xpath and clear then type a valid account number
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("136467")
        sleep(2)
        # Find the account submit button by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        sleep(2)
        # Print the actual result from the page title
        print(f"Actual result EA6: {self.driver.title}")
        # Assert the actual result to the expected result
        assert self.driver.title == "Edit Account Form"

    def test_EA7(self):
        sleep(2)
        print("\nTest EA7: InValid Account Number")
        self.driver.back()
        # Find the account number input element by xpath and clear then type an invalid account number
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("12345")
        # Find the account submit button by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
        sleep(2)
        # Switch to the alert box that pops up
        alert = self.driver.switch_to.alert
        sleep(2)
        # Print the actual result from the alert box
        print(f"Actual result EA7: {alert.text}")
        try:
            # assert the text on the alert box to the expected result
            assert alert.text == "Account does not exist"
            # Click ok to close the alert box
            alert.accept()
        except AssertionError:
            # catch the error and click ok to close the alert box
            alert.accept()
            # raise the error to fail the test case
            raise

    def test_EA8(self):
        sleep(2)
        print("\nReset Button")
        # Find the account number input element by xpath and clear then type qwer
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("qwer")
        # Find the reset button by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name='res']").click()
        sleep(2)
        # Find the account number input element by xpath and get the value of the element
        element = self.driver.find_element(By.XPATH, "//input[@name='accountno']")
        # Print the actual result
        print(f"Actual result EA8_01: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == ""
        # Find the account number input element by xpath and clear then type 123456
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='accountno']").send_keys("123456")
        # Find the reset button by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name='res']").click()
        # Find the account number input element by xpath and get the value of the element
        element = self.driver.find_element(By.XPATH, "//input[@name='accountno']")
        # Print the actual result
        print(f"Actual result EA8_02: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == ""

    def test_DA1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Find the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Find the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Find the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Get the Delete account link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        print("\nTest Case DA1: Account number cannot be empty")
        # Get the account number input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA1 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "Account Number must not be blank"

    def test_DA2(self):
        sleep(2)
        print("\nTest Case DA2: Account number must be numeric")
        # Find the account number input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("1234")
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA2_01 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "Characters are not allowed"
        # Find the account number input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("Acc123")
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA2_02 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "Characters are not allowed"

    def test_DA3(self):
        sleep(2)
        print("\nTest Case DA3: Account number cannot have special character")
        # Find the account number input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123!@#")
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA3_01 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "Special characters are not allowed"
        # Find the account number input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("!@#")
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA3_02 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "Special characters are not allowed"

    def test_DA4(self):
        sleep(2)
        print("\nTest Case DA4: Account number cannot have blank space")
        # Find the account number input element by xpath and clear then type 123 12 then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA4 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "Characters are not allowed"

    def test_DA5(self):
        sleep(2)
        print("\nTest Case DA5: First Character cannot be space")
        # Find the account number input element by xpath and clear then type first character blank then press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # find element by ID with error message
        element = self.driver.find_element(By.ID, "message2")
        # print actual result from the element by ID for error message
        print(f"Actual result DA5 is: {element.text}")
        # Assert the actual result with the expected result
        assert element.text == "First character cannot have space"

    def test_DA6(self):
        sleep(2)
        print("\nTest Case DA6: Valid Account Number")
        # Find the account number input element by xpath and clear then type a valid account
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("136727")
        # Find the submit button element by Xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        # switch to alert box to confirm if you really want to delete account
        alert = self.driver.switch_to.alert
        # Click ok to close the alert box
        alert.accept()
        try:
            # look for another alert box that confirms delete
            message = self.driver.switch_to.alert
            # Print the actual result
            print(f"Actual result DA6 is: {message.text}")
            # Assert the actual result with the expected result
            assert message.text == "Account deleted successfully"
            # Click ok to close the alert box
            message.accept()
        except Exception as e:
            # Print error encountered
            print(f"Actual result DA6 is: {e}")
            # Assert false to fail the test as error has been caught
            assert False

    def test_DA7(self):
        # Move the window tab back to continue the delete account process
        self.driver.back()
        sleep(2)
        print("\nTest Case DA7: InValid Account Number")
        # Find the account number input element by xpath and clear then type an invalid account
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("12345")
        # Find the submit button element by Xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        # switch to alert box to confirm if you really want to delete account
        alert = self.driver.switch_to.alert
        # Click ok to close the alert box
        alert.accept()
        # look for another alert box that confirms delete
        message = self.driver.switch_to.alert
        # Print the actual result
        print(f"Actual result DA7 is: {message.text}")
        try:
            # Assert the actual result with the expected result
            assert message.text == "Account does not exist"
            # Click ok to close the alert box
            message.accept()
        except AssertionError:
            # Click ok to close the alert box after error has been caught
            message.accept()
            # raise error to fail the test because error has been caught
            raise

    def test_DA8(self):
        sleep(2)
        print("\nTest Case DA8: Reset Button")
        # Find the account number input element by xpath and clear then type qwer
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("qwer")
        # Find the reset button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        # Find the account number input element by xpath and get the value
        element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # Print the actual result
        print(f"Actual result DA8_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == ""
        # Find the account number input element by xpath and clear then type 123456
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123456")
        # Find the reset button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        # Find the account number input element by xpath and get the value
        element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # Print the actual result
        print(f"Actual result DA8_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == ""

    def test_BE1(self):
        sleep(2)
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Find the login manager ID element by name and input the correct ID
        self.driver.find_element(By.XPATH, "//input[@name=\'uid\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'uid\']").send_keys("mngr584309")
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.XPATH, "//input[@name=\'password\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.XPATH, "//input[@name=\'btnLogin\']").click()
        # Get the Balance Enquiry link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        print("\nTest BE1: Account number cannot be empty")
        # Find the account number input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual error BE1 is: {element.text}")
        # Assert the actual result and expected result
        assert element.text == "Account Number must not be blank"

    def test_BE2(self):
        sleep(2)
        print("\nTest BE2: Account number must be numeric")
        # Find the account number input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("1234")
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual error BE2_01 is: {element.text}")
        # Assert the actual result and expected result
        assert element.text == "Characters are not allowed"
        # Find the account number input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("Acc123")
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual error BE2_02 is: {element.text}")
        # Assert the actual result and expected result
        assert element.text == "Characters are not allowed"

    def test_BE3(self):
        sleep(2)
        print("\nTest BE3: Account number cannot have special character")
        # Find the account number input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123!@#")
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual error BE3_01 is: {element.text}")
        # Assert the actual result and expected result
        assert element.text == "Special characters are not allowed"
        # Find the account number input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("!@#")
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual error BE3_02 is: {element.text}")
        # Assert the actual result and expected result
        assert element.text == "Special characters are not allowed"

    def test_BE4(self):
        sleep(2)
        print("\nTest BE4: First Character cannot be space")
        # Find the account number input element by xpath and clear then First character be blank the press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        # wait for 10 secs to timeout or to find element by ID with the error message
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual error BE4 is: {element.text}")
        # Assert the actual result and expected result
        assert element.text == "First character cannot have space"

    def test_BE5(self):
        sleep(2)
        print("\nTest BE5: Valid Account Number")
        # Find the account number input element by xpath and clear then enter valid account number
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("136467")
        # Find submit button element and click
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        sleep(2)
        # Print actual result of the page title
        print(f"Actual error BE5 is: {self.driver.title}")
        # Assert actual result to validate the expected result
        assert self.driver.title != "demo.guru99.com"

    def test_BE6(self):
        sleep(2)
        print("\nTest BE6: InValid Account Number")
        # Go back on the window tab to remove error page
        self.driver.back()
        # Find the account number input element by xpath and clear then enter an invalid account number
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("12345")
        # Find submit button element and click
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        sleep(2)
        # switch to the alert box
        alert = self.driver.switch_to.alert
        # Print actual result of the alert box
        print(f"Actual error BE6 is: {alert.text}")
        try:
            # Assert the actual result to expected result
            assert alert.text == "Account does not exist"
            # Click ok to remove the alert box
            alert.accept()
        except AssertionError:
            # Click ok to remove the alert box after error has been caught
            alert.accept()
            # Raise error to fail test after error has been caught
            raise

    def test_BE7(self):
        sleep(2)
        print("\nTest BE7: Reset Button")
        # Find the account number input element by xpath and clear then enter qwer
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("qwer")
        # Find reset button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        sleep(1)
        # Find the account number input element by xpath and get value
        element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # Print the actual result
        print(f"Actual error BE7_01 is: {element.text}")
        # assert actual result to expected result
        assert element.text == ""
        # Find the account number input element by xpath and clear then enter 123456
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123456")
        # Find reset button element by xpath and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        sleep(1)
        # Find the account number input element by xpath and get value
        element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # Print the actual result
        print(f"Actual error BE7_02 is: {element.text}")
        # Assert actual result to expected result
        assert element.text == ""

    def test_MS1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Get the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Get the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Get the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Get the mini statement link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        print("\nTest MS1: Account number cannot be empty")
        # Get the account input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the element by ID with the error message
        element = self.driver.find_element(By.ID, "message2")
        # print the actual message
        print(f"Actual result MS1 is: {element.text}")
        # Assert the actual message to the expected message
        assert element.text == "Account Number must not be blank"

    def test_MS2(self):
        sleep(2)
        print("\nTest MS2: Account number must be numeric")
        # Get the account input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("1234")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find element with the error message by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual result MS2_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"
        # Find the account number input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("Acc123")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find element with the error message by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual result MS2_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_MS3(self):
        sleep(2)
        print("\nTest MS3: Account number cannot have special character")
        # Find the account number input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find element with the error message by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual result MS3_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"
        # Find the account number input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find element with the error message by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual result MS3_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"

    def test_MS4(self):
        sleep(2)
        print("\nTest MS4: Account number cannot have blank space")
        # Find the account number input element by xpath and clear then type 123 12 and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find element with the error message by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual result MS4 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_MS5(self):
        sleep(2)
        print("\nTest MS5: First Character cannot be space")
        # Find the account number input element by xpath and clear, then a first character blank and press the TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find element with the error message by ID
        element = self.driver.find_element(By.ID, "message2")
        # Print the actual result
        print(f"Actual result MS5 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "First character cannot have space"

    def test_MS6(self):
        sleep(2)
        print("\nTest MS6: Valid Account Number")
        # Find the account number input element by xpath and clear, then type a valid account
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("136727")
        # Find submit button element and click
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        try:
            # Click the title of the page
            print(f"{self.driver.title}")
            # Wait for 10 sec to timeout or for the element by ID containing the error message is present
            table = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.TAG_NAME, "table")))
            print(f"Actual result MS5 is: Table showing statement")
            # if there is a table element in the page
            if table:
                # pass test
                assert True
            # Go back to the previous page
            self.driver.back()
        except Exception as e:
            # Go back to the previous page after catching error
            self.driver.back()
            # print the error caught
            print(f"Actual result MS5 is: {e}")
            # Assert False to fail the result
            assert False

    def test_MS7(self):
        sleep(2)
        print("\nTest MS7: InValid Account Number")
        # Find the account number input element by xpath and clear, then type an invalid account
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("12345")
        # Find submit button element and click
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        sleep(2)
        # Switch to the alert box
        alert = self.driver.switch_to.alert
        # Print actual result from the alert box
        print(f"Actual result MS7 is: {alert.text}")
        try:
            # Assert the actual result to the expected result
            assert alert.text == "Account does not exist"
            # click ok to close the alert box
            alert.accept()
        except AssertionError:
            # click ok to close the alert box after error has been caught
            alert.accept()
            # raise error to fail test case
            raise

    def test_MS8(self):
        sleep(2)
        print("\nTest MS8: Reset Button")
        # Find the account number input element by xpath and clear, then type qwer
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("qwer")
        # Find reset button element and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        # Find the account number input element by xpath and get the current value
        element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # print the actual result
        print(f"Actual result MS8_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == ""
        # Find the account number input element by xpath and clear, then type 123456
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123456")
        # Find reset button element and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        # Find the account number input element by xpath and get the current value
        element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # print the actual result
        print(f"Actual result MS8_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == ""

    def test_CS1(self):
        # To navigate to the site websites
        self.driver.get("https://demo.guru99.com/V4/")
        # Find the login manager ID element by name and input the correct ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr584309")
        # Find the login password element by name and input the correct ID
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("dEtAbud")
        # Find the submit button element by name and click submit
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Find the customised statement link by link text and click
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        print("\nTest CS1: Account number cannot be empty")
        # Get the account input element by xpath and click then press tab key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS1 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Account Number must not be blank"

    def test_CS2(self):
        sleep(2)
        print("\nTest CS2: Account number must be numeric")
        # Find the account input element by xpath and clear then type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("1234")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS2_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"
        # Find the account input element by xpath and clear then type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("Acc123")
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS2_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_CS3(self):
        sleep(2)
        print("\nTest CS3: Account number cannot have special character")
        # Find the account input element by xpath and clear then type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS3_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"
        # Find the account input element by xpath and clear then type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS3_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"

    def test_CS4(self):
        sleep(2)
        print("\nTest CS4: Account number cannot have blank space")
        # Find the account input element by xpath and clear then type 123 12 and press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS4 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_CS5(self):
        sleep(2)
        print("\nTest CS5: First Character cannot be space")
        # Find the account input element by xpath and clear then first character is a space and press TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message2")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message2")
        # print the actual result
        print(f"Actual result CS5 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "First character cannot have space"

    def test_CS6(self):
        sleep(2)
        print("\nTest CS6: click on the date field")
        # Find the calendar input element and click without selecting any date
        self.driver.find_element(By.XPATH, "//input[@name=\'fdate\']").click()
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message26")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message26")
        # print the actual result
        print(f"Actual result CS6 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "From Date Field must not be blank"

    def test_CS7(self):
        sleep(2)
        print("\nTest CS7: click on the date field")
        # Find the calendar input element and click without selecting any date
        self.driver.find_element(By.XPATH, "//input[@name=\'tdate\']").click()
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message27")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message27")
        # print the actual result
        print(f"Actual result CS7 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "From Date Field must not be blank"

    def test_CS8(self):
        sleep(2)
        print("\nTest CS8: Minimum Transaction Value must be numeric")
        # Find the minimum transaction value input element, clear and type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("1234")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message12")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message12")
        # print the actual result
        print(f"Actual result CS8_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"
        # Find the minimum transaction value input element, clear and type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("Acc123")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message12")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message12")
        # print the actual result
        print(f"Actual result CS8_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_CS9(self):
        sleep(2)
        print("\nTest CS9: Minimum Transaction Value cannot have special character")
        # Find the minimum transaction value input element, clear and type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message12")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message12")
        # print the actual result
        print(f"Actual result CS9_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"
        # Find the minimum transaction value input element, clear and type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message12")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message12")
        # print the actual result
        print(f"Actual result CS9_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Special characters are not allowed"

    def test_CS_10(self):
        sleep(2)
        print("\nTest CS10: Minimum Transaction Value cannot have blank space")
        # Find the minimum transaction value input element, clear and type 123 12 and enter TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message12")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message12")
        # print the actual result
        print(f"Actual result CS10 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_CS_11(self):
        sleep(2)
        print("\nTest CS11: First Character cannot be space")
        # Find the minimum transaction value input element, clear and type first character blank and enter TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message12")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message12")
        # print the actual result
        print(f"Actual result CS11 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "First character cannot have space"

    def test_CS_12(self):
        sleep(2)
        print("\nTest CS12: Number of transaction must be numeric")
        # Find the Number of transaction value input element, clear and type 1234
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("1234")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message13")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message13")
        # print the actual result
        print(f"Actual result CS12_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"
        # Find the Number of transaction value input element, clear and type Acc123
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("Acc123")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message13")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message13")
        # print the actual result
        print(f"Actual result CS12_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_CS_13(self):
        sleep(2)
        print("\nTest CS13: Number of transaction have special character")
        # Find the Number of transaction value input element, clear and type 123!@#
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("123!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message13")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message13")
        # print the actual result
        print(f"Actual result CS13_01 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Number of Transaction cannot have special character"
        # Find the Number of transaction value input element, clear and type !@#
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("!@#")
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message13")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message13")
        # print the actual result
        print(f"Actual result CS13_02 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Number of Transaction cannot have special character"

    def test_CS_14(self):
        sleep(2)
        print("\nTest CS14: Number of transaction cannot have blank space")
        # Find the Number of transaction value input element, clear and type 123 12 and enter TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("123 12")
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message13")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message13")
        # print the actual result
        print(f"Actual result CS14 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "Characters are not allowed"

    def test_CS_15(self):
        sleep(2)
        print("\nTest CS15: First Character cannot be space")
        # Find the Number of transaction value input element, clear and type First Character blank and enter TAB key
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys(Keys.TAB)
        sleep(2)
        # Wait for 10 sec to timeout or for the element by ID containing the error message is present
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "message13")))
        # Find the error message element by ID
        element = self.driver.find_element(By.ID, "message13")
        # print the actual result
        print(f"Actual result CS15 is: {element.text}")
        # Assert the actual result to the expected result
        assert element.text == "First character cannot have space"

    def test_CS_16(self):
        sleep(2)
        print("\nTest CS16: Reset Button")
        # Find the account number value input element, clear and type an account number
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("136727")
        # Find the element for from date, click and select a valid date
        self.driver.find_element(By.XPATH, "//input[@name=\'fdate\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'fdate\']").send_keys("2024-08-09")
        # Find the element for to date, click and select a valid date
        self.driver.find_element(By.XPATH, "//input[@name=\'tdate\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'tdate\']").send_keys("2024-08-07")
        # Find the element for minimum transaction value, clear and enter an amount
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("100")
        # Find the element for number of transaction value, clear and enter a value
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("2")
        # Find the element for reset button and click
        self.driver.find_element(By.XPATH, "//input[@name=\'res\']").click()
        # Find the account number value input element
        account_number_element = self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']")
        # Print the actual result for account number
        print(f"Actual result CS16_01 is: {account_number_element.text}")
        # Assert the actual result to the expected result
        assert account_number_element.text == ""
        # Find the for date value input element
        for_date_element = self.driver.find_element(By.XPATH, "//input[@name=\'fdate\']")
        for_date_value = for_date_element.get_attribute("value")
        # Print the actual result for date value
        print(f"Actual result CS16_02 is: {for_date_value}")
        # Assert the actual result to the expected result
        assert for_date_value == ""
        # Find the to date value input element
        to_date_element = self.driver.find_element(By.XPATH, "//input[@name=\'tdate\']")
        to_date_value = to_date_element.get_attribute("value")
        # Print the actual result for to date value
        print(f"Actual result CS16_03 is: {to_date_value}")
        # Assert the actual result to the expected result
        assert to_date_value == ""
        # Find the minimum transaction value input element
        minimum_value_element = self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']")
        # Print the actual result on minimum transaction
        print(f"Actual result CS16_04 is: {minimum_value_element.text}")
        # Assert the actual result to the expected result
        assert minimum_value_element.text == ""
        # Find the number of transaction by Xpath and get the value
        transaction_number_element = self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']")
        # Print the actual result for number for transaction
        print(f"Actual result CS16_05 is: {transaction_number_element.text}")
        # Assert the actual result to the expected result
        assert transaction_number_element.text == ""

    def test_CS_17(self):
        sleep(2)
        print("\nTest CS17: Verify Submit Button")
        # Find element for account ID by Xpath and clear then input an account number
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'accountno\']").send_keys("136727")
        # Find element for date by Xpath and clear then input the date
        self.driver.find_element(By.XPATH, "//input[@name=\'fdate\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'fdate\']").send_keys("2024-08-06")
        # Find element to date by Xpath and clear then input the date
        self.driver.find_element(By.XPATH, "//input[@name=\'tdate\']").click()
        self.driver.find_element(By.XPATH, "//input[@name=\'tdate\']").send_keys("2024-08-08")
        # Find the minimum transaction value input element, clear and input a valid value
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'amountlowerlimit\']").send_keys("500")
        # Find the number of transaction value input element, clear and input a valid value
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").clear()
        self.driver.find_element(By.XPATH, "//input[@name=\'numtransaction\']").send_keys("4")
        # Find the element with the submit button and click to submit
        self.driver.find_element(By.XPATH, "//input[@name=\'AccSubmit\']").click()
        sleep(2)
        try:
            # Switch to the alert box
            alert = self.driver.switch_to.alert
            # Print the actual result in the alert box
            print(f"Actual result MS7 is: {alert.text}")
            # Assert actual result to expected result
            assert alert.text == "Please fill all fields"
            # Click ok to close alert box
            alert.accept()
        except Exception as e:
            # Print error message caught
            print(f"The error caught is {str(e).splitlines()[0]}")
            # Go back the previous page in the tab
            self.driver.back()
            # Assert false to fail test case after catching the error
            assert False

    # Called once after all tests have been executed
    @classmethod
    def tearDownClass(cls):
        sleep(2)
        print("teardownClass")
        cls.driver.quit()
