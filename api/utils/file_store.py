from flask import session, jsonify, make_response, Response, flash
from base64 import b64encode, b64decode, decodebytes
import io
import requests
import os
import tempfile
import mimetypes

# Local modules
from utils.extensions import db
from models import File, file_schema
from config import FILE_STORE_URI
from users.user import Admin


class FileStore:

    def upload(self, request):
        file = request.files['file']
        filename = file.filename
        files = {'file': file}
        if session['logged_in']:
            data = {
                'filename': filename,
            }
            flash('Uploading file...')
            r = requests.post(FILE_STORE_URI + 'upload', data=data, files=files)

            if r.status_code == 200:
                file = File(filename=filename, user_id=Admin.USER_ID)
                db.session.add(file)
                db.session.commit()

                return 'Upload successful. _id: ' + r.text
            else:
                return 'Connection to Mongo failed.'

    def download(self, request):
        if request.method == 'POST':
            filename = request.form['filename']
            if session['logged_in']:
                data = {
                    'filename': filename,
                }
                session['filename'] = filename
                r = requests.post(FILE_STORE_URI + 'download', data=data, stream=True)

            if r.status_code == 200:
                file_type = FileStore._get_file_type(filename)
                if file_type in ['.jpg', '.png']:
                    return FileStore._handle_image(r, filename)
                if file_type == '.pdf':
                    return FileStore._handle_pdf(r, filename)
                if file_type == '.mp4':
                    return FileStore._handle_mp_four(r)
                else:
                    return 'Unrecognized file type. Returning data as stored: ' + str(r.content)

            else:
                return 'Connection to Mongo failed.'
        else:
            data = {
                'filename': session['filename']
            }
            r = requests.post(FILE_STORE_URI + 'download', data=data)
            return FileStore._handle_mp_four(r)

    def get_current_users_files(self, request):
        if session['logged_in']:
            files = db.session.query(File).filter_by(user_id=Admin.USER_ID).all()
            files = file_schema.dump(files)
            return jsonify(files)

    @staticmethod
    def _get_file_type(filename):
        base_name, extension = os.path.splitext(filename)
        return extension

    @staticmethod
    def _handle_image(r, filename):
        img = b64encode(r.content)
        img = img.decode('utf-8')
        return '<img id="' + filename +'" src="data:image/jpg;base64,'+ img +'">'

    @staticmethod
    def _handle_pdf(r, filename):
        buffer = io.BytesIO()
        pdf = b64encode(r.content)
        pdf = b64decode(pdf)
        buffer.write(pdf)
        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=' + filename
        return response

    @staticmethod
    def _generate_data_from_response(resp, chunk=2048):
        for data_chunk in resp.iter_content(chunk_size=chunk):
            yield data_chunk

    @staticmethod
    def _handle_mp_four(r):
        rv = Response(FileStore._generate_data_from_response(r), 206, mimetype='video/mp4',
                    direct_passthrough=True)
        rv.headers.add('Content-Range', r.headers.get('Content-Range'))
        rv.headers.add('Content-Length', r.headers['Content-Length'])
        return rv

