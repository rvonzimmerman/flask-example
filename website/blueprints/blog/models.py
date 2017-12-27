from website.database import db

class Post(db.Model):
    __tablename__ = 'post'
    id            = db.Column(db.Integer, primary_key = True)
    date          = db.Column(db.Date)
    title         = db.Column(db.String(50))
    author        = db.Column(db.Integer, db.ForeignKey('user.id'))
    content       = db.Column(db.String(500))
    category      = db.Column(db.String(20))

