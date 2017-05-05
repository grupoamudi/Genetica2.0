from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import numpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weoijhgsdlkjfwelkr20943091d98asokolfqeoi"!!?qw?sda/~dwqp1deo'
socketio = SocketIO(app)

clients = []

@app.route('/')
def index():
    return render_template('index.html')

@app.before_first_request
def init_program():
    pass

@socketio.on('vote')
def handle_vote(json):
    print("aaa")
    console.log('recieved vote')
    pass

@socketio.on('connect')
def connected():
    print("Client Connected")
    clients.append(request.namespace)

@socketio.on('disconnect')
def disconnected():
    print("Client Disconnected")
    clients.remove(request.namespace)

if __name__ == '__main__':
    import thread, time
    import glob, os
    
    thread.start_new_thread(lambda: socketio.run(app))
    
    # Searches for individuals
    for file in glob.glob("*.bin"):
        print(file)
    # If not creates individuals
    # Start mutating at slow rate
