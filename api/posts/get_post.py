from flask import session, jsonify
from utils.extensions import db
from models import Post, post_schema
from users.user import Admin

class GetPost:

    def get_posts(self, request):

        try:
            if session['logged_in']:
                data = db.session.query(Post).all()
                data = post_schema.dump(data)
                return jsonify(data)
            else:
                return 'Please log in'

        except Exception as e:
            return 'Get posts failed: ' + str(e)

    def get_current_users_posts(self, request):

        try:
            if session['logged_in']:
                data = db.session.query(Post).filter_by(user_id=Admin.USER_ID).all()
                data = post_schema.dump(data)
                return jsonify(data)
            else:
                return 'Please log in'

        except Exception as e:
            return 'Get current users posts failed: ' +str(e)
