import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2.5)

# TODO: Get Cookie
# TODO: Click on Cookie
cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")


def click_on_cookie(cookie):
    cookie.click()


# TODO: Time 5s
# TODO: Find most expensive upgrade
def buy_upgrade():
    if random.randint(0, 5) == 5:
        products = driver.find_elements(By.CSS_SELECTOR, value="#store #upgrades .upgrade.enabled")
    else:
        products = driver.find_elements(By.CSS_SELECTOR, value="#store #products .product.enabled")
    if not products:
        return
    products[-1].click()
    return buy_upgrade()


def cookies_per_second():
    cookies = driver.find_element(By.CSS_SELECTOR, value="#cookiesPerSecond")
    return f"cookies/second: {cookies.text.split(': ')[1]}"


def play():
    try:
        play_time = time.time() + 5 * 60  # 5 minutes from now
        timeout = time.time() + 5  # 5 seconds from now
        while True:
            if time.time() > play_time:
                print(cookies_per_second())
                driver.quit()
                break
            if time.time() > timeout:
                buy_upgrade()
                timeout = time.time() + 5
            click_on_cookie(cookie)
    except StaleElementReferenceException:
        pass
    except BaseException:
        pass


# TODO: Remove cookie consent
driver.execute_script("""
document.querySelector(".fc-consent-root").remove()
document.querySelector("#darken").remove()
""")

# TODO: Buy upgrade
play()
