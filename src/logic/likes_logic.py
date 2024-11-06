from utils.dal import *
from models.likes_model import *

class Likes_Logic:
    def __init__(self):
        self.dal = DAL()

    def search_for_user_ID(self,userId):
        sql = "SELECT userId FROM app_users WHERE userId = %s"
        params = (userId,)
        ID = self.dal.get_scalar(sql,params)
        return bool(ID) 
    
    def search_for_vacation_ID(self,vacation_id):
        sql = "SELECT vacation_id from vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        ID = self.dal.get_scalar(sql,params)
        return bool(ID)

    def add_like_to_vacation(self,userId,vacation_id):

        sql = "INSERT INTO likes (userId,vacation_id) VALUES (%s,%s)"
        params = (userId,vacation_id,)
        self.dal.insert(sql,params)
 
    def get_vacation_ids_of_liked_by_user(self,userId):
            sql = '''SELECT vacation_id 
                    FROM vacations_db.likes
                    where userId = %s;'''
            params = (userId,)
            vacations_likes_count= self.dal.get_table(sql,params)
            print(vacations_likes_count)
            #turning likes dictionary to list of vacationId values :
            likes = [vId for l in vacations_likes_count for vId in  l.values()]
            return likes

    def get_likes_by_vacation_id(self,vacation_id):
            sql = '''SELECT count(vacation_id) as LikeCount
                    FROM vacations_db.likes
                    where vacation_id = %s;'''
            params = (vacation_id,)
            vacation_like_count= self.dal.get_table(sql,params)
            likes = [vId for l in vacation_like_count for vId in  l.values()]
            return likes[0] #return int type number of likes for one vacation
        
    def delete_like_from_vacation(self,userId,vacation_id):
        sql = "DELETE FROM likes where userId = %s AND vacation_id = %s"
        params = (userId,vacation_id,)
        self.dal.delete(sql,params)


    def close(self):
        self.dal.close()