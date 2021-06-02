from flask_login import current_user

from db.mongodb import mongo
from web.lib.timezone import utc_time
from web.lib.misc import generate_random_id

col_name = 'message'


def db_new_message(msg):
    t = utc_time()
    extra_info = {
        '_id': generate_random_id(),
        'type': '',
        'created_at': t,
        'updated_at': t,
        'user': {
            'u_id': current_user.info['_id'],
            'username': current_user.info['username'],
        }
    }
    msg.update(extra_info)
    mongo.db[col_name].insert_one(msg)


def db_query_message(q, p=None):
    return mongo.db[col_name].find(q, p)
