import time

x = int(time.time())
z = int(time.time()) + 30
y = 1

print (x)
print (z)

while y == 1:
    if x >= z:
        y = 0
    x = int(time.time())
    print (time.time())

print ('acabei')


if total_votes >= 10:
    for i,individuo in enumerate(individuos):
        vote_stash[i+1] = 0;
    socketio.emit('update_vote_number', vote_stash, broadcast=True)
