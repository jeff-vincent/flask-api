from flask import Flask, request, session

from csv_parser import ParseCSV

app = Flask('__main__')
app.secret_key = 'IsItSecret?IsItSafe?'

@app.route('/')
def index():
    session['logged_in'] = True
    return 'index'

@app.route('/parse-csv', methods=['GET','POST'])
def parse_csv():
    return ParseCSV.parse(request, session)




if __name__ == '__main__':
    app.run()