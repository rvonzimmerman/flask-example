from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    from website.database import db, migrate
    from website.blueprints.blog.models import Post
    from website.blueprints.accounts.models import User
    from website.blueprints.blog.blog import blog
    from website.blueprints.accounts.accounts import accounts
    app.register_blueprint(accounts)
    app.register_blueprint(blog)
    migrate.init_app(app, db)
    db.init_app(app)

    return app

def create_db_session(config_filename = None):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    from website.database import db, migrate
    from website.blueprints.blog.models import Post
    from website.blueprints.blog.models import User
    from website.blueprints.blog.blog import blog
    app.register_blueprint(blog)
    migrate.init_app(app, db)
    db.init_app(app)
    return db
