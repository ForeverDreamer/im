from flask import Flask, render_template, redirect
# from flask_cors import CORS
from extension.websocket import init_websocket
from extension.auth import init_auth
from extension.restapi import init_restapi
from extension.mongodb import init_mongodb


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# import urllib
# user = urllib.parse.quote_plus('root')
# password = urllib.parse.quote_plus('Root@1234.')
# print(user, password)
app.config['MONGO_URI'] = 'mongodb://root:Root%401234.@192.168.71.20:7091/im?authSource=admin'
# CORS(app)


@app.route('/im')
def im():
    return render_template('client/index.html')


@app.route('/')
def index():
    return redirect('/im')


if __name__ == '__main__':
    init_restapi(app)
    init_auth(app)
    init_mongodb(app)
    socketio = init_websocket(app)
    socketio.run(app, host='0.0.0.0', port=5000)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
