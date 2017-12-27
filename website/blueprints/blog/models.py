from website.database import db
class User(db.Model):
    __tablename__ = 'user'
    id            = db.Column(db.Integer, primary_key = True)
    username      = db.Column(db.String(80), unique   = True, nullable = False)
    email         = db.Column(db.String(120), unique  = True, nullable = False)
    obj           = db.Column(db.JSON)

    def __repr__(self):
        return '<User: %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post'
    id            = db.Column(db.Integer, primary_key = True)
    date          = db.Column(db.Date)
    title         = db.Column(db.String(50))
    content       = db.Column(db.String(500))
    category      = db.Column(db.String(20))

