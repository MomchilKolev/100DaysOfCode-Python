import os

import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
url = os.environ.get("URL")
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(1)

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

def sign_in():
    # Get and click on sign in button
    sign_in_button = driver.find_element(By.CSS_SELECTOR,
                                         value=".nav__cta-container .nav__button-secondary")
    sign_in_button.click()

    time.sleep(1)

    # Get input fields
    username_input = driver.find_element(By.CSS_SELECTOR, value="#username")
    password_input = driver.find_element(By.CSS_SELECTOR, value="#password")

    # Input Credentials
    username_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(1)

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = \
    driver.find_elements(by=By.CSS_SELECTOR, value=".artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


def save_job():
    try:
        name = driver.find_element(By.CSS_SELECTOR,
                                   value=".job-details-jobs-unified-top-card__job-title-link")
        print(name.text)
        time.sleep(1)
        save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
        save_button.click()
    except BaseException as error:
        print("Save job error: ", error)


def apply_to_job():
    # Easy Apply
    easy_apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button")
    easy_apply_button.click()
    time.sleep(1)

    try:
        # Handle next
        # next_button = driver.find_element(By.CSS_SELECTOR, "[data-easy-apply-next-button]")
        # next_button.click()
        #
        # time.sleep(.5)
        # review_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Review your "
        #                                                            "application']")
        # review_button.click()

        # time.sleep(.5)
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            value="[aria-label='Submit application']")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()
            
        time.sleep(2)
        # Click close button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
    except BaseException as error:
        print("Error", error)


def next_page():
    next = driver.find_element(By.CSS_SELECTOR, value=".jobs-search-results-list__pagination "
                                                      ".active + li")
    if next:
        next.click()
        each_page()


def each_page():
    time.sleep(1)
    # # Get jobs
    jobs_list = driver.find_elements(By.CSS_SELECTOR,
                                     value=".jobs-search-results-list ul li.jobs-search-results__list-item")

    # For each job
    for job in jobs_list:
        print(job)
        job.click()
        time.sleep(1.5)

        # Save
        # save_job()

        # Apply
        # apply_to_job()

    next_page()


sign_in()

each_page()
