from models import User
from extensions import db

class SignUp:


    def sign_up(request):
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Successfully created user {}'.format(new_user.email)
        
        except Exception as e:
            return str(e)
