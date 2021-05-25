from marshmallow import Schema, fields, validate, post_load
from werkzeug.exceptions import Unauthorized

from dao.user import find_user_by_username
from lib.utils import construct_login_info


class AccountLoginSchema(Schema):
    username = fields.Str(validate=validate.Length(min=2, max=50), required=True)
    password = fields.Str(validate=validate.Length(min=6, max=20), required=True)

    @post_load
    def try_login(self, data, **kwargs):
        user = find_user_by_username(data['username'])
        if user is None:
            raise Unauthorized('用户名或密码错误')
        if user['password'] == data['password']:
            return user
        else:
            raise Unauthorized('用户名或密码错误')
