from models import User, user_schema
from extensions import db
from admin import Admin
from flask import session, jsonify

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


    def get_all_users(request):
        try:
            if session['logged_in']:
                if session['admin_user']:
                    data = db.session.query(User).all()
                    data = user_schema.dump(data)
                    return jsonify(data)
                else:
                    return 'This action is restricted to admin users.'
            else:
                return 'Please log in'

        except Exception as e:
            return 'Get all users failed: ' + str(e)


