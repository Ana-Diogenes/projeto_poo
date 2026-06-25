import abc
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import random
from datetime import datetime
import csv

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

class ModeloIA(abc.ABC):
    def __init__(self,nome):
        self.nome = nome
    @abc.abstractmethod
    def prever(self):
        pass

class Knn(ModeloIA):
    def prever(self):
        tabela = pd.read_csv("student_mental_health_burnout_1M.csv")
        tradutor = LabelEncoder() 
        tabela['gender'] = tradutor.fit_transform(tabela['gender'])
        x = tabela.drop(['burnout_score','mental_health_index','risk_level','dropout_risk'], axis=1)
        y = tabela ['risk_level']
        ia_knn = KNeighborsClassifier()
        ia_knn.fit(x,y)
        novos_usuarios = pd.read_csv('novos.csv').drop(['burnout_score','mental_health_index','dropout_risk'], axis=1)
        novos_usuarios['gender'] = tradutor.transform(novos_usuarios['gender'])
        nova_previsao = ia_knn.predict(novos_usuarios)
        return nova_previsao

class Arvore(ModeloIA):
    def prever(self):
        tabela = pd.read_csv("student_mental_health_burnout_1M.csv")
        tradutor = LabelEncoder() 
        tabela['gender'] = tradutor.fit_transform(tabela['gender'])
        x = tabela.drop(['burnout_score','mental_health_index','risk_level','dropout_risk'], axis=1)
        y = tabela ['risk_level']
        ia_arvore = RandomForestClassifier()
        ia_arvore.fit(x,y)
        novos_usuarios = pd.read_csv('novos.csv').drop(['burnout_score','mental_health_index','dropout_risk'], axis=1)
        novos_usuarios['gender'] = tradutor.transform(novos_usuarios['gender'])
        nova_previsao = ia_arvore.predict(novos_usuarios)
        return nova_previsao

class DormirCedo:
    nome = 'dormir cedo'
    def motivar(self):
        return random.choice(["Dormir cedo hoje é investir em uma versão mais forte de você amanhã.","Seu corpo precisa de descanso tanto quanto sua mente precisa de foco.","Quem dorme cedo não perde tempo — ganha energia.","A disciplina de hoje é o sucesso de amanhã começando no seu sono.","Desligar agora é escolher acordar melhor depois.","Não é sobre dormir menos, é sobre viver melhor.","A noite bem dormida é o primeiro passo de um dia produtivo.","Seu futuro agradece cada hora de sono que você respeita hoje."])
    
    def calular_sono(self,inicio,fim):
        t1 = datetime.strptime(inicio,"%H:%M")
        t2 = datetime.strptime(fim,"%H:%M")
        if t2 < t1:
            t2 = t2.replace(day=2)
        return t2 - t1

class AtividadeFisica:
    nome = 'atividade fisica'
    def motivar(self):
        return random.choice(["Seu corpo pode até pedir para parar, mas sua mente decide continuar.","Um treino hoje é um passo a menos em direção à sua melhor versão.","Disciplina vence a motivação quando a vontade acaba.","Você não treina só o corpo, treina a mente também.","O esforço de hoje é o resultado de amanhã.","Não espere sentir vontade, crie o hábito.","Cada gota de suor te aproxima do seu objetivo.","O limite começa onde sua determinação acaba.","Treinar é investir em você mesmo.","Você é mais forte do que a desculpa que tentou te parar."])
    def calcular_IMC(self,peso,altura):
        return peso/(altura**2)

class Leitura:
    nome = 'leitura'
    def motivar(self):
        return random.choice(["Quem lê vive mil vidas em uma só.", "Ler é treinar a mente para enxergar o mundo de outra forma.", "Um livro por dia afasta a ignorância para sempre.", "A leitura abre portas que a realidade ainda não mostrou.", "Quem lê nunca está sozinho.", "Cada página lida é um passo no seu crescimento.", "Livros são academias para a mente.", "Ler hoje é pensar melhor amanhã.", "A leitura transforma curiosidade em conhecimento.", "Quanto mais você lê, mais você entende o mundo."])
    def calcular_media(self,paginas,dias):
        return paginas/dias
class Meditacao:
    nome = 'meditacao'
    def motivar(self):
        return random.choice(["Respire fundo e permita que sua mente encontre a calma.", "Cada respiração é uma oportunidade de recomeçar.", "O silêncio interior é uma fonte inesgotável de força.", "Você não precisa controlar tudo; apenas esteja presente.", "A paz que você procura já existe dentro de você.", "Deixe os pensamentos passarem como nuvens no céu.", "Seu bem-estar começa com um momento de atenção plena.", "Respire tranquilidade, expire preocupações.", "A serenidade cresce quando você desacelera."])
    def calcular_tempo_meditacao(self,inicio,fim):
        t1 = datetime.strptime(inicio,"%H:%M")
        t2 = datetime.strptime(fim,"%H:%M")
        if t2 < t1:
            t2 = t2.replace(day=2)
        return t2 - t1


class AtividadeMixin:
    def registrar_atividade(usuario,atividade):
        return f'{usuario} - {atividade}'

class Conquista:
    def __init__(self,nome):
        self.nome = nome

class Usuario (AtividadeMixin):
    def __init__(self,nome, senha, caracterizacao):
        self.nome = nome
        self.senha = senha
        self.caracteristicas= caracterizacao
        self.habitos = []
        self.conquistas = []
        self.registrar_atividade(self.nome,'criou conta')

    def prever(self,modelo):
        if modelo == 'knn':
            Knn('knn').prever()
            self.registrar_atividade(self.nome,'fez previsão com KNeighbors')
        elif modelo == 'arvore':
            Arvore('arvore').prever()
            self.registrar_atividade(self.nome,'fez previsão com RandomForest')

    def adicionar_conquista(self, nome):
        self.conquistas.append(Conquista(nome))
        self.registrar_atividade(self.nome,f'obteve a conquista {nome}')

class Sistema:
    def __init__(self):
        self.__senha = 'DemetriosMelhorProfessor'
        usuarios = ''
        with open('usuarios.csv',"r") as lista_usuarios:
            usuarios = csv.reader(lista_usuarios, delimiter=",")
        self.usuarios = usuarios
