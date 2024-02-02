from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium'
options.add_argument('--headless')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# driver.get("https://ossinsight.io")
# entries = driver.find_elements(By.CSS_SELECTOR, ".MuiTableRow-root span")
# entry = driver.find_elements(By.XPATH, '/html/body/div/div[4]/div[2]/main/section[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/span/a[1]')
# print(entry)

# Scrape Python Event Dates
driver.get("https://www.python.org/")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li")
event_dict = {}
for i, event in enumerate(events):
    time, name = event.text.split('\n')
    event_dict[i] = { "time": time, "name": name}
print(event_dict)

driver.quit()