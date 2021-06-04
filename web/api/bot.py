from flask import request
from flask_restx import Namespace, Resource
from flask_login import login_required

from chat.message import bot_message_to_room

api = Namespace('auth', description='权限验证')


@api.route('/reply')
class Bot(Resource):
    """第三方智能问答助理操作接口"""
    @api.response(200, '操作成功返回数据')
    @api.response(400, '参数错误提示')
    @api.response(401, '未登录操作提示')
    def post(self):
        req_data = request.json or {}
        print(req_data)
        sender, r_id = req_data['recipient_id'].split('@')
        bot_message_to_room({'r_id': r_id, 'msg': req_data['text']})
        return {'data': {'msg': 'success'}}
