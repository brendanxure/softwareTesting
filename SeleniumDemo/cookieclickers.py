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

# Open the Cookie clicker homepage
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Define IDs and prefixes used in the game
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")))

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()

    # Get the current cookie count
    cookies_count = driver.find_element(By.ID, cookies_id).text
    cookies_count = int(cookies_count.split(" ")[0].replace(",", ""))

    # loop through the first 4 product to check if they can be purchased
    for i in range(4):
        # Get the price of the product
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        # if the price is not a digit(eg. not available), skip to next product
        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        # if the current cookies count is greater than or equal to the product price, by the product
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

    time.sleep(0.1)
