from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the chrome driver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Google homepage
driver.get("https://google.com")

# Wait until the search input field is present on the page
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

input_element.clear()

input_element.send_keys("Professor Topher Youtube" + Keys.ENTER)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Professor Topher")))
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Professor Topher")
link.click()


# wait for 10 seconds to allow page to open
time.sleep(10)

# close the browser
driver.quit()
