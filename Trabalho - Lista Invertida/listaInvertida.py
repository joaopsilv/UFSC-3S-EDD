import json
from diretorio import Diretorio
from jogo import Jogo


class ListaInvertida:
    def __init__(self):
        self.__documentos = []
        self.__diretorios = []

    def inicializar(self):
        self.menu()

    def mostrar_opcoes(self):
        print(f"{'OPÇÕES':-^30}")
        print('1 - Exibir todos jogos')
        print('2 - Carregar dados pre-definidos')
        print('3 - Incluir jogo')
        print('4 - Remover jogo')
        print('5 - Busca Simples')
        print('6 - Busca Composta')
        print('0 - Encerrar')
        num = int(input())
        return num if num in range(7) else 0

    def menu(self):
        opcoes = {
            1: self.exibir_documentos,
            2: self.carga,
            3: self.incluir_documento,
            4: self.remover_documento,
            5: self.busca_simples,
            6: self.busca_composta,
            0: self.encerrar
        }

        while True:
            try:
                opcoes[self.mostrar_opcoes()]()
            except ValueError:
                break

    def recolher_dados_inclusao(self):
        print(f"{'JOGO':-^30}")
        titulo = input('Titulo: ')
        nota = float(input('Nota: '))
        genero = input('Genero: ')
        plataforma = input('Plataforma: ')
        return {'titulo': titulo, 'nota': nota, 'genero': genero, 'plataforma': plataforma}

    def recolher_dados_busca_simples(self):
        print(f"{'BUSCA SIMPLES':-^30}")
        criterio = input('Criterio: ')
        valor = input('Valor: ')
        return {'criterio': criterio, 'valor': valor}

    def recolher_dados_busca_composta(self):
        print(f"{'BUSCA COMPOSTA':-^30}")
        criterio1 = input('Criterio 1: ')
        valor1 = input('Valor 1: ')
        print('-'*5)
        criterio2 = input('Criterio 2: ')
        valor2 = input('Valor 2: ')
        return {'criterio1': criterio1, 'valor1': valor1, 'criterio2': criterio2, 'valor2': valor2}

    def carga(self):
        file = open('jogos.json')
        dados = json.load(file)
        for jogo in dados:
            self.incluir_documento(jogo)
        file.close()

    def busca_simples(self):
        dados = self.recolher_dados_busca_simples()
        diretorio = self.__find_dir_by_criterio(dados['criterio'].lower())
        if not diretorio:
            print("Nao existe diretorio para este criterio")
        else:
            print(f"{'RESULTADO':-^30}")
            valor = self.__tratar_numero(dados['valor'])

            if valor not in diretorio.indices.keys():
                print("Este criterio nao atende ao valor passado")
            else:
                resultado = diretorio.indices[valor]
                if not resultado:
                    print("Nenhum jogo corresponde a busca")
                else:
                    for id in resultado:
                        jogo = self.__find_document_by_id(id)
                        self.exibir_jogo(jogo)

    def busca_composta(self):
        dados = self.recolher_dados_busca_composta()
        diretorio1 = self.__find_dir_by_criterio(dados['criterio1'].lower())
        diretorio2 = self.__find_dir_by_criterio(dados['criterio2'].lower())
        if not diretorio1:
            print("Nao existe diretorio para o criterio 1")
        elif not diretorio2:
            print("Nao existe diretorio para o criterio 2")
        else:
            print(f"{'RESULTADO':-^30}")
            valor1 = self.__tratar_numero(dados['valor1'])
            valor2 = self.__tratar_numero(dados['valor2'])
            if valor1 not in diretorio1.indices.keys():
                print("O criterio 1 nao atende ao valor passado")
            elif valor2 not in diretorio2.indices.keys():
                print("O criterio 2 nao atende ao valor passado")
            else:
                resultado = set(diretorio1.indices[valor1]).intersection(diretorio2.indices[valor2])
                if not resultado:
                    print("Nenhum jogo corresponde a busca")
                else:
                    for id in resultado:
                        jogo = self.__find_document_by_id(id)
                        self.exibir_jogo(jogo)

    def incluir_documento(self, jogo_dict = None):
        dados = jogo_dict or self.recolher_dados_inclusao()
        jogo = self.__find_document_by_titulo(dados['titulo'])
        if jogo:
            print("Este jogo ja foi incluido")
        else:
            jogo = Jogo()
            ultimo_id = self.__documentos[-1].id if self.__documentos else 0
            jogo.id = ultimo_id + 1
            jogo.titulo = dados['titulo']
            for col in ('nota', 'genero', 'plataforma'):
                setattr(jogo, col, dados[col])
                diretorio = self.__find_dir_by_criterio(col) or Diretorio(col)
                diretorio.add_identificador(getattr(jogo, col), jogo.id)
                self.__diretorios.append(diretorio)
            self.__documentos.append(jogo)
            print("Jogo incluido com sucesso")

    def remover_documento(self):
        print(f"{'SELECIONAR JOGO':-^30}")
        titulo = input('Titulo: ')
        jogo = self.__find_document_by_titulo(titulo)
        if not jogo:
            print("Este jogo nao existe")
        else:
            self.__documentos.remove(jogo)
            for dir in self.__diretorios:
                for val, ids in dir.indices.items():
                   if jogo.id in ids:
                       dir.indices[val].remove(jogo.id)
            print("Jogo excluido com sucesso")

    def exibir_documentos(self):
        print(f"{'JOGOS':-^30}")
        if not self.__documentos:
            print("Nenhum jogo foi incluido")
        for jogo in self.__documentos:
            self.exibir_jogo(jogo)

    def exibir_jogo(self, jogo: Jogo):
        print(f"{'ID:':<15} {jogo.id}")
        print(f"{'Titulo:':<15} {jogo.titulo}")
        print(f"{'Nota:':<15} {jogo.nota}")
        print(f"{'Genero:':<15} {jogo.genero}")
        print(f"{'Plataforma:':<15} {jogo.plataforma}")
        print()

    def encerrar(self):
        exit(0)

    def __tratar_numero(self, str_num):
        if str_num.replace('.', '').isnumeric():
            return float(str_num)
        return str_num

    def __find_document_by_id(self, id):
        for doc in self.__documentos:
            if doc.id == id:
                return doc
        return None

    def __find_document_by_titulo(self, titulo):
        for doc in self.__documentos:
            if doc.titulo == titulo:
                return doc
        return None

    def __find_dir_by_criterio(self, criterio):
        for dir in self.__diretorios:
            if dir.criterio == criterio:
                return dir
        return None
