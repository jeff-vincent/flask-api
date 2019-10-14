from models import User
from extensions import db
from auth import APIAuth

class Admin:


    def sign_up(request):
        
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Successfully created user {}'.format(new_user.email)
        
        except Exception as e:
            return 'Sign-up failed; ' + str(e)


    def login(request):

        try:
            active_user = APIAuth.authorize(request)
            if active_user:
                return 'Login successful'

            else:
                return 'Please sign-up'
        
        except Exception as e:
            return 'Login failed: ' + str(e)
