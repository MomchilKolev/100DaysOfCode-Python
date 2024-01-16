import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 43.233601
MY_LONG = 27.918762
MY_TIMEZONE_IDENTIFIER = "Europe/Sofia"

HOSTNAME = "localhost"
PORT = 1025
FROM_ADDR = "first@man.pizza"
TO_ADDR = "second@man.pizza"
EMAIL = f"""\
FROM: {FROM_ADDR}
TO: {TO_ADDR}
Subject: International Space Station Overhead Notifier


The International Space Station (ISS) is currently overhead and visible. Look up!"""


def iss_overhead(my_location_tuple):
    """Check if ISS is currently above with 5deg margin -> True/False"""
    # Your position is within +5 or -5 degrees of the ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # iss_latitude = 40
    # iss_longitude = 30

    if (my_location_tuple[0] + 5 >= iss_latitude >= my_location_tuple[0] - 5) and (
            my_location_tuple[1] + 5 >= iss_longitude >= my_location_tuple[1] - 5):
        return True
    return False


def is_night():
    """Is it night at your location -> True/False"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "tzId": MY_TIMEZONE_IDENTIFIER,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    # current_hour = 4

    return True if current_hour < sunrise or current_hour > sunset else False


def iss_overhead_notifier():
    """If it is night and ISS is visible from your location
    send an email"""
    # If the ISS is close to my current position
    # and it is currently dark
    if iss_overhead((MY_LAT, MY_LONG)) and is_night():
        print("ISS OVERHEAD NOW")
        # Then email me to tell me to look up
        with smtplib.SMTP(host=HOSTNAME, port=PORT) as connection:
            connection.set_debuglevel(1)
            connection.sendmail(from_addr=FROM_ADDR, to_addrs=TO_ADDR, msg=EMAIL)
    else:
        print("ISS NOT CURRENTLY VISIBLE OVERHEAD")


# BONUS: run the code every 60 seconds
while True:
    time.sleep(60)
    iss_overhead_notifier()
