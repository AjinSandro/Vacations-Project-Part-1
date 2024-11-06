from flask import Blueprint, render_template, session , redirect, url_for
from facades.auth_facade import AuthFacade
home_blueprint = Blueprint("home_view",__name__)
auth_facade = AuthFacade()
from models.client_error import *
@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    try:
        auth_facade.block_anonymous()
        user = session.get("current_user")
        return render_template("home.html", active="home", current_user = user)
    except AuthError as err:
       return redirect(url_for("auth_view.login",error=err.message, credentials = {}))
    except ValidationError as err:
        return render_template("login.html", error=err.message)
