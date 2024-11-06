from logic.vacations_logic import Vacations_Logic
from flask import request
from models.vacation_model import VacationModel
from models.client_error import *
from datetime import datetime


class VacationFacade:
    def __init__(self):
        self.logic = Vacations_Logic()

    def get_all_vacations(self):
        return self.logic.get_all_vacations_by_date()
    
    def get_one_vacation(self, vacation_id):
        vacation = self.logic.get_one_vacation(vacation_id)
        if not vacation:raise ResourceNotFoundError(vacation_id)
        return vacation


    def add_new_holiday(self):
        country_id = request.form.get("country_id") 
        vacation_details = request.form.get("vacation_details") 
        vacation_date_start = request.form.get("vacation_date_start") 
        vacation_date_end = request.form.get("vacation_date_end")
        vacation_price = request.form.get("vacation_price")
        image = request.files["image"] 
        vacation = VacationModel(None, country_id, vacation_details, vacation_date_start, vacation_date_end, vacation_price, image)
        error = vacation.validate_insert()
        if error : raise ValidationError(error,vacation)
        self.logic.add_vacation(vacation)
        
 

    def update_vacation(self):
        vacation_id = request.form.get("vacation_id")
        country_id = request.form.get("country_id") 
        vacation_details = request.form.get("vacation_details") 
        vacation_date_start = request.form.get("vacation_date_start") 
        vacation_date_end = request.form.get("vacation_date_end")
        vacation_price = request.form.get("vacation_price")
        image = request.files["image"] 
        vacation = VacationModel(vacation_id, country_id, vacation_details, vacation_date_start, vacation_date_end, vacation_price, image)
        error = vacation.validate_edit()
        if error : raise ValidationError(error,vacation)
        self.logic.update_vacation(vacation)
        

    def delete_existing_vacation(self,vacation_id):
        self.logic.delete_vacation(vacation_id)

    def close(self):
        self.logic.close()



