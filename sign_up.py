from models import User

class SignUp:


    def sign_up(request):
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = User(email=email, password=password)
            return 'Successfully created user {}'.format(new_user.email)
        
        except Exception as e:
            return str(e)
