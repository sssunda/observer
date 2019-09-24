from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
soc_io = SocketIO(app)

@app.route('/')
def index():
    return "This is observer's server"

@soc_io.on("connect")
def connect():
    print('success to connect')

@soc_io.on("message")
def handle_message(message):
    print(message)

if __name__ == '__main__':
    soc_io.run(app)