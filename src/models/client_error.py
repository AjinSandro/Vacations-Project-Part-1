class ClientError(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message = message


class ResourceNotFoundError(ClientError):
    def __init__(self,vacation_id):
        super().__init__(f"{vacation_id} not found")
        self.vacation_id = vacation_id
        

class ValidationError(ClientError):
    def __init__(self,message,model):
        super().__init__(message)
        self.model = model
        

class AuthError(ClientError):
    def __init__(self,message,model=None):
        super().__init__(message)
        self.model = model