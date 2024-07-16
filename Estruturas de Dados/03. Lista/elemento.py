

class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__anterior = None
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, elemento):
        self.__anterior = elemento

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, elemento):
        self.__proximo = elemento
