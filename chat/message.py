from flask_login import current_user

from flask_socketio import SocketIO, send, emit, join_room, leave_room
from db.message import db_new_message


def read_receipt_cb():
    # 数据库插入消息已读的记录
    print('message was received!')


def send_message_to_room(msg, cb=read_receipt_cb):
    emit('msg', msg['msg'], to=msg['r_id'], callback=cb)
    db_new_message(msg)


def broadcast_message(msg):
    emit('msg', msg, broadcast=True)
    db_new_message(msg)


def send_error_message(err):
    emit('error', err)
