#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Print a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb/', strict_slashes=False)
def display_HBNB():
    return 'HBNB'


@app.route('/c/<text>/', strict_slashes=False)
def C_is_fun(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def Python_is_cool(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
