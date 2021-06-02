import traceback

from marshmallow import Schema, fields, post_load, ValidationError

from db.message import db_query_message


class QueryMessageSchema(Schema):
    q = fields.Dict(required=True)
    # p = fields.Dict(required=True)

    @post_load
    def execute(self, data, **kwargs):
        return db_query_message(data)
