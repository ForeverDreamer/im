from db.mongodb import mongo
from web.lib.timezone import utc_time
from constant.user import TYPE, ROLES, STATUS

col_name = 'user'
query = {'active': True}


def db_find_user(q, p=None, many=False):
    q.update(query)
    if many:
        return mongo.db[col_name].find(q, p)
    else:
        return mongo.db[col_name].find_one(q, p)


def db_create_user(user):
    t = utc_time()
    extra_info = {
        'created_at': t,
        'updated_at': t,
        'type': TYPE[0],
        'active': True,
        'status': STATUS[1],
        'last_login': None,
        'roles': [ROLES[1]],
        'rooms': [],
        'self_room': None,
    }
    user.update(extra_info)
    mongo.db[col_name].insert_one(user)


def db_update_user(q, u):
    q.update(query)
    mongo.db[col_name].update_one(q, u)


def db_enter_room(u_id, r_id):
    q = query.copy()
    q.update({'_id': u_id})
    mongo.db[col_name].update_one(q, {'$addToSet': {'rooms', r_id}})


def db_update_self_room(u_id, r_id=None):
    q = query.copy()
    q.update({'_id': u_id})
    mongo.db[col_name].update_one(q, {'$set': {'self_room', r_id}})
