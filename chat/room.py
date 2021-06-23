from flask_socketio import emit

from db.user import db_update_user


def chat_enter_room(u_id, r_id):
    db_update_user({'_id': u_id}, {'$addToSet': {'rooms': r_id}, '$set': {'current_r_id': r_id}})
    emit('enter_room', to=r_id)


def chat_leave_room(u_id, r_id):
    db_update_user(
        {'_id': u_id},
        {'$pull': {'rooms': r_id}, '$set': {'current_r_id': 'e99dbbd8-747f-4eae-8582-0b31395fa368'}}
    )
    emit('leave_room')
