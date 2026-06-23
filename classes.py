class Caracterizacao:
    def __init__(self,idade,genero,ano_academico,horas_estudo_dia,pressao_provas,performance_academica,nivel_extresse,nivel_ansiedade,nivel_depressao,horas_sono,atividade_fisica,suporte_social,tempo_tela,uso_internet,extresse_financeiro,expectativa_familiar):
            self.__idade = idade
            self.__genero = genero
            self.__ano_academico = ano_academico
            self.__horas_estudo_dia = horas_estudo_dia
            self.__pressao_provas = pressao_provas
            self.__performance_academica = performance_academica
            self.__nivel_extresse = nivel_extresse
            self.__nivel_ansiedade = nivel_ansiedade
            self.__nivel_depressao = nivel_depressao
            self.__horas_sono = horas_sono
            self.__atividade_fisica = atividade_fisica
            self.__suporte_social = suporte_social
            self.__tempo_tela = tempo_tela
            self.__uso_internet = uso_internet
            self.__extresse_financeiro = extresse_financeiro
            self.__expectativa_familiar = expectativa_familiar

            @property
            def idade(self):
                return self.__idade

            @idade.setter
            def idade(self, valor):
                if type(valor) == int:
                    self.__idade = valor
                    return True
                return False

            @property
            def genero(self):
                return self.__genero

            @genero.setter
            def genero(self, valor):
                if type(valor) == str:
                    self.__genero = valor
                    return True
                return False

            @property
            def ano_academico(self):
                return self.__ano_academico

            @ano_academico.setter
            def ano_academico(self, valor):
                if type(valor) == int:
                    self.__ano_academico = valor
                    return True
                return False

            @property
            def horas_estudo_dia(self):
                return self.__horas_estudo_dia

            @horas_estudo_dia.setter
            def horas_estudo_dia(self, valor):
                if type(valor) == float:
                    self.__horas_estudo_dia = valor
                    return True
                return False

            @property
            def pressao_provas(self):
                return self.__pressao_provas

            @pressao_provas.setter
            def pressao_provas(self, valor):
                if type(valor) == float:
                    self.__pressao_provas = valor
                    return True
                return False

            @property
            def performance_academica(self):
                return self.__performance_academica

            @performance_academica.setter
            def performance_academica(self, valor):
                if type(valor) == float:
                    self.__performance_academica = valor
                    return True
                return False

            @property
            def nivel_extresse(self):
                return self.__nivel_extresse

            @nivel_extresse.setter
            def nivel_extresse(self, valor):
                if type(valor) == float:
                    self.__nivel_extresse = valor
                    return True
                return False

            @property
            def nivel_ansiedade(self):
                return self.__nivel_ansiedade

            @nivel_ansiedade.setter
            def nivel_ansiedade(self, valor):
                if type(valor) == float:
                    self.__nivel_ansiedade = valor
                    return True
                return False

            @property
            def nivel_depressao(self):
                return self.__nivel_depressao

            @nivel_depressao.setter
            def nivel_depressao(self, valor):
                if type(valor) == float:
                    self.__nivel_depressao = valor
                    return True
                return False

            @property
            def horas_sono(self):
                return self.__horas_sono

            @horas_sono.setter
            def horas_sono(self, valor):
                if type(valor) == float:
                    self.__horas_sono = valor
                    return True
                return False

            @property
            def atividade_fisica(self):
                return self.__atividade_fisica

            @atividade_fisica.setter
            def atividade_fisica(self, valor):
                if type(valor) == float:
                    self.__atividade_fisica = valor
                    return True
                return False

            @property
            def suporte_social(self):
                return self.__suporte_social

            @suporte_social.setter
            def suporte_social(self, valor):
                if type(valor) == float:
                    self.__suporte_social = valor
                    return True
                return False

            @property
            def tempo_tela(self):
                return self.__tempo_tela

            @tempo_tela.setter
            def tempo_tela(self, valor):
                if type(valor) == float:
                    self.__tempo_tela = valor
                    return True
                return False

            @property
            def uso_internet(self):
                return self.__uso_internet

            @uso_internet.setter
            def uso_internet(self, valor):
                if type(valor) == float:
                    self.__uso_internet = valor
                    return True
                return False

            @property
            def estresse_financeiro(self):
                return self.__extresse_financeiro

            @estresse_financeiro.setter
            def estresse_financeiro(self, valor):
                if type(valor) == float:
                    self.__extresse_financeiro = valor
                    return True
                return False

            @property
            def expectativa_familiar(self):
                return self.__expectativa_familiar

            @expectativa_familiar.setter
            def expectativa_familiar(self, valor):
                if type(valor) == float:
                    self.__expectativa_familiar = valor
                    return True
                return False
              
class Usuario:
    def __init__(self,nome, senha, caracterizacao):
        self.nome = nome
        self.senha = senha
        self.caracteristicas= caracterizacao
        self.habitos = []
        self.conquistas = []

    def prever(self):
        pass
    def acessar_habitos(self):
        pass
    def adicionar_conquista(self):
        pass