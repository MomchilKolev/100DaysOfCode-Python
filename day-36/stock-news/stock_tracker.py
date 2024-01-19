import os
import smtplib
import requests

from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_URL = "https://newsapi.org/v2/everything?"
NEWS_PAGE_SIZE = 3
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
FROM_ADDR = os.environ.get("FROM_ADDR")
TO_ADDR = os.environ.get("TO_ADDR")


class StockTracker:
    def __init__(self):
        self.stock_api_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": STOCK_API_KEY
        }
        self.news_params = {
            "apiKey": NEWS_API_KEY,
            "q": COMPANY_NAME,
            "pageSize": NEWS_PAGE_SIZE,
            "page": 1
        }

        # Stock data
        self.percent_difference: float = 0
        self.percent_difference_symbol: str = ""

        # Three articles
        self.three_articles: list = []

    # # STEP 1: Use https://www.alphavantage.co
    def get_percent_difference(self):
        # 35 requests/day When STOCK price increase/decreases by 5% between yesterday and the day
        # before yesterday then print("Get News")
        response = requests.get(url=STOCK_ENDPOINT,
                                params=self.stock_api_params)
        response.raise_for_status()
        stock_data = response.json()

        # Don't use datetime, because last working day stored may be older than yesterday
        # Save response before you run out of 35 daily requests
        # with open("stock_data.json", "w") as data_file:
        #     json.dump(data, data_file)
        # Use saved response
        # with open("stock_data.json", "r") as data_file:
        #     stock_data = json.load(data_file)

        days = [value for (key, value) in stock_data['Time Series (Daily)'].items()]
        last_day = float(days[0]['4. close'])
        second_to_last_day = float(days[1]['4. close'])
        difference = abs(round(last_day - second_to_last_day, 2))
        self.percent_difference = (difference / second_to_last_day) * 100.0
        price_increase = last_day > second_to_last_day
        self.percent_difference_symbol = "🔺" if price_increase else "🔻"
        return self.percent_difference

    def get_news(self):
        # # STEP 2: Use https://newsapi.org 100 requests per day Instead of printing ("Get
        # News"), actually get the first 3 news pieces for the COMPANY_NAME.
        response = requests.get(url=NEWS_URL, params=self.news_params)
        response.raise_for_status()
        articles = response.json()["articles"]
        # Save news data
        # with open("news_data.json", "w") as data_file:
        #     json.dump(articles, data_file)
        # Read saved news data
        # with open("news_data.json", "r") as data_file:
        #     articles = json.load(data_file)["articles"]

        self.three_articles = [(article["title"], article["description"]) for article in articles]

    def notify(self):
        # # STEP 3: Use https://www.twilio.com or send an email
        # Send a separate message with the
        # percentage change and each article's title and description to your phone number.
        news_string = '\n'.join([f"Headline: {article[0]}\nBrief: {article[1]}" for article in (
            self.three_articles)])
        msg = f"""\
FROM: {FROM_ADDR}
TO: {TO_ADDR}
Subject: Stock Changes
    
    
{STOCK}: {self.percent_difference_symbol} {self.percent_difference}
{news_string}
        """
        smtp = smtplib.SMTP(host=HOST, port=PORT)
        smtp.sendmail(from_addr=FROM_ADDR, to_addrs=TO_ADDR, msg=msg)

        # Optional: Format the SMS message like this:
        """TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent 
        investors are required to file by the SEC The 13F filings show the funds' and investors' 
        portfolio positions as of March 31st, near the height of the coronavirus market crash. or 
        "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: 
        We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent 
        investors are required to file by the SEC The 13F filings show the funds' and investors' 
        portfolio positions as of March 31st, near the height of the coronavirus market crash."""
