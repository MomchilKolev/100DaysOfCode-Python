import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

load_dotenv()

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
api_key = os.environ.get("API_KEY")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(
            self):  # This is a dictionary comprehension function created inside the Cafe class definition. It will be used to turn rows into a dictionary before sending it to jsonify.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=["GET"])
def random():
    random_cafe = db.session.execute(db.select(Cafe).order_by(db.sql.func.random()).limit(1)).scalar()
    cafe_dict = {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    }
    return jsonify(cafe=cafe_dict)


@app.route('/all', methods=["GET"])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    # This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP GET - Read Record
@app.route('/search', methods=["GET"])
def search():
    loc = request.args.get('location')
    cafes_in_area = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if len(cafes_in_area) == 0:
        error = { "error": {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        }
        return jsonify(error)
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes_in_area])


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():
    if request.method == "POST":
        name = request.form.get('name')
        map_url = request.form.get('map_url')
        new_cafe = Cafe(name=name, map_url=map_url)
        db.session.add(new_cafe)
        db.session.commit()


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update_cafe_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def report_closed(cafe_id):
    if api_key == request.args['api-key']:
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }), 404
    return jsonify(error={
        "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
    }), 403

if __name__ == '__main__':
    app.run(debug=True)
