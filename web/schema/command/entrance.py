import traceback

from marshmallow import Schema, fields, post_load, ValidationError

from schema.command.cmd import CMDS


class CommandSchema(Schema):
    cmd = fields.Str(required=True)
    params = fields.Dict(required=True)
    accessory = fields.List(fields.Raw())

    @post_load
    def execute(self, data, **kwargs):
        try:
            res_data = CMDS[data['cmd']](data)
        except KeyError as err:
            print('====================================')
            traceback.print_tb(err.__traceback__)
            # print(traceback.format_tb(err.__traceback__))
            print('====================================')
            raise ValidationError(f'<{data["cmd"]}>命令不存在!')

        return res_data
