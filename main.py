from flask import Flask, request
from extensions import db
from create_post import CreatePost
from admin import Admin


def create_app():
    app = Flask(__name__)
    app.secret_key = 'IsItSecret?IsItSafe?'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/flaskapidb'
    db.init_app(app)    
    return app 

def setup_database(app):
    with app.app_context():
        db.create_all()

app = create_app()
setup_database(app)


@app.route('/')
def index():
    return """
        <form action="/sign-up" method="post">
            <p><input type=text name=email placeholder=email>
            <p><input type=password name=password placeholder=password>
            <p><input type=submit value="Sign Up" >
        </form>
        <form action="/login" method="post">
            <p><input type=text name=email>
            <p><input type=password name=password>
            <p><input type=submit value=Login >
        </form>
        <form action="/create-post" method="post">
            <p><input type=text name=content>
            <p><input type=submit value="Create Post" >
        </form>
        <form action="/logout" method="get">
            <p><input type=submit value=Logout >
        </form>
        """

@app.route('/sign-up', methods=['POST'])
def sign_up():
    return Admin.sign_up(request)

@app.route('/login', methods=['POST'])
def login():
    return Admin.login(request)

@app.route('/logout', methods=['GET','POST'])
def logout():
    return Admin.logout(request)

@app.route('/create-post', methods=['GET','POST'])
def do_task():
    return CreatePost.create_post(request)

if __name__ == '__main__':
    app.run()