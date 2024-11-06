from utils.dal import *


class AuthLogic:
    def __init__(self):
        self.dal = DAL()

    
    def add_user(self,user):
        
        sql = "INSERT INTO app_users(firstname,lastname,email,password,role_type) VALUES(%s, %s, %s, %s, %s)"
        self.dal.insert(sql ,(user.firstname, user.lastname, user.email, user.password, user.role_type))
       

    def get_user(self, credentials):
        sql = "SELECT * FROM app_users WHERE email = %s and password = %s"
        user = self.dal.get_scalar(sql,(credentials.email,credentials.password))
        return user


    def is_email_taken(self,email):
        sql = "select EXISTS(select * from app_users where email = %s) as is_taken"
        result = self.dal.get_scalar(sql,(email,))
        return result["is_taken"] == 1    
    
    def close(self):
        self.dal.close()