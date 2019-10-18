from admin import Admin
from flask import session
from extensions import db
from models import File
from config.Config import FILE_STORE_URI
import requests


class FileStore:

    def upload(filename, file):
        if session['logged_in']:
            data = {
                'filename': filename,
                'file': file
            }
            r = requests.post(FILE_STORE_URI + 'upload', data)

            if r.status_code == 200:
                file = File(filename=filename, user_id=Admin.USER_ID)
                db.session.add(file)
                db.session.commit()
            
            return r


    def download(request):
        return ''