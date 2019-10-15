from flask import session
from extensions import db
from models import Post
from admin import Admin

class GetPost:

    def get_posts(request):

        try:
            if session['logged_in']:
                # TODO: use Marshmallow to serialize response. 
                # Currently returning single post, because
                # otherwise it returns list of, well, nothingness...
                posts = db.session.query(Post).first()
                return str(posts.content)
            else:
                return 'Please log in'

        except Exception as e:
            return 'Get posts failed: ' + str(e)

    def get_current_users_posts(request):

        try:
            if session['logged_in']:
                # TODO: use Marshmallow to serialize response. 
                # Currently returning single post, because
                # otherwise it returns list of, well, nothingness...
                posts = db.session.query(Post).filter_by(user_id=Admin.USER_ID).first()
                return str(posts.content)
            else:
                return 'Please log in'

        except Exception as e:
            return 'Get current users posts failed: ' +str(e)
