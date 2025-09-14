from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver - SIMPLIFIED VERSION without webdriver-manager
# Specify the path to chromedriver directly
service = Service()  # This will use the chromedriver from your PATH if available

# Alternative: If you want to specify the exact path to chromedriver
# service = Service(r'C:\path\to\chromedriver.exe')

driver = webdriver.Chrome(service=service)

try:
    print("Navigating to website...")
    driver.get("https://www.saucedemo.com/v1/")
    
    print("Logging in...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Wait for inventory page to load
    print("Waiting for page to load...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    
    # Add first product to cart
    print("Adding product to cart...")
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    # Give it a moment to update
    time.sleep(2)
    
    # Verify cart count updated
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1", f"Expected cart count 1, but got {cart_count}"
    
    print("✅ Test passed: Product successfully added to cart")
    
finally:
    print("Closing browser...")
    driver.quit()
    print("Test completed!")