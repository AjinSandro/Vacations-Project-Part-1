from logic.auth_logic import AuthLogic
from flask import request, session
from models.users_model import UsersModel
from models.role_model import RoleModel
from models.client_error import *
from models.credentials_model import CredentialsModel
from utils.cyber import Cyber
from logic.auth_logic import *

class AuthFacade:
    def __init__(self):
        self.logic = AuthLogic()

    # Registration Facades:    
    def register(self):
        
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        user = UsersModel(None,firstname,lastname,email,password,RoleModel.User.value)
        
        error = user.validate_insert()
        if error: raise ValidationError("Registration error, please try again.", user)
        if self.logic.is_email_taken(email): raise ValidationError("Email already exists.",user)
        user.password = Cyber.hash(user.password)
        self.logic.add_user(user)
        credentials = CredentialsModel(email,Cyber.hash(password))
        user = self.logic.get_user(credentials)
        del user["password"] # delete from session dictionary password key
        session["current_user"] = user 

        
    # User login Facades:
    def login(self):

        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialsModel(email,Cyber.hash(password))
        error = credentials.validate()
        if error : raise ValidationError(error, credentials)
        user = self.logic.get_user(credentials)
        if not user : raise AuthError("Incorrect email or password", user)
        del user["password"] # delete from session dictionary password key
        session["current_user"] = user 
        
     # block guest - users that didn't login
    def block_anonymous(self):
        user = session.get("current_user")
        if not user : raise AuthError("You're not logged in.")

    # block guests or users that dont have admin permission
    def block_non_admin(self):
        user = session.get("current_user")
        if not user : raise AuthError("You're not logged in.")
        if user["role_type"] != RoleModel.Admin.value: raise AuthError ("You're not authorized to perform this action.")

    def logout(self):
        session.clear()
        

    def close(self):
        self.logic.close()

