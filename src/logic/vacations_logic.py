from utils.dal import DAL
from utils.image_handler import ImageHandler

class Vacations_Logic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations_by_date(self):
        sql = '''SELECT 
    v.vacation_id, 
    v.vacation_details,
    v.vacation_date_start,
    v.vacation_date_end,
    v.vacation_price,
    v.vacation_picture_file,
    c.country_name, 
    COALESCE(l.LikeCount, 0) AS LikeCount
    FROM vacations_db.vacations v
    JOIN vacations_db.countires c ON v.country_id = c.country_Id
    LEFT JOIN (
    SELECT vacation_id, COUNT(*) AS LikeCount
    FROM vacations_db.likes
    GROUP BY vacation_id
    ) l ON l.vacation_id = v.vacation_id
    ORDER BY v.vacation_date_start ASC, v.vacation_date_end ASC;'''
        return self.dal.get_table(sql)


    def get_one_vacation(self,vacation_id):
        sql = "select * FROM vacations_db.vacations WHERE vacation_id = %s"
        return self.dal.get_scalar(sql,(vacation_id,))


    def search_for_Vacation_ID(self,vacation_id):
        sql = "SELECT vacation_id from vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_scalar(sql,params)
        return bool(result)
    

    def add_vacation(self,vacation):
        vacation_picture_file = ImageHandler.save_image(vacation.image)
        sql = "INSERT INTO vacations (country_id,vacation_details,vacation_date_start,vacation_date_end,vacation_price,vacation_picture_file) VALUES (%s, %s, %s, %s, %s, %s)"
        
        return self.dal.insert(sql,(vacation.country_id,vacation.vacation_details,vacation.vacation_date_start,vacation.vacation_date_end,vacation.vacation_price,vacation_picture_file))

      
    def update_vacation(self,vacation):
        old_image_name = self.get_old_image_name(vacation.vacation_id)
        vacation_picture_file = ImageHandler.update_image(old_image_name, vacation.image)
        sql = "UPDATE vacations_db.vacations SET country_id = %s, vacation_details = %s, vacation_date_start = %s, vacation_date_end = %s, vacation_price = %s, vacation_picture_file = %s where vacation_id = %s"
        self.dal.update(sql, ((vacation.country_id,vacation.vacation_details,vacation.vacation_date_start,vacation.vacation_date_end,vacation.vacation_price,vacation_picture_file,vacation.vacation_id)))


    def get_old_image_name(self,vacation_id):
        sql = "SELECT vacation_picture_file from vacations where vacation_id = %s"
        result = self.dal.get_scalar(sql,(vacation_id,))
        return result["vacation_picture_file"]


    def delete_vacation(self,vacation_id):
        vacation_picture_file = self.get_old_image_name(vacation_id)
        ImageHandler.delete_image(vacation_picture_file)
        sql = "DELETE FROM vacations where vacation_id = %s"
        self.dal.delete(sql,(vacation_id,))
        
    
    def close(self):
        self.dal.close()
        