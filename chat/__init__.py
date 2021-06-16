from flask_socketio import SocketIO
from .event import register_events


def init_websocket(app):
    socketio = SocketIO(
        app,
        cors_allowed_origins="*",
        # path='/chat/',
        serveClient=False,
        logger=True,
        engineio_logger=True,
    )
    register_events(socketio)
    return socketio
