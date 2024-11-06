from logic.likes_logic import *


class LikesFacade:
    def __init__(self):
        self.logic = Likes_Logic()

    def get_likes_by_vacation_id(self,vacation_id): 
        LikesCount = self.logic.get_likes_by_vacation_id(vacation_id)
        return LikesCount

    def user_Likes_per_vacation(self,userId):
        all_likes = self.logic.get_vacation_ids_of_liked_by_user(userId)
        return all_likes

    def add_likes_to_vacations(self,userId,vacation_id):
        result = self.logic.add_like_to_vacation(userId,vacation_id)
        return result
    

    def remove_like_from_vacation(self,userId,vacation_id):
        result = self.logic.delete_like_from_vacation(userId,vacation_id)
        return result


    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
    
    def __exit__(self):
        self.close()