""" 
A proposta deste exercício é justamente criar uma classe que simule um array, com seu comportamento convencional.
Ou seja, o array deve ter dados somente de um mesmo tipo - números inteiros -, bem como ter um limite de tamanho definido.
Na instanciação da classe que representa-o, dois parâmetros delimitarão os índices em que ele começa e termina.
Para simular as operações comuns, haverá um método para inserção e um para acesso; executados com índices proporcionais aos informados na instância.
"""


class SuperArray:
    def __init__(self, limite_inferior: int, limite_superior: int) -> None:
        try:
            if not (isinstance(limite_inferior, int) and isinstance(limite_superior, int)):
                raise TypeError("Os limites devem ser números inteiros!")
            self.__limite_inferior = limite_inferior
            self.__limite_superior = limite_superior
            self.__tamanho_array = abs(limite_superior - limite_inferior) + 1
            self.__array = [None] * self.__tamanho_array
        except TypeError as error:
            print(error)

    @property
    def limite_inferior(self) -> int:
        return self.__limite_inferior

    @property
    def limite_superior(self) -> int:
        return self.__limite_superior

    @property
    def tamanho_array(self) -> int:
        return self.__tamanho_array

    @property
    def array(self):
        return self.__array

    def ver_limites(self):
        return f"O limite inferior dado ao array foi {self.limite_inferior} e o limite superior dado ao array foi {self.limite_superior}."

    def atribuir_valor(self, posicao: int, valor: int):
        try:
            if not (isinstance(posicao, int)):
                raise TypeError("A posição deve ser um número inteiro!")
            if not (isinstance(valor, int)):
                raise TypeError("O valor deve ser um número inteiro!")
            index = self.__get_index(posicao)
            self.array[index] = valor
        except (TypeError, IndexError) as error:
            print(error)

    def acessar_posicao(self, posicao: int) -> int:
        try:
            if not (isinstance(posicao, int)):
                raise TypeError("A posição deve ser um número inteiro!")
            index = self.__get_index(posicao)
            return self.array[index]
        except (TypeError, IndexError) as error:
            print(error)

    def __get_index(self, posicao: int) -> int:
        if self.limite_inferior <= self.limite_superior:
            if not (self.limite_inferior <= posicao <= self.limite_superior):
                raise IndexError("Índice fora dos limites do array!")
            return posicao - self.limite_inferior
        else:
            if not (self.limite_superior <= posicao <= self.limite_inferior):
                raise IndexError("Índice fora dos limites do array!")
            return self.limite_inferior - posicao
