

class Jogo:
    def __init__(self):
        self.__id = None
        self.__titulo = None
        self.__nota = None
        self.__genero = None
        self.__plataforma = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota: float):
        if isinstance(nota, float):
            self.__nota = nota

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if isinstance(genero, str):
            self.__genero = genero

    @property
    def plataforma(self):
        return self.__plataforma

    @plataforma.setter
    def plataforma(self, plataforma: str):
        if isinstance(plataforma, str):
            self.__plataforma = plataforma
