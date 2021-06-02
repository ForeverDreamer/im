from flask import Flask, render_template, redirect
# from flask_cors import CORS
# from web.extension.websocket import init_websocket
from web.extension.auth import init_auth
from web.extension.restapi import init_restapi
from db.mongodb import init_mongodb
from chat import init_websocket
from web.config import conf

app = Flask(__name__)
app.config.from_mapping(conf['dev'])
# CORS(app)


@app.route('/home')
def im():
    return render_template('client/index.html')


@app.route('/')
def index():
    return redirect('/home')


if __name__ == '__main__':
    init_restapi(app)
    init_auth(app)
    init_mongodb(app)
    socketio = init_websocket(app)
    socketio.run(app, host='0.0.0.0', port=5000)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
