#!/usr/bin/python3
"""A script that starts a web application with given routes"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints given string"""
    return "Hello HBNB!"


@app.route("/", strict_slashes=False)
def hbnb():
    """Display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Print given text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """Display Python {}" followed by given input"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n is a number if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
