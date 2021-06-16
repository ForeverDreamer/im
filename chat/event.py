from pprint import pprint as pp

from flask import request
from flask_login import current_user
from flask_socketio import SocketIO, join_room, leave_room

from .message import send_message_to_room, bot_message_to_room
from web.extension.auth import authenticated_only
from .user import chat_online, chat_offline
from .room import chat_enter_room, chat_leave_room


ns_events = '/events'


def register_events(socketio):
    @socketio.on('msg', namespace=ns_events)
    def on_msg(data):
        send_message_to_room(data)

    @socketio.on('msg_bot', namespace=ns_events)
    def on_msg(data):
        bot_message_to_room(data)

    @socketio.on('enter_room', namespace=ns_events)
    def on_enter_room(data):
        r_id = data['r_id']
        join_room(r_id)
        chat_enter_room(current_user.info["_id"], r_id)
        # send_message_to_room({'r_id': r_id, 'msg': f'{current_user.info["nickname"]}进入了房间{r_id}'})

    @socketio.on('leave_room', namespace=ns_events)
    def on_leave_room(data):
        r_id = data['r_id']
        leave_room(r_id)
        chat_leave_room(current_user.info["_id"], r_id)
        # send_message_to_room({'r_id': r_id, 'msg': f'{current_user.info["nickname"]}离开了房间{r_id}'})

    @socketio.on('connect', namespace=ns_events)
    @authenticated_only
    def on_connect():
        # pp(current_user.info)
        for r_id in current_user.info['rooms']:
            join_room(r_id)
        chat_online(current_user.info, request.sid)

    @socketio.on('disconnect', namespace=ns_events)
    @authenticated_only
    def on_disconnect():
        for r_id in current_user.info['rooms']:
            leave_room(r_id)
        chat_offline(current_user.info, request.sid)

    # @si.on_error('/events')  # handles the '/events' namespace
    # def error_handler_chat(e):
    #     traceback.print_tb(e.__traceback__)
    #     raise


# def init_websocket(app):
#     socketio = SocketIO(
#         app,
#         cors_allowed_origins="*",
#         # path='/chat/',
#         serveClient=False
#     )
#     register_events(socketio)
#     return socketio
