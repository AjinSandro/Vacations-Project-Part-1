# pip install validate_email_address
from validate_email_address import validate_email
from models.role_model import RoleModel


class UsersModel:

    def __init__(self,userId,firstname,lastname,email,password,role_type):
        self.userId = userId
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role_type = role_type


    def validate_insert(self):
        if not self.firstname: return "missing first name"
        if not self.lastname: return "missing last name"
        if not self.email: return "missing email"
        if not self.password: return "missing password"
        # if not self.role_type: return "missing role_type"
        if len(self.firstname) < 2 or len(self.firstname) > 20: return "firstname must be 2-20 characters"
        if len(self.lastname) < 2 or len(self.lastname) > 20: return "lastname must be 2-20 characters"
        if not validate_email(self.email): return "email not valid"
        if len(self.password) < 5 or len(self.password) > 20: return "password must be 5-20 characters long"
        if self.role_type != RoleModel.Admin.value and self.role_type != RoleModel.User.value : "You're not in a valid role."
        return None


