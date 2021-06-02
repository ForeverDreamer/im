from constant.user import USER_STATUS
from db.user import db_update_user
from chat.message import broadcast_message, send_message_to_room


def chat_online(user, s_r_id):
    db_update_user({'_id': user['_id']}, {'$set': {'status': USER_STATUS[0], 'self_room': s_r_id}})
    # send_message_to_room({'r_id': 'self', 'msg': f'{user["nickname"]} 上线'}, s_r_id)


def chat_offline(user, s_r_id):
    db_update_user({'_id': user['_id']}, {'$set': {'status': USER_STATUS[1], 'self_room': None}})
    # send_message_to_room({'r_id': 'self', 'msg': f'{user["nickname"]} 下线'}, s_r_id)

