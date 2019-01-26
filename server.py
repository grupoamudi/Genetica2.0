# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, send_from_directory, url_for, copy_current_request_context
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
#individuos = ["1", "2", "3", "4"]
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
points_list = {}
for i,individuo in enumerate(individuo_list):
    points_list[i+1] = 0;
print(points_list)

@app.before_first_request
def init_program():
    #repeated function
    def reset_vote_stash(vote_stash):
        vote_stash[1] = 0
        vote_stash[2] = 0
        vote_stash[3] = 0
        vote_stash[4] = 0

    def crossing_over():
        global individuo_list, points_list
        individuo_list = test_png.crosser(vote_stash,individuo_list)
        for i,individuo in enumerate(individuo_list):
            points_list[i+1] = test_png.point_counter(individuo)
        print ("points_list : ", points_list)
        socketio.emit('update_generations')
        reset_vote_stash(vote_stash)
        socketio.emit('update_points_number', points_list, broadcast=True)
        socketio.emit('update_vote_number', vote_stash, broadcast=True)

    scheduler = BackgroundScheduler()
    scheduler.add_job(crossing_over, 'interval', seconds = 5)
    scheduler.start()


@app.route('/')
def index():
    global individuo_list
    number_of_individuos = [i for (i,individuo) in enumerate(individuo_list)]

    return render_template('index.html', individuo_list = number_of_individuos)


@socketio.on('vote')
def handle_vote(json):
    #global individuos, vote_stash

    print('recieved vote ' + str(json))

    vote = int((json['chosen_candidate']))
    count_votes[0] = count_votes[0] + 1
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

    print ("/n/n/nbutton reinitialize pressed/n/n/n")

    emit('reload', broadcast=True)
    pass

if __name__ == '__main__':
    import thread, time
    import glob, os
    # Search
    # If not creates individuals
    # Start mutating at slow rate


    thread.start_new_thread(lambda: socketio.run(app))
