from flask import session
from utils.extensions import db
from models import User



class APIAuth:
    
    @staticmethod
    def authorize(request):
        email = request.form['email']
        password = request.form['password']

        try:
            user = db.session.query(User).filter_by(email=email, password=password).first()
        
            if user:
                session['logged_in'] = True
                return user
            else:
                return False
        
        except Exception as e:
            return 'Auth failed: ' + str(e)
            