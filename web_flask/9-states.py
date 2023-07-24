#!/usr/bin/python3
"""Starts a web flask application
    Application listens on 0.0.0.0:5000
    Routes:
        HTML page with given state 
        and cities ordered by name
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Display an HTML page with list of all states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id():
    """Display info about state id if it exists"""
    for state in storage.all("State").values():
        if state.id == id
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
