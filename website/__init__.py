from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    from models import db, migrate
    db.init_app(app)
    migrate.init_app(app)

    return app
