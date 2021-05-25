users = {
    'lsl1': {'username': 'lsl1', 'password': '123456', 'rooms': []},
    'lsl2': {'username': 'lsl2', 'password': '123456', 'rooms': []},
    'lsl3': {'username': 'lsl3', 'password': '123456', 'rooms': []},
}


def find_user_by_username(username):
    return users.get(username)
