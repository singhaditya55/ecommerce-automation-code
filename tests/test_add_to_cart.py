from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Flipkart
driver.get("https://www.flipkart.com")
driver.maximize_window()
time.sleep(2)

# Close Login Popup (if present)
try:
    close_btn = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_btn.click()
except:
    print("Login popup not displayed.")

# Search for Mobiles
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Mobiles")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Apply Price Filter (₹15,000 - ₹20,000)
min_price = driver.find_element(By.XPATH, "//input[@placeholder='Min']")
min_price.send_keys("15000")

max_price = driver.find_element(By.XPATH, "//input[@placeholder='Max']")
max_price.send_keys("20000")
max_price.send_keys(Keys.RETURN)
time.sleep(3)

# Select First Mobile from the List
first_mobile = driver.find_element(By.XPATH, "(//a[contains(@class,'_1fQZEK')])[1]")
mobile_name = first_mobile.text
first_mobile.click()
time.sleep(3)

# Switch to New Tab
driver.switch_to.window(driver.window_handles[1])

# Add to Cart
add_to_cart_btn = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
add_to_cart_btn.click()
time.sleep(3)

# Proceed to Cart
driver.get("https://www.flipkart.com/viewcart?exploreMode=true")
time.sleep(3)

# Validate the Mobile in Cart
cart_items = driver.find_elements(By.CLASS_NAME, "_2Kn22P")
is_mobile_in_cart = any(mobile_name in item.text for item in cart_items)

if is_mobile_in_cart:
    print("Test Passed: Selected mobile is present in the cart.")
else:
    print("Test Failed: Selected mobile is not in the cart.")

# Close Browser
driver.quit()
