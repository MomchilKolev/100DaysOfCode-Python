from dotenv import load_dotenv
import os
from smtplib import SMTP

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    @classmethod
    def send_notification(cls, message):
        FROM_ADDR = os.environ.get("FROM_ADDR")
        TO_ADDR = os.environ.get("TO_ADDR")
        HOST = os.environ.get("HOST")
        PORT = int(os.environ.get("PORT"))
        msg = f"""
FROM: {FROM_ADDR}
TO: {TO_ADDR}
Subject: Low Price Alert!


{message}
"""
        smtp = SMTP(host=HOST, port=PORT)
        smtp.sendmail(from_addr=FROM_ADDR, to_addrs=TO_ADDR, msg=msg)