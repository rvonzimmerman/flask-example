from flask import current_app, Blueprint, request
from flask_restful import Api, Resource, url_for, abort
from flask_jwt_simple import JWTManager, create_jwt, get_jwt_identity, jwt_required
from .models import User
from website.database import db

accounts = Blueprint('accounts', __name__,
                  url_prefix = '/accounts')
api = Api(accounts)
jwt = JWTManager()

class Login(Resource):
    @jwt_required
    def get(self):
        return {"Identity" : get_jwt_identity()}

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            abort(400)

        user = User.query.filter_by(username = username).first()
        if user is None:
            abort(400)

        if user.verify_pass(password):
            return {'auth': create_jwt(identity=username)}
        else:
            abort(401)


class Create(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        email    = request.json.get('email')
        if username is None or password is None:
            abort(400)
        if User.query.filter_by(username = username).first() is not None:
            abort(400)

        user = User(username = username, email = email)
        user.hash_pass(password)
        db.session.add(user)
        db.session.commit()





api.add_resource(Login, '/login')
api.add_resource(Create, '/create')
