from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapped_function():
        return '<b>' + function() + "</b>"
    return wrapped_function

def make_emphasis(function):
    def wrapped_function():
        return "<em>" + function() + "</em>"
    return wrapped_function

def make_underlined(function):
    def wrapped_function():
        return "<u>" + function() + "</u>"
    return wrapped_function


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return ("<h1 style='text-align: center;'>Hello world</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://media.giphy.com/media/1wnZSnmrnwJmnJkd1c/giphy-downsized-large.gif"
            "' width='200' />")

@app.route('/<name>')
def greet(name):
    return f"Hello there {name}"

@app.route('/<name>/potato')
def greet2(name):
    return f"Hello there2 {name}"

@app.route('/username/<name>/<number>')
def greet3(name, number):
    return f"Hello there {name}! You are number {number}!"

if __name__ == "__main__":
    app.run(debug=True)
