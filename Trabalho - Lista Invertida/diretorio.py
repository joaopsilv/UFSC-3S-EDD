

class Diretorio:
    def __init__(self, criterio: str):
        self.__criterio = criterio
        self.__indices = {}

    @property
    def criterio(self):
        return self.__criterio

    @property
    def indices(self):
        return self.__indices

    def add_valor(self, novo_valor):
        if novo_valor not in self.indices.keys():
            self.indices[novo_valor] = []

    def add_identificador(self, valor, novo_id):
        self.add_valor(valor)
        if novo_id not in self.indices[valor]:
            self.indices[valor].append(novo_id)
