#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, g, render_template, request
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user based on the provided user ID.
    """

    user_id = request.args.get("login_as")

    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """
    Function that is executed before each request is processed.
    It sets the 'user' attribute in the flask.g object to the current user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Returns the best matching language from the request's accepted languages.
    """
    locale = request.args.get("locale")

    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(["LANGUAGES"])


@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
      The rendered index.html template.
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
