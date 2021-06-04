from flask import Blueprint
from flask_restx import Api

from web.api.auth import api as auth
from web.api.wechat import api as wechat
from web.api.room import api as room
from web.api.command import api as cmd
from web.api.bot import api as bot

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
api.add_namespace(wechat, path='/wechat')
api.add_namespace(room, path='/room')
api.add_namespace(cmd, path='/cmd')
api.add_namespace(bot, path='/bot')


def init_restapi(app):
    app.register_blueprint(blueprint)
