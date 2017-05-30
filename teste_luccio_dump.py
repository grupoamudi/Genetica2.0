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

print ('aaaaaaaaaaaaaaaaaaaaa')
print ()
print ('valorx ',cadaponta.valorx)
print ('valory ',cadaponta.valory)
print ()
print ('xtest ' ,x_test)
print ('xmove ', x_move)
print ('ponta valor ', cadaponta.valory)


for i in vote_stash:
    if max_votes == 0:
        winner = random.randint(0,nb_counter-1)
    elif max_votes < vote_stash[i]:
        max_votes = vote_stash[i]
        winner = int(i)
    vote_stash[i] = 0
