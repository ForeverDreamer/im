from flask_login import current_user

from db.mongodb import mongo
from web.lib.timezone import utc_time
from web.lib.misc import generate_random_id

col_name = 'room'
query = {'active': True}


def db_create_room(room):
    t = utc_time()
    user = current_user.info
    extra_info = {
        '_id': generate_random_id(),
        'created_by': user['username'],
        'owner': user['username'],
        'managers': [],
        'created_at': t,
        'updated_at': t,
        'type': room.pop('r_type'),
        'active': True,
        'user_count': 1,
        'usernames': [user['username']],
        'msg_count': 0,
        'last_msg': None,
    }
    room.update(extra_info)
    mongo.db[col_name].insert_one(room)
    return db_find_room({'name': room['name']})


def db_find_room(q, p=None, many=False):
    q.update(query)
    if many:
        return mongo.db[col_name].find(q, p)
    else:
        return mongo.db[col_name].find_one(q, p)
