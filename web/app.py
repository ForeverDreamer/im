from flask import Flask, render_template
# from flask_cors import CORS
from extension.websocket import init_app


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# CORS(app)


@app.route('/')
def hello_world():
    return render_template('server/index.html')


if __name__ == '__main__':
    init_app(app).run(app, host='0.0.0.0', port=5000)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
