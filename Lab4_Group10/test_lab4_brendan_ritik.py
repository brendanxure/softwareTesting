##########################################################################
# Names:        Brendan Obilo
#               Ritik Sharma
# Reg No:       100952871
#               100952840
# Description:  A program that automatically open Chrome browser, navigates
#               searches for body fat calculator site and calculates the body fat
#               of male and female gender with the provided test case given.
# Type of Document: Lab 4 Group 10
# Date:         06/07/2024
##########################################################################

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class TestLab4brendanritik:
    def setup_method(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_lab4_brendan_ritik(self):
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")

        # Wait until the page is loaded
        WebDriverWait(self.driver, 10).until(
          ec.presence_of_element_located((By.NAME, "cage"))
        )

        self.vars["optSel"] = "F"
        if self.driver.execute_script("return (arguments[0] === \"F\")", self.vars["optSel"]):
            # Choose the female gender
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2)").click()
            # enter the required values for calculation of body fat
            self.driver.find_element(By.NAME, "cage").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "cage").clear()
            self.driver.find_element(By.NAME, "cage").send_keys("40")
            self.driver.find_element(By.NAME, "cweightkgs").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "cweightkgs").clear()
            self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
            self.driver.find_element(By.ID, "cheightmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "cheightmeter").clear()
            self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
            self.driver.find_element(By.ID, "cneckmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "cneckmeter").clear()
            self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
            self.driver.find_element(By.ID, "cwaistmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "cwaistmeter").clear()
            self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
            self.driver.find_element(By.ID, "chipmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "chipmeter").clear()
            self.driver.find_element(By.ID, "chipmeter").send_keys("100")
            # click the calculate button to get result
            time.sleep(1)
            self.driver.find_element(By.NAME, "x").click()
            self.vars["result"] = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
            print("Female Body Fat")
            print("{}".format(self.vars["result"]))
        elif self.driver.execute_script("return (arguments[0] === \"M\")", self.vars["optSel"]):
            # choose the male gender
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
            # enter the required values for calculation of body fat
            self.driver.find_element(By.NAME, "cage").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "cage").clear()
            self.driver.find_element(By.NAME, "cage").send_keys("15")
            self.driver.find_element(By.NAME, "cweightkgs").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "cweightkgs").clear()
            self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
            self.driver.find_element(By.ID, "cheightmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "cheightmeter").clear()
            self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
            self.driver.find_element(By.ID, "cneckmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "cneckmeter").clear()
            self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
            self.driver.find_element(By.ID, "cwaistmeter").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "cwaistmeter").clear()
            self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
            time.sleep(1)
            self.driver.find_element(By.NAME, "x").click()
            self.vars["result"] = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
            print("Male Body Fat")
            print("{}".format(self.vars["result"]))


if __name__ == "__main__":
    test = TestLab4brendanritik()
    test.setup_method()
    try:
        test.test_lab4_brendan_ritik()
    finally:
        test.teardown_method()
