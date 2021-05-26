from constant.user import STATUS
from db.user import db_update_user
from chat.message import broadcast_message


def chat_online(user, r_id):
    db_update_user({'_id': user['_id']}, {'$set': {'status': STATUS[0], 'self_room': r_id}})
    broadcast_message({'r_id': 'room1', 'msg': f'{user["nickname"]} 上线了'})


def chat_enter_room(u_id, r_id):
    db_update_user({'_id': u_id}, {'$addToSet': {'rooms': r_id}})


def chat_leave_room(u_id, r_id):
    db_update_user({'_id': u_id}, {'$pull': {'rooms': r_id}})
