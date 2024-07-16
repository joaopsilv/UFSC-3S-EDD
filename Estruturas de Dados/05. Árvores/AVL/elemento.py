

class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__esquerda = None
        self.__direita = None
        self.__altura = 1

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def esquerda(self):
        return self.__esquerda

    @esquerda.setter
    def esquerda(self, valor):
        self.__esquerda = valor

    @property
    def direita(self):
        return self.__direita

    @direita.setter
    def direita(self, valor):
        self.__direita = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura = valor
