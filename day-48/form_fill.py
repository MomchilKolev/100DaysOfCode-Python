from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Get site
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find First Name, Last Name, Email
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Add inputs
first_name.send_keys("Peter")
last_name.send_keys("Pan")
email.send_keys("peter@pan.pizza")

# Send Credentials
email.send_keys(Keys.ENTER)
