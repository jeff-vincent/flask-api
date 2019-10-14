from flask import Flask, request, session
from extensions import db
from csv_parser import ParseCSV
from sign_up import SignUp


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
    session['logged_in'] = True
    return 'index'

@app.route('/sign-up', methods=['POST'])
def sign_up():
    return SignUp.sign_up(request)

@app.route('/parse-csv', methods=['GET','POST'])
def parse_csv():
    return ParseCSV.parse(request, session)

if __name__ == '__main__':
    app.run()