from admin import Admin
from flask import session, jsonify
from extensions import db
from models import File, file_schema
from config import Config
import requests
from base64 import b64encode


class FileStore:

    def upload(request):
        file = request.files['file']
        filename = request.form['filename']
        files = {'file': file}
        if session['logged_in']:
            data = {
                'filename': filename,
            }
            r = requests.post(Config.FILE_STORE_URI + 'upload', data=data, files=files)

            if r.status_code == 200:
                file = File(filename=filename, user_id=Admin.USER_ID)
                db.session.add(file)
                db.session.commit()

                return 'Upload successful. _id: ' + r.text
            else:
                return 'Connection to Mongo failed.'


    def download(request):
        filename = request.form['filename']
        if session['logged_in']:
            data = {
                'filename': filename,
            }
            r = requests.post(Config.FILE_STORE_URI + 'download', data=data)

            if r.status_code == 200:
                img = b64encode(r.content)
                img = img.decode('utf-8')
                return '<img id="'+filename+'" src="data:image/jpg;base64,'+ img +'">'
            else:
                return 'Connection to Mongo failed.'

    def get_current_users_files(request):
        if session['logged_in']:
            files = db.session.query(File).filter_by(user_id=Admin.USER_ID).all()
            files = file_schema.dump(files)
            return jsonify(files)