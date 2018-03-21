# -*- coding: utf-8 -*-
import random, os
import numpy
import time
import matplotlib.pyplot as plot
import png
from matplotlib import colors as colors

plot.ion()

class individuo():

    # Evolutionnary Parameters
    ind_size = 25;
    mutation_steps = 50;
    max_heads_size = 5;
    direction_map_x = {'baixo': 1, 'cima': -1}
    direction_map_y = {'esquerda': -1, 'direita': 1}

    def __init__(self, array_in = None, pontas_in = None):
        self.array = array_in
        self.pontas = pontas_in
        if not array_in:
            self.generate()

    def mutate(self):
        # For each step
        for step in range(self.mutation_steps):
            # Verifica se criamos uma ponta aleatóriamente
            if Utils.chancenovas():
                if len(self.pontas) < self.max_heads_size:
                    escolhidox = random.randrange (0,len(self.array),1)
                    escolhidoy = random.randrange (0,len(self.array),1)

                    self.array[escolhidox][escolhidoy].valor = 1
                    new_ponta = ponta(escolhidox, escolhidoy)
                    self.pontas.append(new_ponta)

            # Verifica se eliminamos uma ponta aleatóriamente
            if Utils.chancetira():
                if self.pontas:
                    self.pontas.remove(random.choice(self.pontas))

            # Foreach pontas
            for cadaponta in self.pontas:
                # Choose a random direction
                direction = Utils.definedirecao()

                y_test = self.direction_map_y.get(direction)
                x_test = self.direction_map_x.get(direction)
                #print(x_test)
                if x_test:
                    x_move = cadaponta.valorx + x_test if (cadaponta.valorx + x_test) < len(self.array) else 0
                    if x_move == -self.ind_size -1:
                        x_move = 0
                    self.array[x_move][cadaponta.valory].mudavalor();
                    cadaponta.valorx = x_move
                elif y_test:
                    y_move = cadaponta.valory + y_test if (cadaponta.valory + y_test) < len(self.array) else 0
                    if y_move == -self.ind_size -1:
                        y_move = 0
                    #print ('aaa')
                    self.array[cadaponta.valorx][y_move].mudavalor();
                    cadaponta.valory = y_move
                else:
                    raise "DirectionNotFound"

    #def cross_with(self, individuo_to_cross):
    #   pass

    def save_bin(self, file_path):
        ''' No works '''
        try:
            # Opens the binary file
            bin_file = open(file_path, "wb")

            # Converts to binary
            array_binary = bytesarray()

            # Write data
            bin_file.write(array_binary)

            # Close file
            bin_file.close()

            # Success
            return True
        except:
            # Failure
            return False

    def save_png(self, file_path):
        ''' Saves an individuo as png '''

        # Writes Array
        png_file = open(file_path, 'wb')
        d_matrix = self.value_matrix()
        w = png.Writer(len(d_matrix[0]), len(d_matrix), greyscale=True, bitdepth=1)
        w.write(png_file, d_matrix)
        png_file.close()

        # # Writes pontas
        # file_name = os.path.splitext(file_path)
        # new_name = file_name[0] + "-pontas"
        #
        # ponta_path = new_name + file_name[1]
        # # Writes Array
        # png_file = open(ponta_path, 'wb')
        # d_matrix = self.value_matrix()
        # w = png.Writer(len(d_matrix[0]), len(d_matrix), greyscale=True, bitdepth=1)
        # w.write(png_file, d_matrix)
        # png_file.close()

    def load_png(self, file_path):
        """ Loads an individuo data from a png file."""

        png_reader = png.Reader(filename=file_path)
        png_file = png_reader.read()

        png_weight = png_file[0]
        png_height = png_file[1]
        png_pixels = png_file[2]

        array_temp = []

        for line in png_pixels:
            temp_line = []
            for item in line:
                temp_line.append(celula(item))
            array_temp.append(temp_line)

        self.array = array_temp



    def value_matrix(self):
        # Builds Drawing matrix
        drawing_matrix = []
        for line in self.array:
            H = []
            for item in line:
                H.append(int(item.valor))
            drawing_matrix.append(H)
        return drawing_matrix


    def load_bin(self, file_path):

        bin_file = open(file_path, "rb")

        data = bin_file.read()

        print("=========== Loaded Data ================\n")
        print(data)

    def generate(self):
        '''Starts the first dot'''
        #global ind_size

        # Random mutation
        self.array = [[celula() for x in range(self.ind_size)] for y in range(self.ind_size)]
        escolhidox = random.randrange (0,len(self.array),1)
        escolhidoy = random.randrange (0,len(self.array),1)

        self.array[escolhidox][escolhidoy].valor = 1;

        # Corresponding edge
        self.pontas = []
        new_ponta = ponta(escolhidox, escolhidoy)
        self.pontas.append(new_ponta)

    #def clear_single_pixels(self):
     #   pass

class Utils():

    @staticmethod
    def definedirecao():
        chance = random.randrange(0,100,1)
        if chance < 25 :
            direcao = 'cima'
        elif chance < 50 :
            direcao = 'direita'
        elif chance < 75 :
            direcao = 'baixo'
        elif chance < 101:
            direcao = 'esquerda'
        return direcao

    @staticmethod
    def chancenovas ():
        '''Chance de criar novas cabeças.'''
        chancecabeca = random.randrange(0,10001,1)
        if chancecabeca > 9998 :
            return True
        else:
            return False

    @staticmethod
    def chancetira ():
        '''Chance de tirar uma cabeça.'''
        chancetirar = random.randrange(0,10001,1)
        if chancetirar > 9999:
            return True
        else:
            return False

class celula(object):

    def __init__ (self, valor = 0):
        self.valor = valor;

    def mudavalor(self):
        self.valor = not self.valor

class ponta(object):

    def __init__ (self, valorx_in = 0, valory_in = 0):
        self.valorx = valorx_in
        self.valory = valory_in

    def recebevalor (self, x, y):
        self.valorx = x
        self.valory = y

def limpamatriz(array):
    '''Elimina pixels mortos sem vizinhança.'''
    indice = (len(array))
    pontox = 0

    while pontox != len(array):
        pontoy = 0
        while pontoy != len(array):
            compararx1 = pontox + 1
            compararx2 = pontox - 1
            comparary1 = pontoy + 1
            comparary2 = pontoy - 1
            if array[pontox][pontoy].valor == 0:
                if compararx1 == len(array):
                     compararx1 = 0
                if compararx2 == -1:
                     compararx2 = len(array) -1
                if comparary1 == len(array):
                     comparary1 = 0
                if comparary2 == -1:
                     comparary2 = len (array) -1
                if array[compararx1][pontoy].valor == 1 and array[compararx2][pontoy].valor == 1 and array[pontox][comparary1].valor == 1 and array[pontox][comparary2].valor == 1 :
                    array[pontox][pontoy].valor = 1
            if array[pontox][pontoy].valor == 1:
                if compararx1 == len(array):
                     compararx1 = 0
                if compararx2 == -1:
                     compararx2 = len(array) -1
                if comparary1 == len(array):
                     comparary1 = 0
                if comparary2 == -1:
                     comparary2 = len (array) -1
                if array[compararx1][pontoy].valor == 0 and array[compararx2][pontoy].valor == 0 and array[pontox][comparary1].valor == 0 and array[pontox][comparary2].valor == 0 :
                    array[pontox][pontoy].valor = 0
            pontoy += 1
        pontox += 1

def printamatriz (cells_list):
    for i in range(len(cells_list)):
        for j in range(len(cells_list[i].array)):
            linha=[]
            for k in range(len(cells_list[i].array[j])):
                #print(cells_list[i].array[j][k].valor)
                linha += [cells_list[i].array[j][k].valor]
            print (linha)


def main():
    nb_cells = int(input("digite o numero de individuos "))
    cells_list = []

    while nb_cells != 0:
        cells_list += [individuo()]
        nb_cells -= 1
