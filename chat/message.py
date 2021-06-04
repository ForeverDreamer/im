from flask import current_app
from flask_socketio import SocketIO, send, emit, join_room, leave_room

from db.message import db_new_message
from chat.utils import get_bot_reply


def read_receipt_cb():
    # 数据库插入消息已读的记录
    print('message was received!')


def send_message_to_room(msg, cb=read_receipt_cb):
    emit('msg', msg['msg'], to=msg['r_id'], callback=cb)
    db_new_message(msg)
    # if msg['msg'].startswith('@bot '):
    #     msg['msg'] = msg['msg'][5:]
    #     get_bot_reply(msg)
        # msg['msg'] = get_bot_reply(msg['msg'][5:])
        # msg['user']['u_id'] = 'rasa_bot_id'
        # msg['user']['username'] = current_app.config['BOT']['username']
        # emit('msg', msg['msg'], to=msg['r_id'], callback=cb)
        # db_new_message(msg)


def broadcast_message(msg):
    emit('msg', msg, broadcast=True)
    db_new_message(msg)


def send_error_message(err):
    emit('error', err)


def bot_message_to_room(msg):
    msg['msg'] = msg['msg'][5:]
    msg['msg'] = get_bot_reply(msg)
    msg['user'] = {'u_id': 'rasa_bot_id', 'username': current_app.config['BOT']['username']}
    # This is a function that can only be called from a SocketIO event handler,
    # as in obtains some information from the current client context
    emit('msg', msg['msg'], to=msg['r_id'])
    db_new_message(msg)
