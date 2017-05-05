from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import numpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weoijhgsdlkjfwelkr20943091d98asokolfqeoi"!!?qw?sda/~dwqp1deo'
socketio = SocketIO(app)

clients = []
individuos = ["1", "2", "3", "4"]  # TODO: Fix
# Init vote_stash
vote_stash = {};
for i,individuo in enumerate(individuos):
    vote_stash[i+1] = 0;
print(vote_stash)

@app.route('/')
def index():
    return render_template('index.html')

@app.before_first_request
def init_program():
    pass

@socketio.on('vote')
def handle_vote(json):
    #global individuos, vote_stash

    print('recieved vote ' + str(json))

    vote = int((json['chosen_candidate']))

    if 1 <= vote <= len(individuos):
        vote_stash[vote] = vote_stash[vote] + 1

    emit('update_vote_number', vote_stash, broadcast=True)

@socketio.on('broadcast_votes')
def broadcast_votes():
    pass

@socketio.on('connect')
def connected():
    emit('update_vote_number', vote_stash)
    print("Client Connected")
    clients.append(request.namespace)

@socketio.on('disconnect')
def disconnected():
    print("Client Disconnected")
    clients.remove(request.namespace)

if __name__ == '__main__':
    import thread, time
    import glob, os

    # Search
    # If not creates individuals
    # Start mutating at slow rate


    thread.start_new_thread(lambda: socketio.run(app))
