##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
from datetime import datetime
import random
import smtplib
import pandas

FROM_ADDRESS = "first@email.pizza"
HOSTNAME = "localhost"
PORT = 1025
now = datetime.now()
today = (now.day, now.month)


def format_email(to_address, content):
    global FROM_ADDRESS
    return f"""\
From: {FROM_ADDRESS}
To: {to_address}
Subject: Happy Birthday!
    
    
{content}
"""


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with
# the person's actual name from birthdays.csv
def send_email(to):
    """Send email to birthday person"""
    name = to.get("name")
    email = to.get("email")
    random_letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter_number}.txt") as data_file:
        letter_template = data_file.read()
        letter = letter_template.replace("[NAME]", name)

    # 4. Send the letter generated in step 3 to that person's email address.
    formatted_email = format_email(email, letter)
    with smtplib.SMTP(host=HOSTNAME, port=PORT) as connection:
        connection.set_debuglevel(1)
        connection.sendmail(from_addr=FROM_ADDRESS, to_addrs=email, msg=formatted_email)


# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv", index_col=None)
[send_email(row[1]) for row in birthdays.iterrows() if (row[1].get("day"), row[1].get("month")) == today]

