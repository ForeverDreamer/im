from pprint import pprint as pp

from flask import request
from flask_login import current_user
from flask_socketio import SocketIO, join_room, leave_room

from chat.message import send_message_to_room, broadcast_message
from web.extension.auth import authenticated_only
from chat.user import chat_online, chat_offline, chat_enter_room, chat_leave_room


ns_events = '/events'


def register_events(si):
    @si.on('data', namespace=ns_events)
    def on_data(data):
        r_id = data['r_id']
        msg = data['msg']
        send_message_to_room({'r_id': r_id, 'msg': f'{current_user.info["nickname"]}说: {msg}'}, r_id)

    @si.on('enter_room', namespace=ns_events)
    def on_enter_room(data):
        r_id = data['r_id']
        join_room(r_id)
        chat_enter_room(current_user.info["_id"], r_id)
        send_message_to_room({'r_id': r_id, 'msg': f'{current_user.info["nickname"]}进入了房间'}, r_id)

    @si.on('leave_room', namespace=ns_events)
    def on_leave_room(data):
        r_id = data['r_id']
        leave_room(r_id)
        chat_leave_room(current_user.info["_id"], r_id)
        send_message_to_room({'r_id': r_id, 'msg': f'{current_user.info["nickname"]}离开了房间'}, r_id)

    @si.on('connect', namespace=ns_events)
    @authenticated_only
    def on_connect():
        # pp(current_user.info)
        for r_id in current_user.info['rooms']:
            join_room(r_id)
        chat_online(current_user.info, request.sid)

    @si.on('disconnect', namespace=ns_events)
    @authenticated_only
    def on_disconnect():
        chat_offline(current_user.info, request.sid)

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
