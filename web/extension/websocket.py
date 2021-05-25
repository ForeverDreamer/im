import traceback
from pprint import pprint as pp

from flask import request
from flask_login import current_user
from flask_socketio import SocketIO, join_room, leave_room

from lib.message import send_message_to_room, broadcast_message
from extension.auth import authenticated_only
from extension.mongodb import mongo


from dao.user import users


def register_events(si):
    @si.on('status', namespace='/events')
    def events_message(message):
        print('状态: ', message)

    @si.on('data', namespace='/events')
    def events_data(data):
        print(data)

    @si.on('join_room', namespace='/events')
    def on_join(data):
        # print(data)
        username = data['username']
        room = data['room']
        mongo.db['user'].insert_one({'username': username, 'room': room})
        join_room(room)
        send_message_to_room({'msg': username + f' has entered the {data["room"]}.'}, room)
        send_message_to_room({'msg': username + f' has entered the {request.sid}.'}, request.sid)

    @si.on('leave_room', namespace='/events')
    def on_leave(data):
        username = data['username']
        room = data['room']
        leave_room(room)

    @si.on('connect', namespace='/events')
    @authenticated_only
    # @login_required
    def events_connect(*args, **kwargs):
        # print(args)
        # print(kwargs)
        # print(f'{request.sid} 连接')
        pp(current_user.info)
        # users[request.sid] = {'rooms': [request.sid]}
        # pp(users)
        broadcast_message({'msg': f'{current_user.info["username"]} 上线了'})

    @si.on('disconnect', namespace='/events')
    def events_disconnect():
        print(f'{request.sid}断开连接')

    # @si.on_error('/events')  # handles the '/events' namespace
    # def error_handler_chat(e):
    #     traceback.print_tb(e.__traceback__)
    #     raise


def init_websocket(app):
    socketio = SocketIO(
        app,
        cors_allowed_origins="*",
        # path='/chat/',
        serveClient=False
    )
    register_events(socketio)
    return socketio
