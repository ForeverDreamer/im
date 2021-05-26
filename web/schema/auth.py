
from flask import session
from marshmallow import Schema, fields, validate, validates, validates_schema, ValidationError, post_load
import requests as http
from werkzeug.exceptions import Unauthorized

from constant.auth import LOGIN_TYPE
from web.lib.misc import generate_random_id
from db.auth import db_get_wechat_credentials
from db.user import db_find_user, db_create_user


class RegisterSchema(Schema):
    nickname = fields.Str(validate=validate.Length(min=1, max=50), required=True)
    username = fields.Str(validate=validate.Length(min=1, max=50), required=True)
    password = fields.Str(validate=validate.Length(min=6, max=20), required=True)

    @post_load
    def try_create_user(self, data, **kwargs):
        user = db_find_user({'username': data['username']})
        if user:
            raise ValidationError('用户名已存在')
        db_create_user(
            {
                '_id': generate_random_id(),
                'nickname': data['nickname'],
                'username': data['username'],
                'password': data['password']
            }
        )


class AccountLoginSchema(Schema):
    username = fields.Str(validate=validate.Length(min=2, max=50), required=True)
    password = fields.Str(validate=validate.Length(min=6, max=20), required=True)

    @post_load
    def try_login(self, data, **kwargs):
        user = db_find_user({'username': data['username']})
        if user is None:
            raise Unauthorized('用户名或密码错误')
        if user['password'] == data['password']:
            return user
        else:
            raise Unauthorized('用户名或密码错误')


class CellphoneLoginSchema(Schema):
    phone_number = fields.Str(validate=validate.Length(min=1), required=True)
    verification_code = fields.Str(validate=validate.Length(min=1), required=True)

    @post_load
    def try_login(self, data, **kwargs):
        pass


class WechatLoginSchema(Schema):
    code = fields.Str(required=True)
    state = fields.Str(required=True)

    @validates('code')
    def validate_code(self, code):
        if code == '':
            raise ValidationError('用户未授权')

    @validates_schema
    def validate_state(self, data, **kwargs):
        qr_login = session.get('qr_login')
        if qr_login is None or qr_login.get('state') != data['state']:
            return ValidationError(f'state<{data["state"]}>不匹配')
        data['session'] = qr_login
        session.pop('qr_login', None)

    @post_load
    def try_login(self, data, **kwargs):
        credentials = db_get_wechat_credentials()
        credentials.update({'code': data['code'], 'grant_type': 'authorization_code'})
        r = http.get(
            url='https://api.weixin.qq.com/sns/oauth2/access_token',
            params=credentials
        )
        res_data1 = r.json()
        # pp('res_data1: ')
        # pp(res_data1)
        if res_data1.get('errcode'):
            raise ValidationError(f'获取token失败，{res_data1}')
        else:
            credentials = {'access_token': res_data1['access_token'], 'openid': res_data1['openid']}
            r = http.get(
                url='https://api.weixin.qq.com/sns/userinfo',
                params=credentials
            )
            r.encoding = 'utf-8'
            res_data2 = r.json()
            # pp('res_data2: ')
            # pp(res_data2)
            if res_data2.get('errcode'):
                raise ValidationError(f'获取用户信息失败，{res_data2}')
            res_data1.update(res_data2)


login_schemas = {
    LOGIN_TYPE[0]: AccountLoginSchema,
    LOGIN_TYPE[1]: CellphoneLoginSchema,
    LOGIN_TYPE[2]: WechatLoginSchema,
}


class LoginSchema(Schema):
    login_type = fields.Str(validate=validate.OneOf(LOGIN_TYPE), required=True)
    arguments = fields.Dict()

    @post_load
    def try_login(self, data, **kwargs):
        return login_schemas[data['login_type']]().load(data['arguments'])


