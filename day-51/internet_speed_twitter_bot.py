import os
import time
import requests
import json
import tweepy

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


class InterNetSpeedTwitterBot:
    def __init__(self):
        load_dotenv()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.down = os.environ.get("PROMISED_DOWN")
        self.up = os.environ.get("PROMISED_UP")
        self.driver = webdriver.Chrome(options=options)
        self.speed_test_url = "https://www.speedtest.net/"

        # Twitter
        self.twitter_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        self.twitter_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        self.bearer_token = os.environ.get("BEARER_TOKEN")
        self.twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        self.twitter_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        self.payload = {"text": "Hello world! 2"}
        self.api = {}
        self.auth = {}


    def get_internet_speed(self):
        # TODO: Get Speeds
        print("Opening site")
        self.driver.get(self.speed_test_url)

        # Reject all cookies
        print("Rejecting cookies")
        self.driver.find_element(By.CSS_SELECTOR, value="#onetrust-reject-all-handler").click()

        # Start
        print("Starting test")
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test")
        go_button.click()

        down_speed = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed")

        up_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        while not up_speed.text or up_speed.text == "—":
            print("Waiting for results...")
            time.sleep(5)
            up_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")

        print(f'down is {down_speed.text}')
        print(f'up is {up_speed.text}')


    # def tweet_at_provider(self, tweet="HELLO WORLD!!!!"):
    #     print(self.twitter_consumer_key, self.twitter_consumer_secret)
    #     auth = tweepy.OAuth2AppHandler(
    #         self.twitter_consumer_key, self.twitter_consumer_secret
    #     )
    #     api = tweepy.Client(bearer_token=self.bearer_token,
    #                         consumer_key=self.twitter_consumer_key,
    #                         consumer_secret=self.twitter_consumer_secret,
    #                         access_token=self.twitter_access_token,
    #                         access_token_secret=self.twitter_access_token_secret,
    #                         wait_on_rate_limit=True
    #                         )
    #     api.create_tweet(text="POTATO")




        # self.auth = tweepy.OAuthHandler(self.twitter_consumer_key, self.twitter_consumer_secret)
        #
        # self.auth.set_access_token(
        #     self.twitter_access_token,
        #     self.twitter_access_token_secret
        # )
        #
        # self.api = tweepy.Client(self.auth, wait_on_rate_limit=True)
        #
        # self.api.create_tweet(text="POTATO!")








































        # self.driver.get(self.twitter_url)
        # time.sleep(2)
        #
        # # sign_in_button = self.driver.find_element(By.LINK_TEXT, value="Sign in")
        #
        # # Remove overlays
        # overlay = self.driver.find_element(By.CSS_SELECTOR, value="#layers")
        # if overlay:
        #     self.driver.execute_script("document.querySelector('#layers').remove()")
        #     time.sleep(1)
        #
        # # sign_in_button = self.driver.find_element(By.CSS_SELECTOR, value="a[href='/login']")
        # # sign_in_button2 = self.driver.find_element(By.LINK_TEXT, value="Sign in")
        # # print("si", sign_in_button)
        # # print("si2", self.driver.find_element(By.LINK_TEXT, value="Sign in"))
        # # sign_in_button.click()
        # # if sign_in_button2:
        # #     sign_in_button2.click()
        #
        # # Input email and enter
        # email_input = self.driver.find_element(By.CSS_SELECTOR, value="input[type='text']")
        # email_input.send_keys(self.twitter_email)
        # email_input.send_keys(Keys.ENTER)
        # time.sleep(1)
        # self.action.move_by_offset(10, 20)
        # print(email_input.text)
        #
        # # Input password and enter
        # password_input = self.driver.find_element(By.NAME, value="password")
        # password_input.send_keys(self.twitter_password)
        # password_input.send_keys(Keys.ENTER)
        # self.action.move_by_offset(210, 20)
        # time.sleep(1)
        # exit(0)
        #
        # # Remove overlays
        # overlay = self.driver.find_element(By.CSS_SELECTOR, value="#layers")
        # if overlay:
        #     self.driver.execute_script("document.querySelector('#layers').remove()")
        #     time.sleep(1)
        #
        # # Get editor, add tweet, post tweet
        # editor = self.driver.find_element(By.CSS_SELECTOR, ".DraftEditor-root")
        # if editor:
        #     editor.click()
        #     editor.send_keys("THIS IS OBNOXIOUS!!!")



