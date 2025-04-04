from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ProductListingPage:
    def __init__(self, driver):
        self.driver = driver
        self.min_price_filter = (By.XPATH, "//input[@placeholder='Min']")
        self.max_price_filter = (By.XPATH, "//input[@placeholder='Max']")
        self.first_product = (By.XPATH, "(//a[contains(@class,'_1fQZEK')])[1]")

    def apply_price_filter(self, min_price, max_price):
        self.driver.find_element(*self.min_price_filter).send_keys(str(min_price))
        max_price_input = self.driver.find_element(*self.max_price_filter)
        max_price_input.send_keys(str(max_price))
        max_price_input.send_keys(Keys.RETURN)
        time.sleep(3)

    def select_first_product(self):
        product = self.driver.find_element(*self.first_product)
        product_name = product.text
        product.click()
        return product_name
