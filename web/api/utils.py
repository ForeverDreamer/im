from schema.utils import format_room_info
from db.room import db_find_room


def get_rooms(rooms):
    return [format_room_info(room) for room in db_find_room({'_id': {'$in': rooms}}, many=True)]
