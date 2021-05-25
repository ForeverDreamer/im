from flask import Blueprint
from flask_restx import Api

from api.auth import api as auth

blueprint = Blueprint('rest api',
                      __name__,
                      url_prefix='/v1',
                      static_folder='static')

api = Api(
    blueprint,
    title='im rest api',
    version='0.1',
    description='即时通信软件rest api',
    validate=False,
    # doc='/api'
    # All API metadatas
)

api.add_namespace(auth, path='/auth')


def init_restapi(app):
    app.register_blueprint(blueprint)
