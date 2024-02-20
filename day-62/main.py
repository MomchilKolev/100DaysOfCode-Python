import csv
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_wtf.form import request
from dotenv import load_dotenv

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
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField(
        'Cafe Location on Google Maps (URL)',
        validators=[DataRequired(), URL()]
    )
    opening_time = StringField('Opening Time e.g. 6AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 10pm', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Coffee Rating',
        choices=[('x' if i == 0 else '☕' * i, 'x' if i == 0 else '☕' * i) for i in range(0, 6)]
    )
    wifi_rating = SelectField(
        'Wifi Strength Rating',
        choices=[('✘' if i == 0 else '💪' * i, '✘' if i == 0 else '💪' * i) for i in range(0, 6)]
    )
    power_rating = SelectField(
        'Power Rating',
        choices=[('✘' if i == 0 else '🔌' * i, '✘' if i == 0 else '🔌' * i) for i in range(0, 6)]
    )
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
    # Exercise:
        values = request.form.values()
        list_values = list(values)[1:-1]
        csv_row = ','.join(list_values)
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open('cafe-data.csv', 'a') as data_file:
            data_file.write(f"\n{csv_row}")
        print('added new entry', csv_row)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
