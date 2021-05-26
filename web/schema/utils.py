from web.lib.timezone import str_local_time_without_timezone


def construct_login_info(user):
    info = user.info
    return {
        'u_id': info['_id'],
        'nickname': info['nickname'],
        'username': info['username'],
        'created_at': str_local_time_without_timezone(info['created_at']),
        'last_login': info['last_login'],
        'rooms': info['rooms'],
    }
