import genetic_lib as lib

def main():

    teste = True
    
    if teste == True:
        nb_cells = 4
    else:
        nb_cells = int(input("digite o numero de individuos "))
    
    individuo_list = []

    while nb_cells != 0:
        inviduo_list += [lib.individuo()]
        nb_cells -= 1

    for i in range(len(indviduo_list)):
        for j in range(10):
            cells_list[i].mutate()
        cells_list[i].save_png("%s.png" %i)        

    #A.array = []

    #A.load_png("test.png")

    #A.save_png("test_compare.png")
    # print("==== Original data =====\n")
    # print(A.array)

main()
