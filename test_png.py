import genetic_lib as lib


once = True


def crosser(vote_stash, individuo_list):
    new_individuolist = []
    ########   Gera as chances de mutação     #############
    vote_list = []
    chance_list = []
    total = 0
    semvoto = 0
    soma = 0
    real_chance_list = []
    # obtém de vote_stash os votos e cria uma vote_list utilizável #
    for i in vote_stash:
        vote_list += [vote_stash[i]]
    # determina se houve votos válidos #
    for i in range(len(vote_list)):
        if vote_list[i] != 0 :
            semvoto = 1
    # se não houve votos #
    if semvoto == 0:
        total = len(vote_list)
        for i in range(len(vote_list)):
            vote_list[i]=1
            print ('vote_list' , vote_list)
        for i in range(len(vote_list)):
            chance_list += [(vote_list[i]/len(vote_list))*100]
    # se houve votos #
    else:
        for i in range(len(vote_list)):
            total += vote_list[i]
        for i in range(len(vote_list)):
            chance_list += [(vote_list[i]/total)*100]
    print ('chance_list : ',chance_list)

    #######    The real chance_list #########################
    for i in range(len(chance_list)):
        soma += chance_list[i]
        real_chance_list += [soma]
    soma = 0
    print ('real_chance_list : ', real_chance_list)

    #######    Eleição do que fazer #########################
    lista_do_que_fazer = []
    for i in range (len (individuo_list)):
        lib.random.seed()
        cte_escolhe_o_que_vai_acontecer = lib.random.randint(0,100)
        if cte_escolhe_o_que_vai_acontecer <= 10 :
            lista_do_que_fazer += ['extincao']
        else:
            if cte_escolhe_o_que_vai_acontecer <= 20 :
                lista_do_que_fazer += ['mutar_sozinho']
            else:
                if cte_escolhe_o_que_vai_acontecer <= 100 :
                    lista_do_que_fazer += ['cruzar']
    print ('lista do que fazer : ',lista_do_que_fazer)

    #######     Fazer o que foi eleito ###########################

    for i in lista_do_que_fazer:
        if i == 'extincao':
            ''' cria um indivíduo novo do 0 '''
            new_individuolist += [lib.individuo()]
            # o indivíduo é extinto depois de cruzar #
#        if i == 'mutar_sozinho':
            ''' faz o indivíduo mutar sozinho'''

        if i == 'cruzar':
            chosen = []
            ##########   até a lista ser menor que 2, adicionar indivíduos para cruzar  #######
            while len(chosen) < 2:
                for i in range (len(chance_list)):
                    chance_possibility = lib.random.randint(0,100)
                    if chance_possibility <= chance_list[i]:
                        chosen += [i]
            print ('chosen list : ', chosen )
            print (len(chosen))
            hold_chosen =[]
            #######    se a lista de escolhidos para cruzar é maior que 2, escolher aleatóriamente 2 ########
            if len(chosen) > 2:
                while len(hold_chosen) != 2 :
                    choose_one = lib.random.randint(0,len(chosen)-1)
                    print ('choose_one : ', choose_one)
                    hold_chosen += [chosen[choose_one]]
                chosen = hold_chosen
                print ('chosen list : ', chosen )



    return individuo_list






def mutation_method (individuo_list):
    print ()
    for i in range(len(individuo_list)):
        for j in range(len(individuo_list[i].array)):
            for k in range(len(individuo_list[i].array[j])):
                ####### foi acessado o valor de cada célula de cada individuo #########
                print (individuo_list[i].array[j][k].valor)

    return individuo_list
















#not used anymore
def main_testepng(individuo,winner):
    new_individuolist = []
    individuo_to_copy = []
    individuo_to_copy_lines = []
    #Copy the winning figure to save
    for i in range(len(individuo[winner].array)) :
        for j in range(len(individuo[winner].array[i])):
            individuo_to_copy_lines += [individuo[winner].array[i][j].valor]
        individuo_to_copy += [individuo_to_copy_lines]
        individuo_to_copy_lines = []
    for i in range (len(individuo)):
        for j in range (len(individuo[i].array)):
            for k in range(len(individuo[i].array[j])):
                #Paste the victorious figure to the others
                individuo[i].array[j][k].valor = individuo_to_copy[j][k]
        #Make individues to mutate
        individuo[i].mutate()
        #Saves figures
        individuo[i].save_png("static/%s.png" %i)
        new_individuolist += [individuo[i]]
    return new_individuolist

#not used anymore
def old_crossing_over():
    total_votes = 0
    highest_voted = 0
    winner = 0
    global nb_counter
    #Checks if number of votes > 0
    for i in vote_stash:
        total_votes += vote_stash[i]
    if total_votes == 0:
        winner = random.randint(0,nb_counter-1)
    #Get voted list
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
