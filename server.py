from flask import Flask, render_template, request, send_from_directory, url_for
from flask_socketio import SocketIO, send, emit
from apscheduler.schedulers.background import BackgroundScheduler
import time
import test_png
import numpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weoijhgsdlkjfwelkr20943091d98asokolfqeoi"!!?qw?sda/~dwqp1deo'
socketio = SocketIO(app)

clients = []
#individuos = ["1", "2", "3", "4"]  # TODO: Fix
nb_individuos = 4
individuo_list = []
while nb_individuos != 0:
    individuo_list += [test_png.lib.individuo()]
    nb_individuos -= 1
count_votes = [0]
print (individuo_list)

# Init vote_stash
vote_stash = {};
for i,individuo in enumerate(individuo_list):
    vote_stash[i+1] = 0;
print(vote_stash)


@app.before_first_request
def init_program():
    def crossing_over():
        total_votes = 0
        max_votes = 0
        winner = 0
        print ('a')
        for i in vote_stash:
            if max_votes < vote_stash[i]:
                max_votes = vote_stash[i]
                winner = int(i)
        socketio.emit('reload', {})
        #print ('max vote' , max_votes)
        #print ('winner ', winner)
        test_png.main_testepng(individuo_list)

        return
    scheduler = BackgroundScheduler()
    scheduler.add_job(crossing_over, 'interval', seconds = 3)
    scheduler.start()
    pass


@app.route('/')
def index():
    return render_template('index.html')
#TODO: Static serving images for index.html



@socketio.on('vote')
def handle_vote(json):
    #global individuos, vote_stash

    print('recieved vote ' + str(json))

    vote = int((json['chosen_candidate']))

    count_votes[0] = count_votes[0] + 1
    #print (count_votes)

    if 1 <= vote <= len(individuo_list):
        vote_stash[vote] = vote_stash[vote] + 1

    emit('update_vote_number', vote_stash, broadcast=True)

@socketio.on('update_figures')
def update_figures():
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
