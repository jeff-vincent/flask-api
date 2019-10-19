from admin import Admin
from flask import session
from extensions import db
from models import File
from config import Config
import requests


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
            
            return r.text


    def download(request):
        return ''