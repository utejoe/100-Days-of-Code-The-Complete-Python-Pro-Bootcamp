from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Selenium WebDriver (make sure you have chromedriver installed and in PATH)
driver = webdriver.Chrome()

try:
    # Navigate to Amazon product page
    driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS")

    # Find dollar price element
    price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text

    # Find cents price element
    price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

    # Print the full price
    print(f"The price is ${price_dollar}.{price_cents}")

    # Navigate to Python.org and find search bar element by name
    driver.get("https://www.python.org")
    search_bar = driver.find_element(By.NAME, "q")
    print(f"Search bar tag name: {search_bar.tag_name}")
    print(f"Search bar placeholder: {search_bar.get_attribute('placeholder')}")

    # Find submit button by ID
    submit_button = driver.find_element(By.ID, "submit")
    print(f"Submit button size: {submit_button.size}")

    # Find documentation link by CSS selector
    documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
    print(f"Documentation link text: {documentation_link.text}")

    # Find submit website bug link by XPath
    bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[5]/a')
    print(f"Bug link href: {bug_link.get_attribute('href')}")

finally:
    # Close the browser window
    driver.quit()
