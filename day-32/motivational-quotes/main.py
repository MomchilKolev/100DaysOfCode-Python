import datetime as dt
from random import choice
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as data_file:
    quotes = data_file.readlines()

quote = choice(quotes).strip().encode("utf-8", "ignore")
print(quote)


hostname = "localhost"
port = 1025
from_address = "first@email.xyz"
to_address = "second@email.xyz"
email_message = f"""
From: {from_address}
To: {to_address}
Subject: Motivational Quote


{quote}"""

print(day_of_week)
if day_of_week == 0:
    with smtplib.SMTP(host=hostname, port=port) as connection:
        connection.set_debuglevel(1)
        connection.sendmail(from_addr=from_address, to_addrs=to_address, msg=email_message)