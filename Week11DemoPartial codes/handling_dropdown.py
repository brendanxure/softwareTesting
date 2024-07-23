import unittest
from time import sleep

from selenium import webdriver

# Import the "Select" package.
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

class DropDownDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        sleep(2)

    # Go to http://demo.guru99.com/test/newtours/register.php and select ANTARCTICA from dropdown list by
    # using index method
    def test01_drop_down_index(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/test/newtours/register.php")
        sleep(5)

        # Using Select class for selecting value from dropdown
        s_list = Select(driver.find_element(By.NAME, "country"))

        # Select Antarctica by index
        s_list.select_by_index(6)

        # You can assert the value of the element too
        self.assertEqual("ANTARCTICA", s_list.first_selected_option.text)
        sleep(5)

    # Go to http://demo.guru99.com/test/newtours/register.php and select AUSTRIA from dropdown list by
    # using value method
    def test02_drop_down(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/test/newtours/register.php")
        sleep(5)

        # Using Select class for selecting value from dropdown
        s_list = Select(driver.find_element(By.NAME, "country"))

        # Select AUSTRIA by value
        s_list.select_by_value("AUSTRIA")
          # Change the selection to lowercase and see the test failing
        sleep(5)

    # Go to http://demo.guru99.com/test/newtours/register.php and select BAHAMAS from dropdown list by
    # using visible_text method
    def test03_drop_down(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://demo.guru99.com/test/newtours/register.php")
        sleep(5)

        # Using Select class for selecting value from dropdown
        s_list = Select(driver.find_element(By.NAME, "country"))

        # Select BAHAMAS by visible text
        s_list.select_by_visible_text("BAHAMAS")
        sleep(5)

    # We can also use the selectByVisibleText()  method in selecting multiple options in a multi SELECT
    # element. As an example, we will take http://jsbin.com/osebed/2 (http://jsbin.com/osebed/2)
    # as the base URL. It contains a drop-down box that allows multiple selections at a time.
    def test04_drop_down(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://output.jsbin.com/osebed/2")
        sleep(5)

        # Using Select class for selecting value from dropdown
        s_list = Select(driver.find_element(By.ID, "fruits"))

        # Select Orange and index 3 from drop down list
        s_list.select_by_visible_text("Orange")
        s_list.select_by_index(3)

        # deselects all previously selected options
        s_list.deselect_all()

        # Get all options and print the text of all elements from the dropdown list
        all_elements = s_list.options
        print("The values present in the drop down lists are: ")

        for element in all_elements:
            print(element)

        sleep(5)

    # Go to http://jsbin.com/osebed/2 (http://jsbin.com/osebed/2), select Apple from the drop down list and
    # assert its text
    def test05_drop_down_assert(self):
        # Create the object driver
        driver = self.driver

        # Get the application
        driver.get("http://output.jsbin.com/osebed/2")
        sleep(5)

        # Using Select class for selecting value from dropdown
        s_list = Select(driver.find_element(By.ID, "fruits"))

        # Get Apple by visible_text
        s_list.select_by_visible_text("Apple")

        # Assert the value of Apple
        self.assertEqual("Apple", s_list.first_selected_option.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
