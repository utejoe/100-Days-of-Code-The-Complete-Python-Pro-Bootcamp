from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Selenium WebDriver (make sure you have chromedriver installed and in PATH)
driver = webdriver.Chrome()

try:
    # Navigate to the webpage containing upcoming events
    driver.get("https://example.com/upcoming-events")

    # Find all event dates
    event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')
    print("Event Times:")
    for time in event_times:
        print(time.text)

    # Find all event names
    event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
    print("\nEvent Names:")
    for name in event_names:
        print(name.text)

    # Create events dictionary
    events = {}
    for n in range(len(event_times)):
        events[n] = {'time': event_times[n].text, 'name': event_names[n].text}

    # Print the events dictionary
    print("\nEvents Dictionary:")
    print(events)

finally:
    # Close the browser window
    driver.quit()
