##########################################################################
# Name:         Brendan Obilo
#               Ritik Sharma
# Reg No:       100952871
#               100952840
# Description:  A program that automatically open Chrome browser, navigates
#               to a shopping site and filters a dress according to given
#               description, then adds to cart and checks out.
# Type of Document: Lab 5 Group 5
# Date:         26/07/2024
##########################################################################

# Selenium and Unitest imports
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# The class that contains the test automation from Selenium IDE
class TestLab5brendanritik(unittest.TestCase):
    @classmethod
    # The start of the class and opens chrome and maximize it
    def setUpClass(cls):
        service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        sleep(2)

    # First test case that navigates to the site and selects the dress
    def test_lab5_01(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(3) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(3) > .text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(2) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(4) > .swatch-option").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(8) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(2) > a > .price:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(4) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active .item:nth-child(3) > a").click()
        print("Selected Product Successfully")

    # Second test case that adds it to the cart
    def test_lab5_02(self):
        product_frame = self.driver.find_element(By.CSS_SELECTOR, ".product-item-info")
        action = ActionChains(self.driver)
        action.move_to_element(product_frame).perform()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".tocart")))
        self.driver.find_element(By.CSS_SELECTOR, ".tocart").click()
        condition_to_wait = ec.visibility_of_element_located((By.CSS_SELECTOR, ".message-success"))
        (WebDriverWait(self.driver, 10).until(condition_to_wait))
        print('Added to Cart Successfully')

    # Third test case that check out the cart
    def test_lab5_03(self):
        self.driver.find_element(By.CSS_SELECTOR, ".showcart").click()
        self.driver.find_element(By.ID, "top-cart-btn-checkout").click()
        (WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".opc-block-summary > .title"))))
        element = self.driver.find_element(By.CSS_SELECTOR, ".opc-block-summary > .title")
        assert element.text == "Order Summary"
        print(f'{element.text} is Successful')

    # The End of the class
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
