from datetime import datetime
from logic.vacations_logic import *

class VacationModel:

    def __init__(self,vacation_id,country_id,vacation_details,vacation_date_start,vacation_date_end,vacation_price,image):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.vacation_details = vacation_details
        self.vacation_date_start = vacation_date_start
        self.vacation_date_end = vacation_date_end
        self.vacation_price = vacation_price
        self.image = image


    def validate_insert(self):
        if not self.country_id: return "Missing country ID"
        if not self.vacation_details: return "Missing vacation details"
        if not self.vacation_date_start: return "Missing vacation start date"
        if not self.vacation_date_end: return "Missing vacation end date"
        if not self.vacation_price: return "Please input vacation price"
        
        if int(self.country_id) < 1 or int(self.country_id) > 12: return "country ID must be from within the supported ID list"
        if len(self.vacation_details) < 5 or len(self.vacation_details) > 250: return "Vacation details must be at least 5 characters and cannot go beyond 250"
        if float(self.vacation_price) < 1 or float(self.vacation_price) > 10000: return "vacation price must be between 1 to 10000 $"
        start_date = datetime.strptime(self.vacation_date_start, '%Y-%m-%d')
        end_date = datetime.strptime(self.vacation_date_end, '%Y-%m-%d')
        if end_date < start_date:  return "Vacation end date cannot be before the start date."
        return None

    def validate_edit(self):
        if not self.country_id: return "Missing country ID"
        if not self.vacation_details: return "Missing vacation details"
        if not self.vacation_date_start: return "Missing vacation start date"
        if not self.vacation_date_end: return "Missing vacation end date"
        if not self.vacation_price: return "Please input vacation price"
        if not self.image: return "Missing vacation image"
        if int(self.country_id) < 1 or int(self.country_id) > 12: return "country ID must be from within the supported ID list"
        if len(self.vacation_details) < 5 or len(self.vacation_details) > 250: return "Vacation details must be at least 5 characters and cannot go beyond 250"
        if float(self.vacation_price) < 1 or float(self.vacation_price) > 10000: return "vacation price must be between 0 to 10000 $"
        start_date = datetime.strptime(self.vacation_date_start, '%Y-%m-%d')
        end_date = datetime.strptime(self.vacation_date_end, '%Y-%m-%d')
        if end_date < start_date:  return "Vacation end date cannot be before the start date."
        return None


