#!/usr/bin/python3
"""Start a flask app that listens on 0.0.0.0:5000"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with list of all states objects in DBstorage
        States are storted in ascending order
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy sessions"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0..0")
