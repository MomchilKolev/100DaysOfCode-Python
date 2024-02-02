from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium'
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS Selectors
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a:first-child")
print(article_count.text)
# article_count.click()

# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# Find the "Search" input by Name
search = driver.find_element(By.NAME, value="search")

# Send keyboard input from Selenium
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()