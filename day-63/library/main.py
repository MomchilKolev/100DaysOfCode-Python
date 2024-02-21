from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, Integer, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

all_books = []


@app.route('/')
def home():
    all_books = list(db.session.execute(db.select(Book)).scalars())
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_dict = request.form.to_dict()
        all_books.append(book_dict)
        new_book = Book(**book_dict)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit/<book_id>', methods=["GET", "POST"])
def edit(book_id):
    if request.method == "POST":
        new_rating = request.form.get('rating')
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", book_id=book_id)


@app.route('/delete/<book_id>')
def delete(book_id):
    try:
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    except BaseException as error_message:
        print("Could not delete book", error_message)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

