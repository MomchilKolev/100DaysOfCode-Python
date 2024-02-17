import os

import requests

from flask import Flask, render_template, request
from dotenv import load_dotenv
from smtplib import SMTP

load_dotenv()

api_endpoint = os.environ.get("API_ENDPOINT")
host = os.environ.get("HOST")
port = int(os.environ.get("PORT"))
from_addr = os.environ.get("FROM_ADDR")
to_addr = os.environ.get("TO_ADDR")

posts = requests.get(api_endpoint).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", h1='Contact me')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        msg = f"""
FROM: {from_addr}
TO: {to_addr}
Subject: New Message

        
Name: {name}
Email: {email}
Phone: {phone}
Message: {message}
"""

        smtp = SMTP(host=host, port=port)
        smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg)
        
        return render_template("contact.html", h1='Successfully sent your message')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
