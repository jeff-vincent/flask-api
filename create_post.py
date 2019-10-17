from flask import session
from models import Post
from admin import Admin
from extensions import db


class CreatePost:

    def create_post(request):

        try:
            if session['logged_in']:
                content = request.form['content']
                new_post = Post(content=content, user_id=Admin.USER_ID)
                db.session.add(new_post)
                db.session.commit()
                return 'New post content: ' + new_post.content
            else: 
                return 'Please log in'
                
        except Exception as e:
            if 'Incorrect integer value:' in str(e):
                return 'Please log in'
            return 'Create post failed. Error Code: ' + str(e)

