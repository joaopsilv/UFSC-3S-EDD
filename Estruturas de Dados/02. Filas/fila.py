

class Fila:
    def __init__(self, tamanho_maximo: int):
        try:
            if not (isinstance(tamanho_maximo, int)):
                raise TypeError("É o tamanho máximo da fila deve ser um número inteiro!")
            self.__tamanho_maximo = tamanho_maximo
            self.__contador = 0
            self.__fila = [None]*tamanho_maximo
            self.__fim = -1
            self.__inicio = 0
        except TypeError as error:
            print(error)

    @property
    def tamanho_maximo(self) -> int:
        return self.__tamanho_maximo

    @property
    def contador(self) -> int:
        return self.__contador

    @contador.setter
    def contador(self, valor):
        self.__contador = valor

    @property
    def fila(self):
        return self.__fila

    @property
    def fim(self) -> int:
        return self.__fim

    @fim.setter
    def fim(self, valor):
        self.__fim = valor

    @property
    def inicio(self) -> int:
        return self.__inicio

    @inicio.setter
    def inicio(self, valor):
        self.__inicio = valor

    def enqueue(self, elemento: int):
        try:
            if self.__fila_cheia():
                raise IndexError("A fila está cheia!")
            self.fim = (self.fim + 1) % self.tamanho_maximo
            self.fila[self.fim] = elemento
            self.contador += 1
        except IndexError as error:
            print(error)

    def dequeue(self) -> int:
        try:
            if self.__fila_vazia():
                raise IndexError("A fila está vazia!")
            temp = self.fila[self.inicio]
            self.inicio = (self.inicio + 1) % self.tamanho_maximo
            self.contador -= 1
            return temp
        except IndexError as error:
            print(error)

    def valor_primeiro_elemento(self) -> int:
        try:
            if self.__fila_vazia():
                raise IndexError("A fila está vazia!")
            return self.fila[self.inicio]
        except IndexError as error:
            print(error)

    def numero_elementos(self) -> int:
        return self.contador

    def __fila_vazia(self) -> bool:
        return self.numero_elementos() == 0

    def __fila_cheia(self) -> bool:
        return self.numero_elementos() == self.tamanho_maximo
