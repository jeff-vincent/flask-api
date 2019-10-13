from flask import Flask, request, session
from extensions import db
from csv_parser import ParseCSV

app = Flask('__main__')
app.secret_key = 'IsItSecret?IsItSafe?'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Jeff:password@localhost/flask-api-db'
db.init_app(app)

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