
from validate_email_address import validate_email

class CredentialsModel:

    def __init__(self,email,password):
        self.email = email
        self.password = password
  

    def validate(self):
        if not self.email: return "One of the parameters is not correct"
        if not self.password: return "One of the parameters is not correct"
        if not validate_email(self.email): return "email not valid"
        return None