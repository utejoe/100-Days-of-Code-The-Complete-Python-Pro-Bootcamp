from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

driver.close()
# driver.quit