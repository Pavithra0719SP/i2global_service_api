from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

mongo = PyMongo()
bcript = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.Config')
    mongo.init_app(app)
    bcript.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

    from api.auth.routes import api_bp
    from api.nots.routes import api_bp as nots_bp
    
    app.register_blueprint(nots_bp, url_prefix='/api')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
    