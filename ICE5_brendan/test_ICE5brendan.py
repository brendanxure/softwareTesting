##########################################################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  A program that navigates to http://demo.guru99.com/test/newtours/
#               and creates a user by filling in all the details on the register web page.
#               After creating username and password then it assert the login successful page.
# Type of Document: In class 5
# Date:         18/07/2024
##########################################################################

# import from unitest and selenium
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# The class for the testcases
class TestICE5brendan(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    # Registration test case
    def test_01register(self):
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        self.driver.find_element(By.NAME, "firstName").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("Brendan")
        self.driver.find_element(By.NAME, "lastName").click()
        self.driver.find_element(By.NAME, "lastName").send_keys("Obilo")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("123456789")
        self.driver.find_element(By.ID, "userName").click()
        self.driver.find_element(By.ID, "userName").send_keys("brendan.obilo@xure.com")
        self.driver.find_element(By.NAME, "address1").click()
        self.driver.find_element(By.NAME, "address1").send_keys("Durham College")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("Durham")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "postalCode").click()
        self.driver.find_element(By.NAME, "postalCode").send_keys("D12 K23")
        self.driver.find_element(By.NAME, "country").click()
        dropdown = self.driver.find_element(By.NAME, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'CANADA']").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("brendan")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("brendan")
        self.driver.find_element(By.NAME, "confirmPassword").click()
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("brendan")
        self.driver.find_element(By.NAME, "submit").click()

    # Login test case
    def test_02login(self):
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "userName").click()
        self.driver.find_element(By.NAME, "userName").send_keys("tutorial")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("tutorial")
        self.driver.find_element(By.NAME, "submit").click()

        # check and assert for success message
        element = self.driver.find_element(By.XPATH, "//h3[contains(.,'Login Successfully')]")
        # Print successful message
        print(f"Success: '{element.text}'")
        # asserting the login successful page
        assert element.text == "Login Successfully"


# the main the executes the program
if __name__ == '__main__':
    unittest.main()
