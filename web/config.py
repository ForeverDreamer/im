import os


# base = {
#     'BASE_DIR': os.path.abspath(os.path.dirname(__file__)),
#
# }

# import urllib
# user = urllib.parse.quote_plus('root')
# password = urllib.parse.quote_plus('Root@1234.')
# print(user, password)

dev = {
    'BASE_DIR': os.path.abspath(os.path.dirname(__file__)),
    'SECRET_KEY': 'dev_secret',
    'MONGO_URI': 'mongodb://root:Root%401234.@192.168.71.20:7091/im?authSource=admin',
    'HOST_DOMAIN': 'http://127.0.0.1',
    'COS_DOMAIN': '/backend/static',
    # 'COS_DOMAIN': '/static',
    'BOT': {
        'url': 'http://localhost:5005/webhooks/rest/webhook',
        'username': 'rasa',
    }
}

prod = {
    'BASE_DIR': os.path.abspath(os.path.dirname(__file__)),
    'SECRET_KEY': 'prod_secret',
    'MONGO_URI': 'mongodb://root:Root%401234.@192.168.71.20:7091/im?authSource=admin',
    'HOST_DOMAIN': 'https://127.0.0.1',
    'COS_DOMAIN': 'https://127.0.0.1/static',
    'BOT': {
        'url': 'http://localhost:5005/webhooks/rest/webhook',
        'username': 'rasa',
    }
}


conf = {'dev': dev, 'prod': prod}
