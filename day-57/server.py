import os
import random
import requests

from flask import Flask, render_template
from datetime import date
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
blog_url = os.environ.get('BLOG_URL')

@app.route('/')
def index():
    random_number = random.randint(1, 10)
    year = date.today().year
    return render_template(
        "index.html",
        random_number=random_number,
        year=year,
        creator="Peter Dinkens",
    )

@app.route('/blog/<id>')
def get_blog(id):
    response = requests.get(blog_url)
    all_posts = response.json()
    print("id", id)
    return render_template("blog.html", posts=all_posts, id=id)

if __name__ == "__main__":
    app.run(debug=True)