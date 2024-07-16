

class Elemento:
    def __init__(self, valor: str):
        try:
            if not(isinstance(valor, str)):
                raise TypeError("O valor do elemento deve ser uma string!")
            self.__valor = valor
            self.__proximo = None
        except TypeError as error:
            print(error)

    @property
    def valor(self) -> str:
        return self.__valor

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, elemento):
        try:
            if not(isinstance(elemento, Elemento)):
                raise TypeError("O próximo elemento deve ser um elemento!")
            self.__proximo = elemento
        except TypeError as error:
            print(error)
