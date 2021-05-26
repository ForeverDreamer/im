from flask_socketio import SocketIO, send, emit, join_room, leave_room


def read_receipt_cb():
    # 数据库插入消息已读的记录
    print('message was received!')


def send_message_to_room(data, r_id, cb=read_receipt_cb):
    emit('data', data, to=r_id, callback=cb)


def broadcast_message(data):
    emit('data', data, broadcast=True)


def send_error_message(err):
    emit('error', err)
