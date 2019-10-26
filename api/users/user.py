from flask import session
from models import User
from utils.extensions import db
from utils.auth import APIAuth

class Admin:

    # TODO: move this to the db. 
    ADMIN_USER_LIST = ['jeff.d.vincent@gmail.com']

    USER_ID = ''

    def sign_up(self, request):
        
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Successfully created user: ' + new_user.email
        
        except Exception as e:
            print(str(e))
            if 'UNIQUE constraint failed: user.email' in str(e):
                return 'An account with that email already exists.' 


    def login(self, request):

        try:
            active_user = APIAuth.authorize(request)

            if active_user:
                if active_user.email in Admin.ADMIN_USER_LIST:
                    session['admin_user'] = True
                
                Admin.USER_ID = active_user.id
                return 'Login successful'

            else:
                return 'Please sign-up'
        
        except Exception as e:
            return 'Login failed: ' + str(e)

    def logout(self, request):

        session['logged_in'] = False
        session['admin_user'] = False
        Admin.USER_ID = ''
        return 'Logout Successful'

