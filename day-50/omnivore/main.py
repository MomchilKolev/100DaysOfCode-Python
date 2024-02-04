import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

load_dotenv()

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
with open(".newsletters.json", "r") as data_file:
    newsletters = json.load(data_file)


driver = webdriver.Firefox()

# Load site
driver.get("https://omnivore.app")
time.sleep(2.5)

# Get and click on login
login_button = driver.find_element(By.LINK_TEXT, value="Login")
login_button.click()
time.sleep(1.5)

# Continue with email
continue_with_email_button = driver.find_element(By.CSS_SELECTOR, value="[class*='actionLink']")
continue_with_email_button.click()

# Get inputs
email_input = driver.find_element(By.NAME, value="email")
password_input = driver.find_element(By.NAME, value="password")

# Input credentials
email_input.send_keys(email)
password_input.send_keys(password)

# Login
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(2)

# For each newsletter
for newsletter in newsletters:
    current = driver.find_element(By.CSS_SELECTOR, value=f"[title='{newsletter}")
    print("before current if")
    if current:

        # Click on it
        current.click()
        time.sleep(2)

        # Click on each newsletter edit labels
        xpath = '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]'
        container = driver.find_element(By.XPATH, xpath)
        all_edit_buttons = container.find_elements(
            By.CSS_SELECTOR, value="button[title*='Edit labels (l)']"
        )
        if not all_edit_buttons:
            continue
        time.sleep(2)

        # for each newsletter item open labels
        print("before for")
        labels_modal_xpath = "/html/body/div[4]/div/div"
        for edit_button in all_edit_buttons:
            driver.execute_script("arguments[0].click();", edit_button)
            time.sleep(1)
            labels_modal = driver.find_element(By.XPATH, value=labels_modal_xpath)
            labels = labels_modal.find_elements(By.TAG_NAME, value="label")
            if labels:
                # For each label, if it should be checked but isn't, check it
                for label in labels:
                    if label.text in newsletters[newsletter]:
                        driver.execute_script("arguments[0].click()", label)
                    # print("After if")
                close_button = driver.find_element(By.CSS_SELECTOR, '.xMark')
                try:
                    close_button.click()
                except:
                    close_button.parent.click()
            time.sleep(0.5)
            # break
    # break
    time.sleep(1)
            #     break
            # print(edit_buttons)
            # add labels

# # for edit_label in edit_labels:
# #     edit_label.click()
