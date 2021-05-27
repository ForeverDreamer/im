from web.lib.timezone import str_local_time_without_timezone


def construct_login_info(user):
    return {
        'u_id': user['_id'],
        'nickname': user['nickname'],
        'username': user['username'],
        'created_at': str_local_time_without_timezone(user['created_at']),
        'last_login': user['last_login'],
        'rooms': user['rooms'],
    }


def format_room_info(room):
    room['r_id'] = room['_id']
    room['created_at'] = str_local_time_without_timezone(room['created_at'])
    room['updated_at'] = str_local_time_without_timezone(room['updated_at'])
    return room
