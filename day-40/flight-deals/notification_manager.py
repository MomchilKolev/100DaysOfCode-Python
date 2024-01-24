from dotenv import load_dotenv
import os
from smtplib import SMTP
import polars as pl

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    FROM_ADDR = os.environ.get("FROM_ADDR")
    HOST = os.environ.get("HOST")
    PORT = int(os.environ.get("PORT"))
    @classmethod
    def send_notification(cls, message):
        TO_ADDR = os.environ.get("TO_ADDR")
        msg = f"""
FROM: {cls.FROM_ADDR}
TO: {TO_ADDR}
Subject: Low Price Alert!


{message}
"""
        smtp = SMTP(host=cls.HOST, port=cls.PORT)
        smtp.sendmail(from_addr=cls.FROM_ADDR, to_addrs=TO_ADDR, msg=msg)

    @classmethod
    def send_emails(cls, message=""):
        try:
            users = pl.read_csv("../flight-club/users.csv")
        except FileNotFoundError:
            print("Create ../flight-club/users.csv")
        else:
            for user in users.iter_rows():
                email = user[2]
                msg = f"""
FROM: {cls.FROM_ADDR}
TO: {email}
Subject: Low Price Alert!


{message}
"""
                smtp = SMTP(host=cls.HOST, port=cls.PORT)
                smtp.sendmail(from_addr=cls.FROM_ADDR, to_addrs=email, msg=msg)


NotificationManager.send_emails()