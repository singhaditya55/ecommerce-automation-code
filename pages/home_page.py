from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.close_popup_button = (By.XPATH, "//button[contains(text(),'✕')]")

    def open_homepage(self, url):
        self.driver.get(url)

    def close_login_popup(self):
        try:
            self.driver.find_element(*self.close_popup_button).click()
        except:
            print("Login popup not displayed.")

    def search_product(self, product_name):
        search = self.driver.find_element(*self.search_box)
        search.send_keys(product_name)
        search.send_keys(Keys.RETURN)
