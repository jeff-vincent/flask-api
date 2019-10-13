from flask import Flask, request
import csv

from csv_parser import ParseCSV

app = Flask('__main__')

@app.route('/')
def index():
    return 'index'

@app.route('/parse-csv', methods=['GET','POST'])
def parse_csv():
    return ParseCSV.parse(request)




if __name__ == '__main__':
    app.run()