import abc
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import random
from datetime import datetime
import csv


class DadosFactuais:
    def __init__(self,idade,genero,ano_academico):
            self.__idade = idade
            self.__genero = genero
            self.__ano_academico = ano_academico 
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

class Caracterizacao:
    def __init__(self,dados_factuais,horas_estudo_dia,pressao_provas,performance_academica,nivel_estresse,nivel_ansiedade,nivel_depressao,horas_sono,atividade_fisica,suporte_social,tempo_tela,uso_internet,estresse_financeiro,expectativa_familiar):
            self.dados_factuais = dados_factuais
            self.__horas_estudo_dia = horas_estudo_dia
            self.__pressao_provas = pressao_provas
            self.__performance_academica = performance_academica
            self.__nivel_estresse = nivel_estresse
            self.__nivel_ansiedade = nivel_ansiedade
            self.__nivel_depressao = nivel_depressao
            self.__horas_sono = horas_sono
            self.__atividade_fisica = atividade_fisica
            self.__suporte_social = suporte_social
            self.__tempo_tela = tempo_tela
            self.__uso_internet = uso_internet
            self.__estresse_financeiro = estresse_financeiro
            self.__expectativa_familiar = expectativa_familiar
    
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
    def nivel_estresse(self):
        return self.__nivel_estresse

    @nivel_estresse.setter
    def nivel_estresse(self, valor):
        if type(valor) == float:
            self.__nivel_estresse = valor
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
        return self.__estresse_financeiro
    
    @estresse_financeiro.setter
    def estresse_financeiro(self, valor):
        if type(valor) == float:
            self.__estresse_financeiro = valor
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

class ModeloIA():
    def prever(self,dados):
        tabela = pd.read_csv("student_mental_health_burnout_1M.csv")
        tradutor = LabelEncoder() 
        tabela['gender'] = tradutor.fit_transform(tabela['gender'])
        x = tabela.drop(['burnout_score','mental_health_index','risk_level','dropout_risk'], axis=1)
        y = tabela ['risk_level']
        ia_arvore = RandomForestClassifier()
        ia_arvore.fit(x,y)
        previsao = pd.DataFrame([{'age': dados.dados_factuais.idade,'gender': dados.dados_factuais.genero,'academic_year': dados.dados_factuais.ano_academico,'study_hours_per_day': dados.horas_estudo_dia,'exam_pressure': dados.pressao_provas,'academic_performance': dados.performance_academica,'stress_level': dados.nivel_estresse,'anxiety_score': dados.nivel_ansiedade,'depression_score': dados.nivel_depressao,'sleep_hours': dados.horas_sono,'physical_activity': dados.atividade_fisica,'social_support': dados.suporte_social,'screen_time': dados.tempo_tela,'internet_usage': dados.uso_internet,'financial_stress': dados.estresse_financeiro,'family_expectation': dados.expectativa_familiar}])
        previsao['gender'] = tradutor.transform(previsao['gender'])
        nova_previsao = ia_arvore.predict(previsao)
        return nova_previsao

class Habito (abc.ABC):
    nome = 'Habito'
    
    @abc.abstractmethod
    def motivar (self):
        pass
    
class DormirCedo(Habito):
    nome = 'dormir cedo'
    def motivar(self):
        return random.choice(["Dormir cedo hoje é investir em uma versão mais forte de você amanhã.","Seu corpo precisa de descanso tanto quanto sua mente precisa de foco.","Quem dorme cedo não perde tempo — ganha energia.","A disciplina de hoje é o sucesso de amanhã começando no seu sono.","Desligar agora é escolher acordar melhor depois.","Não é sobre dormir menos, é sobre viver melhor.","A noite bem dormida é o primeiro passo de um dia produtivo.","Seu futuro agradece cada hora de sono que você respeita hoje."])
    
    def calular_sono(self,inicio,fim):
        t1 = datetime.strptime(inicio,"%H:%M")
        t2 = datetime.strptime(fim,"%H:%M")
        if t2 < t1:
            t2 = t2.replace(day=2)
        return t2 - t1

class AtividadeFisica (Habito):
    nome = 'atividade fisica'
    def motivar(self):
        return random.choice(["Seu corpo pode até pedir para parar, mas sua mente decide continuar.","Um treino hoje é um passo a menos em direção à sua melhor versão.","Disciplina vence a motivação quando a vontade acaba.","Você não treina só o corpo, treina a mente também.","O esforço de hoje é o resultado de amanhã.","Não espere sentir vontade, crie o hábito.","Cada gota de suor te aproxima do seu objetivo.","O limite começa onde sua determinação acaba.","Treinar é investir em você mesmo.","Você é mais forte do que a desculpa que tentou te parar."])
    def calcular_IMC(self,peso,altura):
        return peso/(altura**2)

class Leitura (Habito):
    nome = 'leitura'
    def motivar(self):
        return random.choice(["Quem lê vive mil vidas em uma só.", "Ler é treinar a mente para enxergar o mundo de outra forma.", "Um livro por dia afasta a ignorância para sempre.", "A leitura abre portas que a realidade ainda não mostrou.", "Quem lê nunca está sozinho.", "Cada página lida é um passo no seu crescimento.", "Livros são academias para a mente.", "Ler hoje é pensar melhor amanhã.", "A leitura transforma curiosidade em conhecimento.", "Quanto mais você lê, mais você entende o mundo."])
    def calcular_media(self,paginas,dias):
        return paginas/dias
    
class Meditacao (Habito):
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
    def registrar_atividade(self,atividade):
        return f'{self.nome} - {atividade}'

class Conquista:
    def __init__(self,nome):
        self.nome = nome

class Usuario (AtividadeMixin):
    def __init__(self,nome, senha, caracterizacao,sistema):
        self.sistema = sistema
        self.nome = nome
        self.__senha = senha
        self.caracteristicas= caracterizacao
        self.atividades = []
        self.habitos = []
        self.conquistas = []
        self.atividades.append(self.registrar_atividade('criou conta'))
        sistema= sistema+self
        
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,nova_senha):
        if len(nova_senha) >=8:
            self.__senha = nova_senha

    def prever(self):
        self.atividades.append(self.registrar_atividade('fez previsão com RandomForest'))
        self.sistema.atualizar_sistema(self)
        return ModeloIA().prever(self.caracteristicas)

    def adicionar_conquista(self, nome):
        self.conquistas.append(Conquista(nome))
        self.atividades.append(self.registrar_atividade(f'obteve a conquista {nome}'))
        self.sistema.atualizar_sistema(self)
    
    def adicionar_habito(self,habito):
        self.habitos.append(habito)
        self.atividades.append(self.registrar_atividade(f'adiquiriu o habito {habito.nome}'))
        self.sistema.atualizar_sistema(self)

class Sistema:
    def __init__(self,senha):
        self.__senha = senha
        with open('usuarios.csv',"r") as lista_usuarios:
            users = list(csv.reader(lista_usuarios, delimiter=","))
        self.usuarios = users
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,nova_senha):
        if len(nova_senha) >=8:
            self.__senha = nova_senha
        
    def atualizar_sistema(self,usuario):
        lista_nova = []
        with open('usuarios.csv',"r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0].lower() != usuario.nome.lower():
                    lista_nova.append(linha)
                else:
                    lista_nova.append([usuario.nome,usuario.senha,str(usuario.caracteristicas),str(usuario.atividades),str(usuario.habitos),str(usuario.conquistas)])
        with open('usuarios.csv','w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(lista_nova)
            
    def __add__(self, usuario):
        with open('usuarios.csv',"a", newline='') as usuarios:
            escritor = csv.writer(usuarios)
            escritor.writerow([usuario.nome,usuario.senha,str(usuario.caracteristicas),str(usuario.atividades),str(usuario.habitos),str(usuario.conquistas)])
        self.usuarios.append([usuario.nome,usuario.senha,str(usuario.caracteristicas),str(usuario.atividades),str(usuario.habitos),str(usuario.conquistas)])
        return self
    
    def __sub__(self, usuario):
        lista_nova = []
        achou = False
        with open('usuarios.csv',"r") as usuarios:
            lista_usuarios = csv.reader(usuarios, delimiter=",")
            for linha in lista_usuarios:
                if (linha [0]).lower() != (usuario.nome).lower():
                    lista_nova.append(linha)
                elif (linha [0]).lower() == (usuario.nome).lower():
                    achou = True
        if achou == False: 
            return self
        with open ('usuarios.csv','w') as users: 
            for i,linha in enumerate(lista_nova):
                if i==0:
                    users.write(linha[0] +','+ linha[1] +',' + linha[2] +',' + linha[3] +','+ linha[4]+','+linha[5])
                else:
                    users.write('\n'+linha[0] +','+ linha[1] +',' + linha[2] +',' + linha[3] +','+ linha[4]+','+linha[5])
        self.usuarios = lista_nova
        return self

class AcessarSistema(abc.ABC):
    @abc.abstractmethod
    def listar_usuarios(self,sistema):
        pass

class Dev(Usuario,AcessarSistema):
    __senha_dev = 'DevDoSistema'
    
    def listar_usuarios(self,sistema):
        return sistema.usuarios
    
    def excluir_usuario(self, sistema,usuario):
        sistema = sistema - usuario
        return sistema

    def adicionar_usuario(self,sistema,usuario):
        sistema = sistema + usuario
        return sistema
    
    def mudar_senha(self,sistema,nova_senha):
        sistema.senha = nova_senha
    
    @property
    def senha_dev(self):
        return Dev.__senha_dev
    
    @senha_dev.setter
    def senha_dev(self,nova_senha):
        if len(nova_senha) >=8:
            Dev.senha_dev = nova_senha
            
class Mod(Usuario,AcessarSistema):
    __senha_mod = 'ModDoSistema'
    def listar_usuarios(self,sistema):
        nomes_usuarios = []
        for user in sistema.usuarios:
            nomes_usuarios.append(user[0])
        return nomes_usuarios
    
    @property
    def senha_mod(self):
        return Mod.__senha_mod
    
    @senha_mod.setter
    def senha(self,nova_senha):
        if len(nova_senha) >=8:
            Mod.__senha_mod = nova_senha
