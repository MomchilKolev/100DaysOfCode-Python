import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
LAT = os.environ.get("LAT")
LONG = os.environ.get("LONG")

# Email, not SMS
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
FROM_ADDR = os.environ.get("FROM_ADDR")
TO_ADDR = os.environ.get("TO_ADDR")
RAIN_ALERT_EMAIL = f"""\
FROM: {FROM_ADDR}
TO: {TO_ADDR}
Subject: Rain Expected


It's expected to rain in the next 12 hours. Bring an umbrella =]
"""

params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
data = response.json()

# If any condition in next 12 hours is under 700, bring an umbrella
if any([True for item in data["list"] if item["weather"][0]["id"] < 700]):
    print("Bring an umbrella")
    smtp = smtplib.SMTP(host=HOST, port=PORT)
    smtp.sendmail(from_addr=FROM_ADDR, to_addrs=TO_ADDR, msg=RAIN_ALERT_EMAIL)
else:
    print("No rain in sight")
