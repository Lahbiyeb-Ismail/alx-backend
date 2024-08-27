#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for the application.

    Attributes:
      LANGUAGES (list): A list of supported languages for the application.
      BABEL_DEFAULT_LOCALE (str): The default locale for the application.
      BABEL_DEFAULT_TIMEZONE (str): The default timezone for the application.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Returns the best matching language from the request's accepted languages.
    """
    return request.accept_languages.best_match(["LANGUAGES"])


@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
      The rendered index.html template.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
