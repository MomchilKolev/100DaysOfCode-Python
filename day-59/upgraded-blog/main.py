import os

import requests

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

posts_url = os.environ.get("API_ENDPOINT")


@app.route('/')
def index():
    response = requests.get(posts_url)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<id>')
def post(id):
    response = requests.get(f"{posts_url}/{id}")
    post = response.json()
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)