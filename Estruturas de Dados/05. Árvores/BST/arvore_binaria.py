from elemento import Elemento


class ArvoreBinaria:
    def __init__(self, elemento: Elemento | None = None):
        self.__elemento = elemento
        self.__esquerda = None
        self.__direita = None
        if self.__elemento:
            self.__esquerda = ArvoreBinaria()
            self.__direita = ArvoreBinaria()

    @property
    def elemento(self) -> Elemento | None:
        return self.__elemento

    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    @property
    def esquerda(self) -> Elemento | None:
        return self.__esquerda

    @esquerda.setter
    def esquerda(self, esquerda):
        self.__esquerda = esquerda

    @property
    def direita(self) -> Elemento | None:
        return self.__direita

    @direita.setter
    def direita(self, direita):
        self.__direita = direita

    def incluir(self, valor: int):
        novo_elemento = Elemento(valor)
        if self.__vazio():
            self.elemento = novo_elemento
            self.esquerda = ArvoreBinaria()
            self.direita = ArvoreBinaria()
        elif novo_elemento.valor == self.elemento.valor:
            return
        elif novo_elemento.valor < self.elemento.valor:
            self.esquerda.incluir(valor)
        elif novo_elemento.valor > self.elemento.valor:
            self.direita.incluir(valor)

    def excluir(self, valor: int):
        if self.__vazio():
            return self
    
        if valor < self.elemento.valor:
            self.esquerda.excluir(valor)
            return

        if valor > self.elemento.valor:
            self.direita.excluir(valor)
            return
    
        if valor == self.elemento.valor:
            if self.__folha():
                self.elemento = None
                self.esquerda = None
                self.direita = None
                return
            elif self.esquerda.__vazio():
                self.elemento = self.direita.elemento
                self.esquerda = self.direita.esquerda
                self.direita = self.direita.direita
                return
            else:
                self.elemento = self.esquerda.__valor_maximo()
                self.esquerda.excluir(self.esquerda.__valor_maximo().valor)
                return

    def buscar(self, valor: int) -> bool:
        if self.__vazio():
            print(f'O valor {valor} não foi encontrado na árvore')
            return False
        
        if self.elemento.valor == valor:
            print(f'O valor {valor} foi encontrado na árvore')
            return True
        
        if valor < self.elemento.valor:
            return self.esquerda.buscar(valor)
        
        if valor > self.elemento.valor:
            return self.direita.buscar(valor)

    def in_order(self) -> list:
        if self.__vazio():
            return []
        return self.esquerda.in_order() + [self.elemento.valor] + self.direita.in_order()

    def pre_order(self) -> list:
        if self.__vazio():
            return []
        return [self.elemento.valor] + self.esquerda.pre_order() + self.direita.pre_order()

    def pos_order(self) -> list:
        if self.__vazio():
            return []
        return self.esquerda.pos_order() + self.direita.pos_order() + [self.elemento.valor]

    def __vazio(self) -> bool:
        return self.elemento is None
    
    def __folha(self) -> bool:
        return self.esquerda.__vazio() and self.direita.__vazio()

    def __valor_maximo(self) -> Elemento:
        atual = self
        while not atual.direita.__vazio():
            atual = atual.direita
        return atual.elemento
