# pip install python-dotenv

from dotenv import load_dotenv
from os import environ

load_dotenv()

class AppConfig:
    is_development = environ.get("environment") == "development"
    is_production = environ.get("environment") == "production"
    mysql_host = environ.get("mysql_host")
    mysql_user = environ.get("mysql_user")
    mysql_password = environ.get("mysql_password")
    mysql_db = environ.get("mysql_db")
    session_secret_key = environ.get("session_secret_key")
    password_salt = environ.get("password_salt")