

class Pilha:
    def __init__(self, tamanho_maximo: int) -> None:
        try:
            if not (isinstance(tamanho_maximo, int)):
                raise TypeError("É o tamanho máximo da pilha deve ser um número inteiro!")
            self.__tamanho_maximo = tamanho_maximo
            self.__topo = -1
            self.__pilha = [None]*tamanho_maximo
        except TypeError as error:
            print(error)

    @property
    def tamanho_maximo(self) -> int:
        return self.__tamanho_maximo

    @property
    def topo(self) -> int:
        return self.__topo

    @topo.setter
    def topo(self, valor):
        self.__topo = valor

    @property
    def pilha(self):
        return self.__pilha

    def push(self, elemento) -> None:
        try:
            if self.__pilha_cheia():
                raise IndexError("A pilha já atingiu o limite máximo!")
            self.topo += 1
            self.pilha[self.topo] = elemento
        except IndexError as error:
            print(error)

    def pop(self) -> int:
        try:
            if self.__pilha_vazia():
                raise IndexError("A pilha está vazia!")
            temp = self.pilha[self.topo]
            self.topo -= 1
            return temp
        except IndexError as error:
            print(error)

    def valor_topo(self) -> int:
        try:
            if self.__pilha_vazia():
                raise IndexError("A pilha está vazia!")
            return self.pilha[self.topo]
        except IndexError as error:
            print(error)

    def numero_elementos(self) -> int:
        return self.topo + 1

    def __pilha_vazia(self) -> bool:
        return self.numero_elementos() == 0

    def __pilha_cheia(self) -> bool:
        return self.numero_elementos() == self.tamanho_maximo
