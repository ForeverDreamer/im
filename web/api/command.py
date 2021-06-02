import json
from json.decoder import JSONDecodeError

from flask import request, redirect
from flask_restx import Namespace, Resource
from werkzeug.exceptions import BadRequest, ServiceUnavailable
from marshmallow import ValidationError
from flask_login import login_required
from werkzeug.exceptions import Forbidden

from schema.command.entrance import CommandSchema

api = Namespace(name='command api', description='通用操作命令')


@api.route('/')
class Command(Resource):
    @api.response(200, '返回相应数据')
    @api.response(400, '请求参数错误详细信息')
    @api.response(401, '未登录操作提示')
    @api.response(403, '没有操作权限')
    @api.response(503, '服务器内部错误')
    @login_required
    def post(self):
        """通用命令接口"""
        req_data = request.json or dict(request.form)
        req_data['params'] = req_data.get('params') or {}
        try:
            res_data = CommandSchema().load(req_data)
        except ValidationError as err:
            api.logger.error(str(err.messages))
            raise BadRequest(err.messages)
        except Forbidden as err:
            api.logger.error(str(err))
            raise
        except ServiceUnavailable as err:
            api.logger.error(str(err))
            raise

        return {'data': res_data}
