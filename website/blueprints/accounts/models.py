from website.database import db
from passlib.apps import custom_app_context as flask_user_context
class User(db.Model):
    __tablename__     = 'user'
    id                = db.Column(db.Integer, primary_key = True)
    username          = db.Column(db.String(80), unique   = True, nullable = False)
    email             = db.Column(db.String(120), unique  = True, nullable = False)
    obj               = db.Column(db.JSON)
    description       = db.Column(db.String(500))
    password          = db.Column(db.String(255))
    posts             = db.relationship('Post')

    def hash_pass(self, password):
        self.password = flask_user_context.hash(password)

    def verify_pass(self, password):
        return flask_user_context.verify(password, self.password)

    def __repr__(self):
        return '<User: %r>' % self.username

