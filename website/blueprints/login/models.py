from website.database import db
class User(db.Model):
    __tablename__     = 'user'
    id                = db.Column(db.Integer, primary_key = True)
    username          = db.Column(db.String(80), unique   = True, nullable = False)
    email             = db.Column(db.String(120), unique  = True, nullable = False)
    obj               = db.Column(db.JSON)
    post              = db.relationship('post')
    description       = db.Column(db.String(500))

    def __repr__(self):
        return '<User: %r>' % self.username

