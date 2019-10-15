from models import User
from extensions import db
from admin import Admin
from flask import session

class GetUser:

    def get_current_user(request):
        try:
            if session['logged_in']:
                current_user = db.session.query(User).filter_by(id=Admin.USER_ID).first()
                if current_user:
                    return current_user.email
                else:
                    return 'Please log in'
            else:
                return 'Please log in'
        
        except Exception as e:
            return 'Get user failed: ' + str(e)

