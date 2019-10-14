from extensions import db
from models import User


class APIAuth:

    def authorize(request, session):
        email = request.form['email']
        password = request.form['password']

        try:
            user = db.session.query(User).filter_by(email=email, password=password).first()
        
            if user:
                session['logged_in'] = True
                return 'A'
        
        except Exception as e:
            return str(e)
            