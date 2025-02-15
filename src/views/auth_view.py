from flask import Blueprint, render_template, send_file , url_for, redirect, request
from facades.auth_facade import AuthFacade
from models.client_error import *
from models.credentials_model import *
from utils.logger import Logger

auth_blueprint = Blueprint("auth_view",__name__)

facade = AuthFacade()

@auth_blueprint.route("/register",methods = ["GET","POST"])
def register():
    try:
        if request.method == "GET":return render_template("register.html",active = "register", user={})
        facade.register()
        return redirect(url_for("vacations_view.list"))
    except ValidationError as err:
        return render_template("register.html",error = err.message, user = err.model)
    

@auth_blueprint.route("/login",methods = ["GET","POST"])
def login():
    try:
        if request.method == "GET":return render_template("login.html", active="login", credentials = {})
        facade.login()
        return redirect(url_for("vacations_view.list"))
    except (ValidationError, AuthError) as err:
        Logger.log(err.message)
        return render_template("login.html",error = err.message, credentials = err.model)


@auth_blueprint.route("/logout")
def logout():
    facade.logout()
    return redirect(url_for("home_view.home"))