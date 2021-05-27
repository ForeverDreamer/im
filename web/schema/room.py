from flask_login import current_user

from marshmallow import Schema, fields, validate, validates, validates_schema, ValidationError, post_load

from constant.room import ROOM_TYPE
from db.room import db_find_room, db_create_room
from web.schema.utils import format_room_info


class QueryRoomSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1, max=50))

    @post_load
    def query_favorite(self, data, **kwargs):
        if data.get('r_id'):
            data['_id'] = data.pop('r_id')
            return {'room': format_room_info(db_find_room(data))}
        else:
            data['owner'] = current_user.info['username']
            return {'rooms': [format_room_info(room) for room in db_find_room(data, many=True)]}


class CreateRoomSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1, max=50), required=True)
    r_type = fields.Str(validate=validate.OneOf(ROOM_TYPE), required=True)
    description = fields.Str(required=True)

    @post_load
    def try_create_room(self, data, **kwargs):
        user = db_find_room({'name': data['name']})
        if user:
            raise ValidationError('房间名已存在')
        return format_room_info(db_create_room(data))
