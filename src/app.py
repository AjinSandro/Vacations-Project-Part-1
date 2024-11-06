from mysql.connector import connect
from flask import Flask, render_template
from views.home_view import home_blueprint
from views.about_view import about_blueprint
from views.auth_view import auth_blueprint
from views.vacations_view import vacation_blueprint
# from logging import getLogger, ERROR
from utils.config import AppConfig
from utils.logger import Logger
from flask_login import current_user
from models.role_model import RoleModel
app = Flask(__name__)

user = current_user

app.secret_key = AppConfig.session_secret_key

app.register_blueprint(about_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(vacation_blueprint)


@app.context_processor
def inject_user():
    return dict(current_user=current_user, admin=RoleModel.Admin.value)

@app.errorhandler(404)
def page_not_found(error):
    Logger.log(str(error))
    return render_template("404.html")

@app.errorhandler(Exception)
def catch_all(error):
    Logger.log(str(error))
    return render_template('500.html',error=error)