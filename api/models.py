from utils.extensions import db
from marshmallow import Schema, fields

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # admin = db.Column(db.Boolean(), nullable=True)
    # posts = db.Column(db)

    def __repr__(self):
        return '<User %r>' % self.email

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'email', 'password')

user_schema = UserSchema(many=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.id

class PostSchema(Schema):
    class Meta:
        fields = ('id', 'content', 'user_id')

post_schema = PostSchema(many=True)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.id

class FileSchema(Schema):
    class Meta:
        fields = ('id', 'filename', 'user_id')

file_schema = FileSchema(many=True)
