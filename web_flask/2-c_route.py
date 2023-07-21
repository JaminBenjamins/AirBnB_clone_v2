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
    return "C {}".format(text.replace("_"," "))   


if __name__ == "__main__":
    app.run(host="0.0.0.0")
