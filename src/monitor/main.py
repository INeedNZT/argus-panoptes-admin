from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send,  join_room, leave_room
from threading import Thread, Lock
import string
import random
import os
import dotenv


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


MONITOR_ROOM = 'monitor_group'
USER_ROOM = 'user_group'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


def send_join(room):
    emit('join', to=room)


def send_sdp(room, sdp):
    emit('sdp', sdp, to=room)


@socketio.on('connect', namespace='/signaling')
def connect(auth):
    # if not self.authenticate(request.args):
    print(auth)

    print('建立连接')


@socketio.on('disconnect', namespace='/signaling')
def disconnect():
    print('客户端断开连接')


@socketio.on('message', namespace='/signaling')
def message(data):
    print(444444444444444444)
    # emit('my response', {'data': 'Connected'})
    print('received message: ' + data)


@socketio.on('join', namespace='/signaling')
def join(data):
    pass
    # if auth:
    #     join_room(MONITOR_ROOM)
    #     send_join(USER_ROOM)

    # if not auth:
    #     join_room(USER_ROOM)
    #     send_join(MONITOR_ROOM)



if __name__ == '__main__':
   dotenv.load_dotenv('.flaskenv')
   print(os.getenv('FLASK_RUN_HOST'))
   socketio.run(app, host =os.getenv('FLASK_RUN_HOST'), port=os.getenv('FLASK_RUN_PORT'))
