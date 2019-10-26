from flask import Flask, request
from utils.extensions import db
from posts.create_post import CreatePost
from users.user import Admin
from posts.get_post import GetPost
from users.get_user import GetUser
from utils.file_store import FileStore


def create_app():
    app = Flask(__name__)
    app.secret_key = 'IsItSecret?IsItSafe?'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
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
            <p><input type=submit value="Sign Up">
        </form>
        <form action="/login" method="post">
            <p><input type=text name=email>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        <form action="/create-post" method="post">
            <p><input type=text name=content>
            <p><input type=submit value="Create Post">
        </form>
        <form action="/logout" method="get">
            <p><input type=submit value=Logout>
        </form>
        <form action="/get-posts" method="get">
            <p><input type=submit value="Get Posts">
        </form>
        <form action="/get-current-users-posts" method="get">
            <p><input type=submit value="Get Your Posts">
        </form>
        <form action="/get-current-user" method="get">
            <p><input type=submit value="Get Yourself">
        </form>
        <form action="/get-all-users" method="get">
            <p><input type=submit value="Get All Users (Admin action)">
        </form>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <p><input type=file name=file>
            <p><input type=submit value="upload file">
        </form>
        <form action="/download" method="post">
            <p><input type=text name=filename>
            <p><input type=submit value="download file">
        </form>
        <form action="/get-current-users-files" method="get">
            <p><input type=submit value="Get Your Files">
        </form>
        """


@app.route('/sign-up', methods=['POST'])
def sign_up():
    admin = Admin()
    return admin.sign_up(request)


@app.route('/login', methods=['POST'])
def login():
    admin = Admin()
    return admin.login(request)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    admin = Admin()
    return admin.logout(request)


@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    cp = CreatePost()
    return cp.create_post(request)


@app.route('/get-posts', methods=['GET'])
def get_posts():
    gp = GetPost()
    return gp.get_posts(request)


@app.route('/get-current-users-posts', methods=['GET'])
def get_current_users_posts():
    gp = GetPost()
    return gp.get_current_users_posts(request)


@app.route('/get-current-user', methods=['GET'])
def get_current_user():
    gu = GetUser()
    return gu.get_current_user(request)


# Requires Admin
@app.route('/get-all-users', methods=['GET'])
def get_all_users():
    gu = GetUser()
    return gu.get_all_users(request)


# NOTE: The following endpoints require the FileStore service locally. 
@app.route('/upload', methods=['POST'])
def upload():
    fs = FileStore()
    return fs.upload(request)


@app.route('/download', methods=['POST'])
def download():
    fs = FileStore()
    return fs.download(request)


@app.route('/get-current-users-files', methods=['GET'])
def get_current_users_files():
    fs = FileStore()
    return fs.get_current_users_files(request)


if __name__ == '__main__':
    app.run()
