# --------------------------------------------
# Routes for mediamaps.com
# --------------------------------------------

from flask import Blueprint, render_template, send_from_directory,current_app
import os

routes = Blueprint("routes", __name__)


@routes.route("/")
def home():
    return render_template("home.html")

@routes.route("/.well-known/security.txt")
def security_txt():
    return send_from_directory(
        directory=current_app.static_folder,
        path='security.txt',
        mimetype='text/plain; charset=utf-8'
    )
