from flask import Flask
from flask_jwt_extended import JWTManager
import app.config.config
from app.views import Urls

def create_app(config=None):
    """
    Method create a flask object
    :param config: None
    :return: app
    """
    app = Flask(__name__)
    app.config.update(config.__dict__ or {})
    Urls.generate(app)
    return app
app1 = create_app(config=app.config.config.DevelopmentConfig)
app1.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app1)
