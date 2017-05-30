import genetic_lib as lib

once = True

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
