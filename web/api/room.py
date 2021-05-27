from flask import request
from flask_restx import Namespace, Resource
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import BadRequest, Unauthorized
from marshmallow import ValidationError

from web.schema.utils import construct_login_info
from web.schema.room import CreateRoomSchema, QueryRoomSchema
from web.extension.auth import User

api = Namespace('auth', description='权限验证')


@api.route('/')
class Login(Resource):
    """查询房间"""
    @api.response(200, '返回单个或多个房间详情',)
    @api.response(400, '请求参数错误详细信息')
    @api.response(401, '未登录操作提示')
    @login_required
    def get(self):
        """查询收藏夹"""
        req_data = dict(request.args)
        try:
            res_data = QueryRoomSchema().load(req_data)
        except ValidationError as err:
            api.logger.error(str(err.messages))
            raise BadRequest(err.messages)
        res_data.update({'msg': '房间创建成功'})
        return {'data': res_data}

    """创建房间"""
    @api.response(200, '创建成功返回房间信息')
    @api.response(400, '参数错误提示')
    @api.response(401, '未登录操作提示')
    @login_required
    def post(self):
        req_data = request.json or {}
        try:
            room = CreateRoomSchema().load(req_data)
        except ValidationError as err:
            api.logger.error(str(err.messages))
            raise BadRequest(err.messages)
        return {'data': {'msg': '房间创建成功', 'room': room}}