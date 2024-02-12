import requests
import os

from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
blog_url = os.environ.get('BLOG_URL')


@app.route('/')
def home():
    response = requests.get(blog_url)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<id>')
def get_post(id):
    post_url = f"{blog_url}/{id}"
    response = requests.get(post_url)
    post = response.json()
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
