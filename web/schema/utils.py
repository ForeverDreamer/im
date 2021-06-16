from flask import current_app

from web.lib.timezone import str_local_time_without_timezone


def format_user_info(user):
    return {
        'u_id': user['_id'],
        'nickname': user['nickname'],
        'username': user['username'],
        'avatar': f'{current_app.config["COS_DOMAIN"]}/asset/room/1.jpg',
        'created_at': str_local_time_without_timezone(user['created_at']),
        'last_login': user['last_login'],
        'rooms': user['rooms'],
        'current_r_id': user['current_r_id']
    }


def format_room_info(room):
    room['r_id'] = room['_id']
    room['created_at'] = str_local_time_without_timezone(room['created_at'])
    room['updated_at'] = str_local_time_without_timezone(room['updated_at'])
    room['avatar'] = f'{current_app.config["COS_DOMAIN"]}/asset/room/1.jpg'
    return room


def format_message_info(msg):
    msg['m_id'] = msg['_id']
    msg['created_at'] = str_local_time_without_timezone(msg['created_at'])
    msg['updated_at'] = str_local_time_without_timezone(msg['updated_at'])
    return msg
