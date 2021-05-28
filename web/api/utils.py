from schema.utils import format_room_info
from db.room import db_find_room


def get_rooms_by_owner(owner):
    return [format_room_info(room) for room in db_find_room({'owner': owner}, many=True)]