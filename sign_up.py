from db import User
from utils import ParseRequest

class SignUp:

    def sign_up(request):
        request_dict = ParseRequest.parse(request)

        try:
            new_user = User(email=request_dict['email'], password=request_dict['password'])
        
        except Exception as e:
            return str(e)
