import random

class individuo(object):

    def __init__(self):
        self.probabilidade = randit(0,999)/100;
        self.numMutacoes = 0
        self.valor = 0

    def atualizaMutacoes(self):
        self.numMutacoes = self.numMutacoes + 1

    def mudaValor(self):
        if self.valor == 0:
            self.valor = 1
        else:
            self.valor = 0

    def mudaProb(self):
        self.probabilidade = self.probabilidade**self.numMutacoes

    

    


    
        
