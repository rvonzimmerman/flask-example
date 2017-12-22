from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    from database import db, migrate
    from blueprints.blog.blog import blog
    app.register_blueprint(blog)
    db.init_app(app)
    migrate.init_app(app)

    return app
