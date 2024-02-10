from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 9)
COLORS = ["gold", "indianred", "lightseagreen", "mediumvioletred", "navy", "sienna",
          "cornflowerblue", "crimson", "olive", "orchid"]


def colorize_h1_decorator(fn):
    def wrapper(**kwargs):
        return f"<div style='color: {COLORS[int(kwargs['n'])]}'>" + fn(kwargs['n']) + "</div>"
    return wrapper


@app.route('/')
def index():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
            "' width='200' />")


@app.route('/<n>')
@colorize_h1_decorator
def guess(n):
    n = int(n)
    if n > random_number:
        return ("<h1>Too high</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />")
    elif n < random_number:
        return ("<h1>Too low</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />")
    return ("<h1>Correct</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")


if __name__ == "__main__":
    app.run(debug=True)
