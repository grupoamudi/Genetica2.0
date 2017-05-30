from flask import Flask, render_template, request, send_from_directory, url_for
from flask_socketio import SocketIO, send, emit
from apscheduler.schedulers.background import BackgroundScheduler
import time
import test_png
import numpy
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weoijhgsdlkjfwelkr20943091d98asokolfqeoi"!!?qw?sda/~dwqp1deo'
socketio = SocketIO(app)

clients = []
#individuos = ["1", "2", "3", "4"]  # TODO: Fix
nb_individuos = 4
nb_counter = nb_individuos
individuo_list = []
while nb_individuos != 0:
    individuo_list += [test_png.lib.individuo()]
    nb_individuos -= 1
count_votes = [0]

# Init vote_stash
vote_stash = {};
for i,individuo in enumerate(individuo_list):
    vote_stash[i+1] = 0;
print(vote_stash)


@app.before_first_request
def init_program():

    #repeated function
    def crossing_over():
        total_votes = 0
        highest_voted = 0
        winner = 0
        global nb_counter
        #Checks if number of votes > 0
        for i in vote_stash:
            total_votes += vote_stash[i]
        if total_votes == 0:
            winner = random.randint(0,nb_counter-1)
        #Search for the highest voted
        else:
            for j in vote_stash:
                if vote_stash[j] > highest_voted :
                    highest_voted = vote_stash[j]
                    winner = int(j)-1
                vote_stash[j] = 0
        global individuo_list
        print()
        print ('winner:' , winner)
        #updates figures with new ones
        individuo_list = test_png.main_testepng(individuo_list, winner)

        socketio.emit('update_vote_number', vote_stash, broadcast = True)
        socketio.emit('reload', {})
        print()
        return

    scheduler = BackgroundScheduler()
    scheduler.add_job(crossing_over, 'interval', seconds = 1)
    scheduler.start()
    pass


@app.route('/')
def index():
    return render_template('index.html')


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

@socketio.on('connect')
def connected():
    emit('update_vote_number', vote_stash)
    print("Client Connected")
    clients.append(request.namespace)

@socketio.on('disconnect')
def disconnected():
    print("Client Disconnected")
    clients.remove(request.namespace)

@socketio.on('restarter')
def handle_restarter():
    global nb_counter
    global vote_stash
    global individuo_list
    individuo_list = []
    for i in range(nb_counter):
        individuo_list += [test_png.lib.individuo()]
    vote_stash = {};
    for i,individuo in enumerate(individuo_list):
        vote_stash[i+1] = 0;
    print()
    print()
    print ("button reinitialize pressed")
    print()
    print()
    pass

if __name__ == '__main__':
    import thread, time
    import glob, os



    # Search
    # If not creates individuals
    # Start mutating at slow rate


    thread.start_new_thread(lambda: socketio.run(app))
