from elemento import Elemento


class Lista:
    def __init__(self):
        self.__cursor = None
        self.__primeiro = None
        self.__ultimo = None

    @property
    def primeiro(self):
        return self.__primeiro

    @primeiro.setter
    def primeiro(self, elemento: Elemento):
        if isinstance(elemento, Elemento) or elemento is None:
            self.__primeiro = elemento

    @property
    def ultimo(self):
        return self.__ultimo

    @ultimo.setter
    def ultimo(self, elemento: Elemento):
        if isinstance(elemento, Elemento) or elemento is None:
            self.__ultimo = elemento

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, elemento: Elemento):
        self.__cursor = elemento

    def acessarAtual(self) -> Elemento | None:
        return self.__cursor

    def __irParaPrimeiro(self):
        if self.primeiro:
            self.cursor = self.primeiro

    def __irParaUltimo(self):
        if self.ultimo:
            self.cursor = self.ultimo

    def inserirComoPrimeiro(self, elemento):
        try:
            cursor_temporario = self.acessarAtual()
            if self.buscar(elemento.valor):
                raise IndexError("Erro! Este elemento ja pertence a lista")
            self.cursor = cursor_temporario
            novo = elemento
            if self.__vazia():
                self.primeiro = novo
                self.ultimo = novo
                self.__irParaPrimeiro()
            else:
                self.__irParaPrimeiro()
                novo.proximo = self.acessarAtual()
                self.cursor.anterior = novo
                self.primeiro = novo
                self.__irParaPrimeiro()
        except IndexError as e:
            print(e)

    def excluirElemento(self, valor):
        atual = self.buscar(valor)
        if atual:
            self.excluirAtual()

    def excluirAtual(self):
        try:
            if self.__vazia():
                raise IndexError("A lista esta vazia!")
            if self.acessarAtual() == self.primeiro:
                self.excluirPrimeiro()
            elif self.acessarAtual() == self.ultimo:
                self.excluirUltimo()
            else:
                antes_do_atual = self.acessarAtual().anterior
                depois_do_atual = self.acessarAtual().proximo
                antes_do_atual.proximo = depois_do_atual
                depois_do_atual.anterior = antes_do_atual
                self.cursor = antes_do_atual
        except IndexError as e:
            print(e)

    def excluirPrimeiro(self):
        try:
            if self.__vazia():
                raise IndexError("A lista esta vazia!")
            self.__irParaPrimeiro()
            depois_do_atual = self.acessarAtual().proximo
            if depois_do_atual:
                depois_do_atual.anterior = None
            else:
                self.ultimo = depois_do_atual
            self.primeiro = depois_do_atual
            if self.primeiro:
                self.__irParaPrimeiro()
            else:
                self.cursor = None
        except IndexError as e:
            print(e)

    def excluirUltimo(self):
        try:
            if self.__vazia():
                raise IndexError("A lista esta vazia!")
            self.__irParaUltimo()
            antes_do_atual = self.acessarAtual().anterior
            if antes_do_atual:
                antes_do_atual.proximo = None
            else:
                self.primeiro = antes_do_atual
            self.ultimo = antes_do_atual
            if self.ultimo:
                self.__irParaUltimo()
            else:
                self.cursor = None
        except IndexError as e:
            print(e)

    def buscar(self, valor: int) -> Elemento | None:
        try:
            self.__irParaPrimeiro()
            while self.acessarAtual():
                if self.acessarAtual().valor == valor:
                    return self.__cursor
                self.cursor = self.cursor.proximo
            else:
                self.__irParaPrimeiro()
            raise IndexError("Esta chave nao pertence a lista")
        except IndexError as e:
            print(e)

    def __vazia(self) -> bool:
        return not any([self.primeiro, self.ultimo])
