from schema.utils import format_message_info
from schema.command.params import QueryMessageSchema
from db.message import db_query_message


def query_message(data):
    return [format_message_info(msg) for msg in db_query_message(data['params'])]


CMDS = {
    'query_message': query_message,
}
