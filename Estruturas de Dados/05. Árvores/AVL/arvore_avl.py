from elemento import Elemento


class ArvoreAVL:
    def __init__(self):
        self.__raiz = None

    @property
    def raiz(self) -> Elemento | None:
        return self.__raiz

    @raiz.setter
    def raiz(self, raiz: Elemento | None):
        self.__raiz = raiz

    def inserir_valor(self, valor: int):
        self.raiz = self.__inserir(self.raiz, valor)

    def deletar_valor(self, valor: int):
        self.raiz = self.__deletar(self.raiz, valor)

    def buscar_valor(self, valor: int) -> Elemento | None:
        return self.__buscar(self.raiz, valor)

    def __inserir(self, raiz: Elemento | None, valor: int) -> Elemento:
        if not raiz:
            return Elemento(valor)
        elif valor < raiz.valor:
            raiz.esquerda = self.__inserir(raiz.esquerda, valor)
        else:
            raiz.direita = self.__inserir(raiz.direita, valor)
    
        raiz.altura = 1 + max(self.__altura(raiz.esquerda), self.__altura(raiz.direita))
        fator_balanceamento = self.__fator_balanceamento(raiz)
    
        if fator_balanceamento > 1 and self.__fator_balanceamento(raiz.esquerda) >= 0:
            return self.__rotacao_direita(raiz)
    
        if fator_balanceamento < -1 and self.__fator_balanceamento(raiz.direita) <= 0:
            return self.__rotacao_esquerda(raiz)
    
        if fator_balanceamento > 1 and self.__fator_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.__rotacao_esquerda(raiz.esquerda)
            return self.__rotacao_direita(raiz)
    
        if fator_balanceamento < -1 and self.__fator_balanceamento(raiz.direita) > 0:
            raiz.direita = self.__rotacao_direita(raiz.direita)
            return self.__rotacao_esquerda(raiz)
    
        return raiz

    def __deletar(self, raiz: Elemento | None, valor: int) -> Elemento | None:
        if not raiz:
            return raiz
    
        if valor < raiz.valor:
            raiz.esquerda = self.__deletar(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.__deletar(raiz.direita, valor)
        else:
            if not raiz.esquerda:
                temp = raiz.direita
                raiz = None
                return temp
            elif not raiz.direita:
                temp = raiz.esquerda
                raiz = None
                return temp
            
            temp = self.__menor_elemento(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self.__deletar(raiz.direita, temp.valor)
    
        raiz.altura = 1 + max(self.__altura(raiz.esquerda), self.__altura(raiz.direita))
        fator_balanceamento = self.__fator_balanceamento(raiz)
    
        if fator_balanceamento > 1 and self.__fator_balanceamento(raiz.esquerda) >= 0:
            return self.__rotacao_direita(raiz)
    
        if fator_balanceamento < -1 and self.__fator_balanceamento(raiz.direita) <= 0:
            return self.__rotacao_esquerda(raiz)
    
        if fator_balanceamento > 1 and self.__fator_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.__rotacao_esquerda(raiz.esquerda)
            return self.__rotacao_direita(raiz)
    
        if fator_balanceamento < -1 and self.__fator_balanceamento(raiz.direita) > 0:
            raiz.direita = self.__rotacao_direita(raiz.direita)
            return self.__rotacao_esquerda(raiz)
    
        return raiz

    def __buscar(self, raiz: Elemento | None, valor: int) -> Elemento | None:
        if not raiz or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.__buscar(raiz.esquerda, valor)
        return self.__buscar(raiz.direita, valor)

    def __altura(self, elemento: Elemento | None) -> int:
        if not elemento:
            return 0
        return elemento.altura

    def __fator_balanceamento(self, elemento: Elemento | None) -> int:
        if not elemento:
            return 0
        return self.__altura(elemento.esquerda) - self.__altura(elemento.direita)

    def __menor_elemento(self, raiz: Elemento) -> Elemento:
        atual = raiz
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def __rotacao_esquerda(self, el_desbalanceado: Elemento) -> Elemento:
        novo_topo = el_desbalanceado.direita
        subarvore_esquerda = novo_topo.esquerda
    
        novo_topo.esquerda = el_desbalanceado
        el_desbalanceado.direita = subarvore_esquerda
    
        el_desbalanceado.altura = 1 + max(self.__altura(el_desbalanceado.esquerda), self.__altura(el_desbalanceado.direita))
        novo_topo.altura = 1 + max(self.__altura(novo_topo.esquerda), self.__altura(novo_topo.direita))
    
        return novo_topo

    def __rotacao_direita(self, el_desbalanceado: Elemento) -> Elemento:
        novo_topo = el_desbalanceado.esquerda
        subarvore_direita = novo_topo.direita
    
        novo_topo.direita = el_desbalanceado
        el_desbalanceado.esquerda = subarvore_direita
    
        el_desbalanceado.altura = 1 + max(self.__altura(el_desbalanceado.esquerda), self.__altura(el_desbalanceado.direita))
        novo_topo.altura = 1 + max(self.__altura(novo_topo.esquerda), self.__altura(novo_topo.direita))
    
        return novo_topo
