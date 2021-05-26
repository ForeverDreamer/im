from flask import request, redirect
from flask_restx import Namespace, Resource
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from web.schema.auth import LoginSchema
from constant.auth import LOGIN_TYPE

api = Namespace(name='wechat', description='微信扫码登录')


@api.route('/')
class WeChat(Resource):

    @api.response(200, '操作成功或失败描述')
    @api.response(400, '请求参数错误详细信息')
    def get(self):
        """微信扫码回调"""
        # pp(request.remote_addr)
        req_data = dict(request.args)
        # pp('req_data: ')
        # pp(req_data)
        req_data['code'] = req_data.get('code') or ''
        data = {'login_type': LOGIN_TYPE[2], 'arguments': req_data}
        try:
            action = LoginSchema().load(req_data)
        except ValidationError as err:
            api.logger.error(str(err.messages))
            raise BadRequest(err.messages)

        return redirect('http://www.baidu.com')
