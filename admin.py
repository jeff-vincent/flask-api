from flask import session
from models import User
from extensions import db
from auth import APIAuth

class Admin:

    USER_ID = ''

    def sign_up(request):
        
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Successfully created user {}'.format(new_user.email)
        
        except Exception as e:
            if "key 'email'" in str(e):
                return 'An account with that email already exists.' 


    def login(request):

        try:
            active_user = APIAuth.authorize(request)
            if active_user:
                
                Admin.USER_ID = active_user.id
                return 'Login successful'

            else:
                return 'Please sign-up'
        
        except Exception as e:
            return 'Login failed: ' + str(e)

    def logout(request):

        session['logged_in'] = False
        Admin.USER_ID = ''
        return 'Logout Successful'

