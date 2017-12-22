from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate(None, db)

class User(db.Model):
    __tablename__ = 'user'
    id            = db.Column(db.Integer, primary_key = True)
    username      = db.Column(db.String(80), unique   = True, nullable = False)
    email         = db.Column(db.String(120), unique  = True, nullable = False)
    obj           = db.Column(db.JSON)

    def __repr__(self):
        return '<User: %r>' % self.username


