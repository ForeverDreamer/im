from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def hello_world():
    return render_template('server/index.html')


@socketio.on('status', namespace='/events')
def events_message(message):
    print('状态: ', message)


@socketio.on('data', namespace='/events')
def events_data(data):
    print(data)
    emit('data', data)


@socketio.on('connect', namespace='/events')
def events_connect(*arg, **kwargs):
    print('连接')
    print(arg)
    print(kwargs)
    emit('data', '欢迎访问')


@socketio.on('disconnect', namespace='/events')
def events_disconnect():
    print('断开连接')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
