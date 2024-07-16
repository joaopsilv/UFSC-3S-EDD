from elemento import Elemento


class FilaDinâmica:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__contador = 0

    @property
    def inicio(self) -> Elemento:
        return self.__inicio

    @inicio.setter
    def inicio(self, valor):
        self.__inicio = valor

    @property
    def fim(self) -> Elemento:
        return self.__fim

    @fim.setter
    def fim(self, valor):
        self.__fim = valor

    @property
    def contador(self) -> int:
        return self.__contador

    @contador.setter
    def contador(self, valor):
        self.__contador = valor

    def enqueue(self, valor):
        novo_elemento = Elemento(valor)
        if self.contador == 0:
            self.inicio = novo_elemento
        else:
            self.fim.proximo = novo_elemento
        self.fim = novo_elemento
        self.contador += 1

    def dequeue(self) -> Elemento:
        try:
            if self.contador == 0:
                raise IndexError("A fila está vazia!")
            auxiliar = self.inicio
            self.inicio = self.inicio.proximo
            self.contador -= 1
            return auxiliar
        except IndexError as error:
            print(error)

    def listar(self):
        atual = self.inicio
        for _ in range(self.contador):
            print(atual.valor)
            atual = atual.proximo
