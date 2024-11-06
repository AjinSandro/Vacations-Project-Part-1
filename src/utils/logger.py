from datetime import datetime
from flask import session

class Logger:
    #path to log file
    log_file ="./logger.log"

    @staticmethod
    def log(message):
        now = datetime.now()
        with open(Logger.log_file, "a") as file:  # a = append
            file.write(str(now) + "\n")
            file.write(message + "\n")
            
            user = session.get("current_user")
            if user:
                # Correct concatenation
                user_info = "User ID: " + str(user.get("userId", "N/A")) + ", User Email: " + user.get("email", "N/A")
                file.write(user_info + "\n")
                
            file.write("-------------------------------------------------" + "\n")