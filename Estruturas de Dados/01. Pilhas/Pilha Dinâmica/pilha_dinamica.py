from elemento import Elemento


class PilhaDinâmica:
    def __init__(self):
        self.__topo = None
        self.__contador = 0

    @property
    def topo(self) -> Elemento:
        return self.__topo

    @topo.setter
    def topo(self, valor):
        self.__topo = valor

    @property
    def contador(self) -> int:
        return self.__contador

    @contador.setter
    def contador(self, valor):
        self.__contador = valor

    def push(self, valor):
        novo_elemento = Elemento(valor)
        if self.contador > 0:
            novo_elemento.proximo = self.topo
        self.topo = novo_elemento
        self.contador += 1

    def pop(self) -> Elemento:
        try:
            if self.contador == 0:
                raise IndexError("A pilha está vazia!")
            auxiliar = self.topo
            self.topo = self.topo.proximo
            self.contador -= 1
            return auxiliar
        except IndexError as error:
            print(error)
        
    def list(self):
        atual = self.topo
        for _ in range(self.contador):
            print(atual.valor)
            atual = atual.proximo
