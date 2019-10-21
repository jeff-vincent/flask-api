from flask import session, jsonify, make_response
from base64 import b64encode, b64decode, decodebytes
import io
import requests
import os

# Local modules
from extensions import db
from models import File, file_schema
from config import Config
from admin import Admin


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
                file_type = FileStore._get_file_type(filename)
                if file_type in ['.jpg', '.png']:
                    return FileStore._handle_image(r, filename)
                if file_type =='.pdf':
                    return FileStore._handle_pdf(r, filename)
                else:
                    return 'Unrecognized file type. Returning data as stored: ' + str(r.content)

            else:
                return 'Connection to Mongo failed.'

    def _get_file_type(filename):
        base_name, extension = os.path.splitext(filename)
        return extension

    def _handle_image(r, filename):
        img = b64encode(r.content)
        img = img.decode('utf-8')
        return '<img id="'+ filename +'" src="data:image/jpg;base64,'+ img +'">'

    
    def _handle_pdf(r, filename):
        buffer = io.BytesIO()
        pdf = b64encode(r.content)
        pdf = b64decode(pdf)
        buffer.write(pdf)
        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=' + filename
        return response

    def get_current_users_files(request):
        if session['logged_in']:
            files = db.session.query(File).filter_by(user_id=Admin.USER_ID).all()
            files = file_schema.dump(files)
            return jsonify(files)

