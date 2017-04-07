from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, request

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
    pass

@socketio.on('connect')
def connected():
    clients.append(request.namespace)

@socketio.on('disconnect')
def disconnected():
    clients.remove(request.namespace)

if __name__ == '__main__':
    import thread, time
    thread.start_new_thread(lambda: socketio.run(app))

    # Searches for individuals
    # If not creates individuals
    # Start mutating at slow rate
