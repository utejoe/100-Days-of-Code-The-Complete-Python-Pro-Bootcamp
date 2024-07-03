from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup Selenium WebDriver (ensure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

try:
    # Navigate to the form page
    driver.get("https://example.com/signup")

    # Find input fields by name
    first_name = driver.find_element(By.NAME, 'fName')
    last_name = driver.find_element(By.NAME, 'lName')
    email = driver.find_element(By.NAME, 'email')

    # Fill in the form fields
    first_name.send_keys("John")
    last_name.send_keys("Doe")
    email.send_keys("john.doe@example.com")

    # Find and click the Sign Up button
    sign_up_button = driver.find_element(By.CSS_SELECTOR, 'form button')
    sign_up_button.click()

finally:
    # Close the browser window
    driver.quit()
