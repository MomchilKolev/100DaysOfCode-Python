import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests
from urllib import parse
import json
from datetime import datetime

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

tmdb_api_key = os.environ.get("TMDB_API_KEY")
tmdb_authorization_token = os.environ.get("TMDB_AUTHORIZATION_TOKEN")
tmdb_search_url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
tmdb_get_movie_url = "https://api.themoviedb.org/3/movie/"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {tmdb_authorization_token}"
}
tmdb_poster_url = "https://image.tmdb.org/t/p/original/"


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int]
    description: Mapped[str]
    rating: Mapped[float]
    ranking: Mapped[int]
    review: Mapped[str]
    img_url: Mapped[str]


# CREATE TABLE
with app.app_context():
    db.create_all()

    # Add first item
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # second_movie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    # db.session.add(second_movie)
    # db.session.commit()


# Create Edit Form
class EditForm(FlaskForm):
    rating = IntegerField('Your Rating out of 10, e.g. 7.5', validators=[DataRequired()], )
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField()

class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    movies_list = list(movies)
    # print(movies_list)
    return render_template("index.html", movies=movies_list)


@app.route('/edit/<id>', methods=["GET", "POST"])
def edit(id):
    movie = db.session.get(Movie, id)
    print('movie', movie.rating)
    if request.method == "POST":
        new_rating = request.form.get("rating")
        new_review = request.form.get("review")
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    else:
        edit_form = EditForm()
        return render_template("edit.html", id=id, form=edit_form, movie=movie)


@app.route('/delete/<id>')
def delete(id):
    movie = db.session.get(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if request.method == 'POST':
        title = request.form.get('title')
        query = parse.urlencode({ "query": title })
        response = requests.get(url=f"{tmdb_search_url}&{query}", headers=headers)
        data = response.json()
        movies = data['results']
        # print('movies', movies)
        return render_template("select.html", movies=movies)
    return render_template('add.html', form=add_form)


@app.route('/find_movie/<id>', methods=["GET", "POST"])
def get_movie(id):
    response = requests.get(url=f"{tmdb_get_movie_url}/{id}", headers=headers)
    data = response.json()
    new_movie = Movie(
        title=data['title'],
        img_url=f"{tmdb_poster_url}{data['poster_path']}",
        year=datetime.strptime(data['release_date'], '%Y-%m-%d').year,
        description=data['overview'],
        rating=0,
        review=0,
        ranking=10
    )
    print('data', data)
    print('new_movie', new_movie)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
