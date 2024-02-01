import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

TARGET_PRICE = 100
user_agent = os.environ.get("USER_AGENT")
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HEADERS = {
    "User-Agent": f"{user_agent} "
                  "Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}


def get_item(url: str, headers: {} = None) -> (str, float):
    """Get page, parse page, return (name, price)"""
    if headers is None:
        headers = {}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    product_name = soup.select_one(selector="#title").get_text()
    price = soup.select_one(selector=".a-price")
    price_whole = ''.join(
        n for n in price.select_one(selector=".a-price-whole").get_text() if n.isdigit())
    price_fraction = price.select_one(selector=".a-price-fraction").get_text()

    price_float = float(price_whole) + float(price_fraction) / 100
    return product_name, price_float


def send_email(product_name: str, price: float, url: str):
    host = os.environ.get("HOST")
    port = int(os.environ.get("PORT"))
    from_addr = os.environ.get("FROM_ADDR")
    to_addr = os.environ.get("TO_ADDR")
    msg = f"""
FROM: {from_addr}
TO: {to_addr}
Subject: Product Price Alert

{product_name} is now ${price}.\nBuy now at {url}
""".encode("utf-8")
    smtp = smtplib.SMTP(host=host, port=port)
    smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg)


name, current_price = get_item(URL)

if TARGET_PRICE > current_price:
    print(f"Target price {TARGET_PRICE} is more than current price {current_price} = BUY")
    send_email(name, current_price, URL)
else:
    print(f"Target price {TARGET_PRICE} is less than current price {current_price} = WAIT")
