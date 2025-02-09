#!/usr/bin/python3
"""
   starts a flask app
   listens to 0.0.0.0 on port 5000
"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    renders list of all cities by State objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
