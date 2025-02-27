from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def home():
    return render_template("routes/home.html")