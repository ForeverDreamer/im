from flask_socketio import SocketIO
from .event import register_events


def init_websocket(app):
    socketio = SocketIO(
        app,
        cors_allowed_origins="*",
        # path='/chat/',
        serveClient=False
    )
    register_events(socketio)
    return socketio
