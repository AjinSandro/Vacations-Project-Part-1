from flask import Blueprint, render_template, redirect,url_for ,session

about_blueprint = Blueprint("about_view",__name__)

@about_blueprint.route("/about")
def about():
    return render_template("about.html", active="about")

@about_blueprint.route("/about/submitTicket", methods = ["POST"])
def submitTicket():
    return redirect(url_for("home_view.home"))