from flask import request
from flask_restx import Namespace, Resource
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import BadRequest, Unauthorized
from marshmallow import ValidationError

from web.schema.utils import format_user_info
from web.schema.auth import RegisterSchema, LoginSchema
from web.extension.auth import User
from web.api.utils import get_rooms

api = Namespace('auth', description='权限验证')


@api.route('/register')
class Register(Resource):
    """用户注册"""
    @api.response(200, '登录成功返回用户信息')
    @api.response(400, '参数错误提示')
    def post(self):
        req_data = request.json or {}
        try:
            user = RegisterSchema().load(req_data)
        except ValidationError as err:
            api.logger.error(str(err.messages))
            raise BadRequest(err.messages)
        except Unauthorized as err:
            api.logger.error(str(err))
            raise
        return {'data': {'msg': '注册成功', 'user': user}}


@api.route('/login')
class Login(Resource):
    @api.response(200, '已登录返回用户信息')
    @api.response(401, '未登录操作提示')
    def get(self):
        """查询是否登录"""
        if current_user.is_authenticated:
            res_data = {
                'msg': '用户已登录',
                'user': format_user_info(current_user.info),
                'rooms': get_rooms(current_user.info['rooms']),
            }
        else:
            raise Unauthorized('用户未登录')
        return {'data': res_data}

    @api.response(200, '登录成功返回用户信息')
    @api.response(400, '参数错误提示')
    @api.response(401, '登录信息错误提示')
    def post(self):
        req_data = request.json or {}
        try:
            user = User(LoginSchema().load(req_data))
            login_user(user)
            res_data = {'msg': '登录成功'}
        except ValidationError as err:
            api.logger.error(str(err.messages))
            raise BadRequest(err.messages)
        except Unauthorized as err:
            api.logger.error(str(err))
            raise
        return {'data': res_data}

    @api.doc(description='系统用户退出登录')
    @api.response(200, '操作成功返回数据')
    @api.response(401, '未登录操作提示')
    @login_required
    def delete(self):
        logout_user()
        return {'data': {'msg': '登出成功'}}, 200
