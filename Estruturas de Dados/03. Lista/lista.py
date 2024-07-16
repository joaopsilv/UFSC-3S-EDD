from elemento import Elemento


class Lista:
    def __init__(self, tamanho: int):
        self.__tamanho = None
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        if isinstance(tamanho, int):
            self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho

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

    def __avançarKPosições(self, k: int):
        if k < 0:
            raise IndexError("Erro! A posicao deve ser um inteiro positivo")
        posicao_esperada = self.__posiçãoDe(self.acessarAtual().valor) + k
        if posicao_esperada <= self.tamanho:
            contador = 0
            while self.acessarAtual().proximo:
                if contador == k:
                    return
                self.cursor = self.cursor.proximo
                contador += 1
            posicao_atual = self.__posiçãoDe(self.acessarAtual().valor)
            if posicao_atual != self.tamanho and contador != k:
                raise IndexError("Erro! Nenhum elemento antecede a posicao submetida")
        else:
            raise IndexError("Erro! A posicao deve ser um inteiro positivo que nao ultrapasse o limite da lista")

    def __posiçãoDe(self, valor) -> int:
            self.__irParaPrimeiro()
            contador = 1
            while self.acessarAtual():
                if self.acessarAtual().valor == valor:
                    return contador
                self.cursor = self.cursor.proximo
                contador += 1
            else:
                self.__irParaPrimeiro()
            raise IndexError("Esta chave nao pertence a lista")

    def inserirAntesDoAtual(self, valor):
        try:
            cursor_temporario = self.acessarAtual()
            if self.__cheia():
                raise IndexError("A lista esta cheia!")
            if self.buscar(valor):
                raise IndexError("Erro! Este elemento ja pertence a lista")
            self.cursor = cursor_temporario
            novo = Elemento(valor)
            if self.__vazia():
                self.inserirComoPrimeiro(elemento=novo)
                self.inserirComoUltimo(elemento=novo)
            else:
                novo.proximo = self.acessarAtual()
                antes_do_atual = self.cursor.anterior
                novo.anterior = antes_do_atual
                if antes_do_atual:
                    antes_do_atual.proximo = novo
                self.cursor.anterior = novo
                if self.acessarAtual() == self.primeiro:
                    self.primeiro = novo
            self.cursor = novo
        except IndexError as e:
            print(e)

    def inserirDepoisAtual(self, valor):
        try:
            cursor_temporario = self.acessarAtual()
            if self.__cheia():
                raise IndexError("A lista esta cheia!")
            if self.buscar(valor):
                raise IndexError("Erro! Este elemento ja pertence a lista")
            self.cursor = cursor_temporario
            novo = Elemento(valor)
            if self.__vazia():
                self.inserirComoPrimeiro(elemento=novo)
                self.inserirComoUltimo(elemento=novo)
            else:
                novo.anterior = self.acessarAtual()
                depois_do_atual = self.cursor.anterior
                novo.proximo = depois_do_atual
                if depois_do_atual:
                    depois_do_atual.anterior = novo
                self.cursor.proximo = novo
                if self.acessarAtual() == self.ultimo:
                    self.ultimo = novo
            self.cursor = novo
        except IndexError as e:
            print(e)

    def inserirComoPrimeiro(self, valor = None, elemento = None):
        try:
            cursor_temporario = self.acessarAtual()
            if self.__cheia():
                raise IndexError("A lista esta cheia!")
            if self.buscar(valor):
                raise IndexError("Erro! Este elemento ja pertence a lista")
            self.cursor = cursor_temporario
            novo = elemento or Elemento(valor)
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

    def inserirComoUltimo(self, valor = None, elemento = None):
        try:
            cursor_temporario = self.acessarAtual()
            if self.__cheia():
                raise IndexError("A lista esta cheia!")
            if self.buscar(valor):
                raise IndexError("Erro! Este elemento ja pertence a lista")
            self.cursor = cursor_temporario
            novo = elemento or Elemento(valor)
            if self.__vazia():
                self.ultimo = novo
                self.primeiro = novo
                self.__irParaUltimo()
            else:
                self.__irParaUltimo()
                novo.anterior = self.acessarAtual()
                self.cursor.proximo = novo
                self.ultimo = novo
                self.__irParaUltimo()
        except IndexError as e:
            print(e)
    
    def inserirNaPosicao(self, k: int, valor):
        try:
            if not isinstance(k, int):
                raise ValueError("Erro! A posicao deve ser um numero inteiro")
            cursor_temporario = self.acessarAtual()
            if self.__cheia():
                raise IndexError("A lista esta cheia!")
            if self.buscar(valor):
                raise IndexError("Erro! Este elemento ja pertence a lista")
            self.cursor = cursor_temporario
            novo = Elemento(valor)
            if k == self.__posiçãoDe(self.ultimo and self.ultimo.valor) + 1:
                self.inserirComoUltimo(elemento=novo)
            elif k == 1:
                self.inserirComoPrimeiro(elemento=novo)
            else:
                self.__irParaPrimeiro()
                self.__avançarKPosições(k-1)
                antes_do_atual = self.acessarAtual().anterior
                novo.anterior = antes_do_atual
                novo.proximo = self.acessarAtual()
                if antes_do_atual:
                    antes_do_atual.proximo = novo
                self.cursor.anterior = novo
                self.cursor = novo
        except (IndexError, ValueError) as e:
            print(e)

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

    def excluirElemento(self, valor):
        atual = self.buscar(valor)
        if atual:
            self.excluirAtual()

    def excluirDaPosição(self, k: int):
        try:
            if not isinstance(k, int):
                raise ValueError("Erro! A posicao deve ser um numero inteiro")
            self.__irParaPrimeiro()
            self.__avançarKPosições(k-1)
            self.excluirAtual()
        except (IndexError, ValueError) as e:
            print(e)

    def buscar(self, valor) -> bool:
        try:
            return bool(self.__posiçãoDe(valor))
        except IndexError as e:
            print(e)

    def __vazia(self) -> bool:
        return not any([self.primeiro, self.ultimo])

    def __cheia(self) -> bool:
        try:
            return (self.__posiçãoDe(self.ultimo.valor) == self.tamanho) if self.ultimo else False
        except IndexError as e:
            print(e)
