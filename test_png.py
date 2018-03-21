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
    trigger_print = False
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
            if trigger_print :
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
    if trigger_print :
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
    if trigger_print :
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
                    if trigger_print :
                        print (lista)
                    lista = []
                if trigger_print :
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
            if trigger_print :
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
                            if trigger_print :
                                print ('parente %d'  %(numero_parente))
                            for line_number, each_line in enumerate (each_element.array):
                                for cell_value, each_cell in enumerate (individuo_list[numero_parente].array[line_number]):
                                    lista += [each_cell.valor]
                                if trigger_print :
                                    print (lista)
                                lista = []
                if trigger_print :
                    print ( 'filho'        )
                for line_number,each_line in enumerate (filho.array):
                    for cell_value, each_cell in enumerate (filho.array[line_number]):
                        lista += [each_cell.valor]
                    if trigger_print :
                        print (lista)
                    lista = []
            new_individuolist += [filho]
    for each_individuo_number, each_individuo in enumerate (new_individuolist):
        #print (each_individuo)
        if trigger_print :
            print ('each_indiv  iduo_number : ', each_individuo_number )
        each_individuo.save_png("static/%s.png" %each_individuo_number)

    square_filler (individuo_list)
    return new_individuolist





#############################################################################################################
def square_filler (individuo_list):
### Objetivo: escanear os indivíduos e determinar as células pintadas de cada indivíduo e realizar o esquema para todos#
    for individuo_number,individuo in enumerate(individuo_list):
        print ('        individuo %d       ' %(individuo_number))
        trigger_print = False
        painted_cells_total = 0
        checked_cells_before = []
        for col_number, coluna in enumerate(individuo.array):
            for line_number, linha in enumerate(individuo.array[col_number]):
                if linha.valor == 1:
                    painted_cells_total += 1
                    checked_cells_before += [[col_number,line_number]]
                if trigger_print:
                    print ("linha : %d , coluna : %d " %(line_number ,col_number))
####### lista de celulas pintadas ###########################################
        painted_cell_array = checked_cells_before
        #print ('checked_cells_before : ', checked_cells_before)
        lista_de_lista_de_celulas_em_torno_de_cada_foco = []
        lista_de_focos = []
        for checked_cell_number, checked_cell in enumerate(checked_cells_before):
            foco = checked_cell
            lista_de_focos += [foco]
            blankline_left = False
            blankline_right = False
            blankline_top = False
            blankline_bottom = False
            if trigger_print:
                print ('foco[0]-1 : ', foco[0]-1 )
                print ('foco[0]+1 : ', foco[0]+1 )
                print ('foco[1]-1 : ', foco[1]-1 )
                print ('foco[1]+1 : ', foco[1]+1 )
                print ('ind_size : ', individuo.ind_size)
###################### Observa as imediações do foco #########################
            if foco[0] -1 == -1:
                blankline_left = True
            if foco[0] +1 == individuo.ind_size:
                blankline_right = True
            if foco[1] -1 == -1 :
                blankline_top = True
            if foco[1] +1 == individuo.ind_size:
                blankline_bottom = True
    ##################### inicia escolha de um foco ############################################
    ################### Objetivo: fazer uma lista das células pintadas de cada célula pintada ###########
            painted_cells_total = len (checked_cells_before)
            lista_de_celulas_em_torno_do_foco = []
            lista_de_celulas_em_torno_do_foco += [foco]
            #while painted_cells_total != 0: # essa função tem que acabar quando não tiver mais nenhuma célula por perto
    #################################### checando ao redor da célula foco ####################
            if blankline_left == False and blankline_top == False:
                if individuo.array[foco[0] -1][foco[1] -1].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] -1,foco[1] -1]]
            if blankline_top == False:
                if individuo.array[foco[0] +0][foco[1] -1].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] +0,foco[1] -1]]
            if blankline_right == False and blankline_top == False:
                if individuo.array[foco[0] +1][foco[1] -1].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] +1,foco[1] -1]]
            if blankline_right == False:
                if individuo.array[foco[0] +1][foco[1] +0].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] +1,foco[1] +0]]
            if blankline_right == False and blankline_bottom == False:
                if individuo.array[foco[0] +1][foco[1] +1].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] +1,foco[1] +1]]
            if blankline_bottom == False:
                if individuo.array[foco[0] +0][foco[1] +1].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] +0,foco[1] +1]]
            if blankline_bottom == False and blankline_left == False:
                if individuo.array[foco[0] -1][foco[1] +1].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] -1,foco[1] +1]]
            if blankline_left == False:
                if individuo.array[foco[0] -1][foco[1] +0].valor == 1:
                    lista_de_celulas_em_torno_do_foco += [[foco[0] -1,foco[1] +0]]
                #if individuo.array[foco[0] +0][foco[1] +0].valor == 1 and blank:
                #    lista_de_celulas_em_torno_do_foco += [[foco[0] +0,foco[1] +0]]
                #painted_cells_total -= 1
            lista_de_lista_de_celulas_em_torno_de_cada_foco += [lista_de_celulas_em_torno_do_foco]
        total_number_of_adjacents = 0
        for each_item_number, each_item in enumerate (lista_de_lista_de_celulas_em_torno_de_cada_foco):
            if trigger_print:
                print ('listona gigante ; ', each_item)
########## pegar o numero total de adjacentes para garantir que o método passa por todos possíveis
            each_item = each_item[1:]
            for each_item_index, each_item_inside in enumerate (each_item):
                total_number_of_adjacents += 1
        if trigger_print:
            print ('total_number_of_adjacents', total_number_of_adjacents)
########## Agora possuo uma lista relacionando todos os pontos pintados e seus respectivos células ao lado documentadas #
                    ####### criar e arrumar uma matriz blank que indica onde está os dots
        blank_matrix = generate_blank_to_fill (individuo.ind_size,trigger_print)
        for line_number, line in enumerate (blank_matrix):
            for col_number, col in enumerate (blank_matrix[line_number]):
                for each_foco_index, each_foco in enumerate (lista_de_focos):
                    #print ('lin col ', each_foco[0],each_foco[1])
                    if line_number == each_foco[0]:
                        if col_number == each_foco[1]:
                            blank_matrix[line_number][col_number] += 5
        ######### Analisar as colunas ############## - no final esta parte não fez nada
    #    list_focus_in_line = []
    #    for each_foco_index, each_foco in enumerate (lista_de_focos):
    #        print ('lista_de_focos ' , lista_de_focos)
    #        list_focus_in_line_carrier = []
    #        for line_number in range (individuo.ind_size):
    #            if each_foco[0] == line_number:
    #                list_focus_in_line_carrier += [line_number,each_foco[1]]
    #        list_focus_in_line += [list_focus_in_line_carrier]
    #        print ('list_focus_in_line ' ,list_focus_in_line)
    #        print ()
#
############## Para as linhas ###################################
        for line_number in range (individuo.ind_size):
            same_line = []
            for each_foco_index, each_foco in enumerate(lista_de_focos):
                if line_number == each_foco[0]:
                    same_line += [each_foco[1]]
############# como os focos estão em ordem, dá para fazer a seguinte coisa ###############
                if len(same_line) > 1:
                    changer = min(same_line)+1
                    while changer != max(same_line):
                        if blank_matrix[line_number][changer] == 0:
                            blank_matrix[line_number][changer] += 3
                        changer += 1
                    if trigger_print:
                        print ('same_line end :', same_line[-1])
                        print ('same_line >' , same_line)
################## Para colunas ########################
        for col_number in range (individuo.ind_size):
            same_col = []
            for each_foco_index, each_foco in enumerate (lista_de_focos):
                if col_number == each_foco[1]:
                    same_col += [each_foco[0]]
################# os focos olhando as colunas não estao em ordem ############
            if len(same_col) >1:
                changer = min(same_col)+1
                while changer != max(same_col):
                    if blank_matrix[changer][col_number] == 3:
                        blank_matrix[changer][col_number] +=3
                    if blank_matrix[changer][col_number] == 0:
                        blank_matrix[changer][col_number] +=3
                    changer += 1
################## Aqui o programa já decidiu onde deve trocar o valor
################## O entorno das casas que contem 6 devem ser comparadas
################## Para ver se elas estão envoltas ou por 6 ou por 5, dot.

        for line_number, line in enumerate (blank_matrix):
            print (line)
        print ()

        change_together = []


#        for line_number,line in enumerate (blank_matrix):
#            for col_number,col in enumerate (line):
#                change_together_carrier = []
#                change_value = True
#                if blank_matrix[line_number][col_number] == 6:
############### automaticamente pelo o que foi escrito na função acima, não existem pontos que
############### podem dar erro (estar na borda)
###### No caso, é impossível ter um 0 ao lado
#                    change_together_carrier += [[line_number,col_number]]
#                    if blank_matrix[line_number][col_number-1] == 6:
#                        change_together_carrier +=[[line_number,col_number-1]]
#                    if blank_matrix[line_number+1][col_number] == 6:
#                        change_together_carrier += [[line_number+1,col_number]]
#                    if blank_matrix[line_number][col_number+1] == 6:
#                        change_together_carrier += [[line_number,col_number+1]]
#                    if blank_matrix[line_number-1][col_number] == 6:
#                        change_together_carrier += [[line_number-1,col_number]]
#                    print ('change_together_carrier ; ' , change_together_carrier)
#                    #if times_ran > 1:
#                    #      change_together_carrier = change_together[0:1]
#                    if len(change_together_carrier) > 1:
#                        change_together += [change_together_carrier]
#
#            print ('change_together ' , change_together)
            #change_together =[]
        for i in range(individuo.ind_size):
            #print ()
            for line_number, line in enumerate (blank_matrix):
                for col_number,col in enumerate (line):
                    blankline_left = False
                    blankline_right = False
                    blankline_top = False
                    blankline_bottom = False
                    if line_number -1 == -1:
                        blankline_top = True
                    if line_number +1 == individuo.ind_size:
                        blankline_bottom = True
                    if col_number -1 == -1 :
                        blankline_left = True
                    if col_number +1 == individuo.ind_size:
                        blankline_right = True
                    #print ('col_number -1', col_number -1)
                    if blank_matrix[line_number][col_number] == 6:
                        if blank_matrix[line_number][col_number-1] == 3 and blankline_left == False:
                            blank_matrix[line_number][col_number] = 3
                        if blank_matrix[line_number+1][col_number] == 3 and blankline_bottom == False:
                            blank_matrix[line_number][col_number] = 3
                        if blank_matrix[line_number][col_number+1] == 3 and blankline_right == False:
                            blank_matrix[line_number][col_number] = 3
                        if blank_matrix[line_number-1][col_number] == 3 and blankline_top == False:
                            blank_matrix[line_number][col_number] = 3
            #print (line)
        for line_number,line in enumerate (blank_matrix):
            for col_number,col in enumerate (line) :
                if blank_matrix[line_number][col_number] == 6:
                    individuo.array[line_number][col_number].valor = 1
    return






def generate_blank_to_fill (size,trigger_print):
    blank = []
    for x_times in range(size):
        linha = []
        for y_times in range(size):
            linha += [0]
        blank += [linha]
        if trigger_print:
            print (linha)
    if trigger_print:
        print(blank)
    return blank












def square_filler_old (individuo_list):
    trigger_print = False
####################### conta quantas células estão pintadas #############################
# jeito mais preguiça/porco que eu encontrei #
    for individuo_number,individuo in enumerate(individuo_list):
        painted_cells_total = 0
        checked_cells_before = []
        for col_number, coluna in enumerate(individuo.array):
            for line_number, linha in enumerate(individuo.array[col_number]):
                if linha.valor == 1:
                    painted_cells_total += 1
                    checked_cells_before += [[col_number,line_number]]
                if trigger_print:
                    print ("linha : %d , coluna : %d " %(line_number ,col_number))
        print ('checked_cells_before : ', checked_cells_before)
        for checked_cell_number, each_checked_cell in enumerate(checked_cells_before):
            checked_cells = checked_cells_before
            painted_cells = painted_cells_total
            foco_inicial = each_checked_cell
            removed_from_checked_cells = []
            foco = foco_inicial
            while painted_cells != 0:
                ran_once = False
                invalido = False
                voltou_ao_inicial = False
##############################################################################################
                blankline_left = False
                blankline_right = False
                blankline_top = False
                blankline_bottom = False
#################################################################################################
                skip = False
                teve_ao_lado = False
############################## check if foco is in the removed_cells list ###########################
#                for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
#                    if foco == compare_foco:
#                        invalido = True
#####################################################################################################
                print ('foco : ', foco)
                print ('checked_cells : ',checked_cells)
#                print ('foco[0] -1 : ',foco[0] -1)
#                print ('foco[0] +1 : ',foco[0] +1)
#                print ('foco[1] -1 : ',foco[1] -1)
#                print ('foco[1] +1 : ',foco[1] +1)
                if voltou_ao_inicial == False:
                    if foco[0] -1 == -1:
                        blankline_left = True
                    if foco[0] +1 == individuo.ind_size:
                        blankline_right = True
                    if foco[1] -1 == -1 :
                        blankline_top = True
                    if foco[1] +1 == individuo.ind_size:
                        blankline_bottom = True
######################## skips if didn't find any continuation ###########################
                    if skip == False:
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] -1,foco[1] -1] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] -1][foco[1] -1].valor == 1 and blankline_left == False and blankline_top == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]-1,foco[1]-1]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] +0,foco[1] -1] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] +0][foco[1] -1].valor == 1 and blankline_top == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]-0,foco[1]-1]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] +1,foco[1] -1] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] +1][foco[1] -1].valor == 1 and blankline_right == False and blankline_top == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]+1,foco[1]-1]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] +1,foco[1] +0] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] +1][foco[1] +0].valor == 1 and blankline_right == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]+1,foco[1]+0]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] +1,foco[1] +1] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] +1][foco[1] +1].valor == 1 and blankline_right == False and blankline_bottom == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]+1,foco[1]+1]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] +0,foco[1] +1] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] +0][foco[1] +1].valor == 1 and blankline_bottom == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]+0,foco[1]+1]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] -1,foco[1] +1] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] -1][foco[1] +1].valor == 1 and blankline_left == False and blankline_bottom == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]-1,foco[1]+1]
                            teve_ao_lado = True
                            ran_once = True
                        for checked_cell_number, compare_foco in enumerate (removed_from_checked_cells):
                            if [foco[0] -1,foco[1] +0] == compare_foco:
                                invalido = True
                        if individuo.array[foco[0] -1][foco[1] +0].valor == 1 and blankline_left == False and ran_once == False and invalido == False:
                            print ("foco : ", foco)
                            removed_from_checked_cells += [foco]
                            print('removed_from_checked_cells : ', removed_from_checked_cells)
                            checked_cells.remove([foco[0],foco[1]])
                            foco = [foco[0]-1,foco[1]+0]
                            teve_ao_lado = True
                            ran_once = True
                        if teve_ao_lado == False:
                            print ('não tinha nenhuma pintada ao lado')
                    painted_cells -= 1
            print ('painted_cells : ', painted_cells)

# a linha 190 causa que haja verificação de todas as células em cada indivíduo há como melhorar ?#
####################### percebe se as células fechadas formam um conjunto fechado ########
#    for painted_cell_number, each_painted_cell in enumerate(checked_cells):
#        check_around(individuo_list[checked_cell)

    #for individuo_number,individuo in enumerate(individuo_list):
    #    for col_number, coluna in enumerate(individuo.array):
    #        for line_number, linha in enumerate(individuo.array[col_number]):
############# encontrou uma célula pintada -> checar células em volta ######################
                #if linha.valor == 1:
                    #if individuo.array[col_number -1][line_number -1].valor == 1 :
                    #if individuo.array[col_number +0][line_number -1].valor == 1 :
                    #if individuo.array[col_number +1][line_number -1].valor == 1 :
                    #if individuo.array[col_number +1][line_number +0].valor == 1 :
                    #if individuo.array[col_number +1][line_number +1].valor == 1 :
                    #if individuo.array[col_number +0][line_number +1].valor == 1 :
                    #if individuo.array[col_number -1][line_number +1].valor == 1 :
                    #if individuo.array[col_number -1][line_number +0].valor == 1 :
                    #if individuo.array[col_number +0][line_number +0].valor == 1 :


                    #while painted_cells != 0 :
                    #    painted_cells -= 1


        #print (checked_cells)

    pass




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
