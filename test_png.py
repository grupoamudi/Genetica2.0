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
    for i, vote_list_element in enumerate (vote_list):
        if vote_list_element != 0:
            semvoto = 1
#
#    for i in range(len(vote_list)):
#        if vote_list[i] != 0 :
#            semvoto = 1

    # se não houve votos #
    if semvoto == 0:
        total = len(vote_list)
        for i, vote_list_element in enumerate (vote_list):
#        for i in range(len(vote_list)):
            vote_list[i] = 1
            print ('vote_list', vote_list)
        for i, vote_list_element in enumerate (vote_list):
#        for i in range(len(vote_list)):
            chance_list += [(vote_list[i]/total)*100]
    # se houve votos #
    else:
        for i, vote_list_element in enumerate (vote_list):
            total += vote_list[i]
        for i, vote_list_element in enumerate (vote_list):
            chance_list += [(vote_list[i]/total)*100]
    print ('chance_list : ',chance_list)

    #######    Eleição do que fazer #########################
    lista_do_que_fazer = []
    for todo_individuo, individuo_list_element in enumerate (individuo_list):
        lib.random.seed()
        cte_escolhe_o_que_vai_acontecer = lib.random.randint(0,100)
        if cte_escolhe_o_que_vai_acontecer <= 1 :
            lista_do_que_fazer += ['extincao']
        else:
            if cte_escolhe_o_que_vai_acontecer <= 95 :
                lista_do_que_fazer += ['mutar_sozinho']
            else:
                if cte_escolhe_o_que_vai_acontecer <= 100 :
                    lista_do_que_fazer += ['cruzar']
    print ('lista do que fazer : ',lista_do_que_fazer)

    #######     Fazer o que foi eleito ###########################

    for numero_individuo, acao_a_executar in enumerate(lista_do_que_fazer):
        if acao_a_executar == 'extincao':
            ''' cria um indivíduo novo do 0 '''
            new_individuolist += [lib.individuo()]
            # o indivíduo é extinto depois de cruzar #


        if acao_a_executar == 'mutar_sozinho':
            ''' faz o indivíduo mutar sozinho'''

            individuo_list[numero_individuo].mutate()
            mutated_individuo = individuo_list[numero_individuo]
            for each_line_number , each_line in enumerate (mutated_individuo.array):
                for each_cell_number , each_cell in enumerate (mutated_individuo.array[each_line_number]):
                      each_cell.valor = int(each_cell.valor)

            #      erro de conversão de booleanos     #
            #individuo_list[numero_individuo].array = individuo_list[numero_individuo].array * 1

            new_individuolist += [mutated_individuo]

            ##########  verificacao manual por console ###########################
            Verifica_mutar_sozinho_console = False
            if Verifica_mutar_sozinho_console:
                lista = []
                for each_line_number , each_line in enumerate (mutated_individuo.array):
                    for each_cell_number, each_cell in enumerate (mutated_individuo.array[each_line_number]):
                        lista += [each_cell.valor]
                    print (lista)
                    lista = []
                print ()

        if acao_a_executar == 'cruzar':
            chosen = []
            pare = 0
            ##########   dependendo da porcentagem da chance_list, ele gera números aleatórios e se for maior ele adiciona como escolhido   #####
            while len(chosen) < 2:
                for i, chance_list_element in enumerate (chance_list):
                    chance_possibility = lib.random.randint(0,100)
                    if chance_possibility < chance_list_element and pare == 0:
                        chosen += [i]
                        if len(chosen) == 2:
                            pare = 1
            print ('chosen list : ', chosen)
                ################################   o cruzamento ############################

            ###########   criacao do individuo resultante (filho) ###################

            filho = lib.individuo()

            ###########   probabilidade de passagem de genes   #####################

            #probabilidade_crossing_pai = 50
            #probabilidade_corssing_mae = 50

            chosen_number_0 = chosen[0]
            chosen_number_1 = chosen[1]

            ###########   mecanismo de juncao entre os pais (cruzamento) ###########################
            lista = []
            for line_number,each_line in enumerate (filho.array):

                chance_possibility_crossing = lib.random.randint(0,100)
                if chance_possibility_crossing < 50 : #pega fileira de gene do pais
                    for cell_number_son, each_cell_son in enumerate (filho.array[line_number]):
                        for cell_number_parent, each_cell_parent in enumerate (individuo_list[chosen_number_0].array[line_number]):
                            if cell_number_son == cell_number_parent:
                                #print ('each_cell_parent : ', each_cell_parent.valor)
                                filho.array[line_number][cell_number_son].valor = each_cell_parent.valor
                                #print ('copied 0')
                    filho.array = filho.array * 1
                elif chance_possibility_crossing < 100 : #pega fileira de gene do pais
                    for cell_number_son, each_cell_son in enumerate (filho.array[line_number]):
                        for cell_number_parent, each_cell_parent in enumerate (individuo_list[chosen_number_1].array[line_number]):
                            if cell_number_son == cell_number_parent:
                                #print ('each_cell_parent : ', each_cell_parent.valor)
                                filho.array[line_number][cell_number_son].valor = each_cell_parent.valor
                                #print ('copied 1')
                    filho.array = filho.array * 1
            ##########   verificacao no console do mecanismo  #################################
            Verifica_crossing_console = False
            if Verifica_crossing_console :
                lista = []
                for each_individuo_in_chosen_number, each_individuo in enumerate( chosen):
                    for numero_parente,each_element in enumerate (individuo_list):
                        if each_individuo_in_chosen_number == numero_parente:
                            print ('parente %d'  %(numero_parente))
                            for line_number, each_line in enumerate (each_element.array):
                                for cell_value, each_cell in enumerate (individuo_list[numero_parente].array[line_number]):
                                    lista += [each_cell.valor]
                                print (lista)
                                lista = []
                print ( 'filho'        )
                for line_number,each_line in enumerate (filho.array):
                    for cell_value, each_cell in enumerate (filho.array[line_number]):
                        lista += [each_cell.valor]
                    print (lista)
                    lista = []
            new_individuolist += [filho]
            for each_individuo_number, each_individuo in enumerate (new_individuolist):
                #print (each_individuo)
                each_individuo.save_png("static/%s.png" %each_individuo_number)

    return new_individuolist







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
