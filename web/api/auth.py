from flask import request
from flask_restx import Namespace, Resource
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import BadRequest, Unauthorized
from marshmallow import ValidationError

from lib.utils import construct_login_info
from schema.auth import AccountLoginSchema
from extension.auth import User

api = Namespace('user: login', description='用户登录')


@api.route('/account_login')
class AccountLogin(Resource):
    @api.response(200, '已登录返回用户信息')
    @api.response(401, '未登录操作提示')
    def get(self):
        """查询是否登录"""
        if current_user.is_authenticated:
            res_data = {
                'msg': '用户已登录',
                'user': construct_login_info(current_user),
            }
        else:
            raise Unauthorized('用户未登录')
        return {'data': res_data}

    @api.response(200, '登录成功返回用户信息')
    @api.response(401, '未登录操作提示')
    def post(self):
        req_data = request.json or {}
        try:
            user = User(AccountLoginSchema().load(req_data))
            login_user(user)
            res_data = {'msg': '登录成功', 'user': construct_login_info(user)}
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
