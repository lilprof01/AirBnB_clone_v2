#!/usr/bin/python3
"""
   script that runs a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """renders home route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """renders /hbnb web app route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """renders the value of /c/<text>"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_route(text="is cool"):
    """renders the value of /python/<text>"""
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
