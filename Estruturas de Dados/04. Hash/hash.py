from elemento import Elemento
from lista import Lista


class Hash:
    def __init__(self, tamanho: int, fc: int):
        self.__tamanho = None
        self.__fc = None
        if isinstance(tamanho, int):
            self.__tamanho = tamanho
        if isinstance(fc, int):
            self.__fc = fc
        self.__num_grupos = self.__tamanho//self.__fc
        self.__tabela = [Lista() for _ in range(self.__num_grupos)]

    @property
    def num_grupos(self) -> int:
        return self.__num_grupos

    @property
    def tabela(self):
        return self.__tabela

    def incluir(self, id: int):
        novo = Elemento(id)
        index = novo.calculaBucket(self.num_grupos)
        self.tabela[index].inserirComoPrimeiro(novo)

    def buscar(self, id: int) -> Elemento | None:
        temporario = Elemento(id)
        index = temporario.calculaBucket(self.num_grupos)
        elemento = self.tabela[index].buscar(id)
        return elemento

    def excluir(self, id: int):
        temporario = Elemento(id)
        index = temporario.calculaBucket(self.num_grupos)
        self.tabela[index].excluirElemento(id)
