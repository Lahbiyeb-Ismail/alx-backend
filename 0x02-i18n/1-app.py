#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """
    Renders the index.html template.

    Returns:
      The rendered index.html template.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
