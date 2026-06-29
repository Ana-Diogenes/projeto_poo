import customtkinter as ctk

# ================== CORES ==================

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_CAMPO = "#E59B90"
COR_HOVER = "#D9867C"
COR_TEXTO = "#8B5C5C"
COR_TEXTO_BOTAO = "#FFF2C9"
COR_CAIXA = "#FAC1A7"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ================== TELA INICIAL ==================

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew")
        conteudo.grid_columnconfigure(0, weight=1)
        conteudo.grid_columnconfigure(1, weight=0)
        conteudo.grid_columnconfigure(2, weight=1)
        conteudo.grid_rowconfigure(0, weight=2)
        conteudo.grid_rowconfigure(1, weight=0)
        conteudo.grid_rowconfigure(2, weight=0)
        conteudo.grid_rowconfigure(3, weight=2)
        titulo = ctk.CTkLabel(conteudo, text="Sinapse", font=("Arial", 48, "bold"), text_color=COR_TITULO)
        titulo.grid(row=1, column=1, pady=(0, 40))
        frame_botoes = ctk.CTkFrame(conteudo, fg_color="transparent")
        frame_botoes.grid(row=2, column=1)
        entrar = ctk.CTkButton(frame_botoes, text="Entrar na conta", width=200, height=70, corner_radius=22, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO_BOTAO, font=("Arial", 22, "bold"), command=self.controlador.mostrar_login)
        entrar.grid(row=0, column=0, padx=18)
        criar = ctk.CTkButton(frame_botoes, text="Criar Conta", width=200, height=70, corner_radius=22, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO_BOTAO, font=("Arial", 22, "bold"), command=self.controlador.mostrar_cadastro)
        criar.grid(row=0, column=1, padx=18)
        assinatura = ctk.CTkLabel(conteudo, text="☆ Ana-Diogenes", font=("Arial", 18), text_color=COR_TITULO)
        assinatura.place(relx=0.98, rely=0.97, anchor="se")

# ================== TELA LOGIN ==================

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_campo(self, parent, texto, ocultar=False):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 22))
        label = ctk.CTkLabel(frame, text=texto, font=("Arial", 18), text_color=COR_TEXTO)
        label.pack(anchor="s")
        entry = ctk.CTkEntry(frame, width=490, height=42, corner_radius=8, border_width=0, fg_color=COR_CAMPO, text_color="white", show="*" if ocultar else "")
        entry.pack(anchor="s", pady=(6, 0))
        return entry

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=60, pady=25)
        titulo = ctk.CTkLabel(conteudo, text="Sinapse", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.pack()
        subtitulo = ctk.CTkLabel(conteudo, text="Entre na sua conta", font=("Arial", 18), text_color=COR_TEXTO)
        subtitulo.pack(pady=(0, 25))
        self.nome = self.criar_campo(conteudo, "Nome")
        self.senha = self.criar_campo(conteudo, "Senha", ocultar=True)
        avancar = ctk.CTkButton(conteudo, text=">", width=65, height=65, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.fazer_login)
        avancar.place(relx=1, rely=1, anchor="se", x=-10, y=-5)
        voltar = ctk.CTkButton(conteudo, text="<", width=65, height=65, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.controlador.mostrar_inicial)
        voltar.place(relx=0, rely=1, anchor="sw", x=10, y=-5)

    def fazer_login(self):
        print("Nome:", self.nome.get())
        print("Senha:", self.senha.get())
        self.controlador.mostrar_principal()

# ================== TELA CADASTRO ==================

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_campo(self, parent, texto, ocultar=False):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 22))
        label = ctk.CTkLabel(frame, text=texto, font=("Arial", 18), text_color=COR_TEXTO)
        label.pack(anchor="s")
        entry = ctk.CTkEntry(frame, width=490, height=42, corner_radius=8, border_width=0, fg_color=COR_CAMPO, text_color="white", show="*" if ocultar else "")
        entry.pack(anchor="s", pady=(6, 0))
        return entry

    def criar_checkbox(self, parent, texto):
        return ctk.CTkCheckBox(parent, text=texto, font=("Arial", 16), text_color=COR_TEXTO, fg_color=COR_CAMPO, hover_color=COR_HOVER, border_color=COR_CAMPO, checkmark_color="white", checkbox_width=24, checkbox_height=24, corner_radius=20)

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=60, pady=25)
        titulo = ctk.CTkLabel(conteudo, text="Sinapse", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.pack()
        subtitulo = ctk.CTkLabel(conteudo, text="Vamos criar sua conta!", font=("Arial", 18), text_color=COR_TEXTO)
        subtitulo.pack(pady=(0, 25))
        self.nome = self.criar_campo(conteudo, "Nome")
        self.senha = self.criar_campo(conteudo, "Senha", ocultar=True)
        pergunta = ctk.CTkLabel(conteudo, text="Quais hábitos você deseja adquirir?", font=("Arial", 17), text_color=COR_TEXTO, fg_color="#FFC7A6", corner_radius=0, width=260, height=35)
        pergunta.pack(pady=(0, 20))
        habitos = ctk.CTkFrame(conteudo, fg_color="transparent")
        habitos.pack()
        coluna1 = ctk.CTkFrame(habitos, fg_color="transparent")
        coluna1.grid(row=0, column=0, padx=30)
        coluna2 = ctk.CTkFrame(habitos, fg_color="transparent")
        coluna2.grid(row=0, column=1, padx=30)
        self.dormir = self.criar_checkbox(coluna1, "Dormir cedo")
        self.dormir.pack(anchor="w", pady=12)
        self.atividade = self.criar_checkbox(coluna1, "Praticar atividade física")
        self.atividade.pack(anchor="w", pady=12)
        self.leitura = self.criar_checkbox(coluna2, "Leitura")
        self.leitura.pack(anchor="w", pady=12)
        self.meditacao = self.criar_checkbox(coluna2, "Meditação")
        self.meditacao.pack(anchor="w", pady=12)
        avancar = ctk.CTkButton(conteudo, text=">", width=65, height=65, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.fazer_cadastro)
        avancar.place(relx=1, rely=1, anchor="se", x=-10, y=-5)
        voltar = ctk.CTkButton(conteudo, text="<", width=65, height=65, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.controlador.mostrar_inicial)
        voltar.place(relx=0, rely=1, anchor="sw", x=10, y=-5)

    def fazer_cadastro(self):
        print("Nome:", self.nome.get())
        print("Senha:", self.senha.get())
        habitos = []
        if self.dormir.get():
            habitos.append("Dormir cedo")
        if self.atividade.get():
            habitos.append("Atividade Física")
        if self.leitura.get():
            habitos.append("Leitura")
        if self.meditacao.get():
            habitos.append("Meditação")
        print("Hábitos:", habitos)
        self.controlador.mostrar_caracterizacao1()

# ================== TELA CARACTERIZAÇÃO 1 ==================

class TelaCaracterizacao1(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=40, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_campo(self, parent, texto):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 16))
        label = ctk.CTkLabel(frame, text=texto, text_color=COR_TEXTO, font=("Arial", 16))
        label.pack(anchor="w")
        entrada = ctk.CTkEntry(frame, width=285, height=42, corner_radius=10, border_width=0, fg_color=COR_CAMPO, text_color="white")
        entrada.pack(anchor="w", pady=(3, 0))
        return entrada

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=50, pady=20)
        conteudo.grid_columnconfigure((0, 1), weight=1)
        titulo = ctk.CTkLabel(conteudo, text="Sinapse", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.grid(row=0, column=0, columnspan=2)
        subtitulo = ctk.CTkLabel(conteudo, text="Vamos começar pela sua caracterização!", font=("Arial", 18), text_color=COR_TEXTO)
        subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 25))
        coluna_esquerda = ctk.CTkFrame(conteudo, fg_color="transparent")
        coluna_esquerda.grid(row=2, column=0, padx=(15, 35), sticky="n")
        coluna_direita = ctk.CTkFrame(conteudo, fg_color="transparent")
        coluna_direita.grid(row=2, column=1, padx=(35, 15), sticky="n")
        self.idade = self.criar_campo(coluna_esquerda, "Idade")
        genero_frame = ctk.CTkFrame(coluna_esquerda, fg_color="transparent")
        genero_frame.pack(fill="x", pady=(0, 16))
        genero_label = ctk.CTkLabel(genero_frame, text="Gênero", text_color=COR_TEXTO, font=("Arial", 16))
        genero_label.pack(anchor="w")
        self.genero = ctk.CTkComboBox(genero_frame, values=["Mulher", "Homem", "Outro"], width=285, height=42, corner_radius=10, border_width=0, fg_color=COR_CAMPO, button_color=COR_CAMPO, button_hover_color=COR_HOVER, dropdown_fg_color=COR_CAMPO, dropdown_hover_color=COR_HOVER, dropdown_text_color="white", text_color="white")
        self.genero.set("Mulher")
        self.genero.pack(anchor="w", pady=(3, 0))
        self.ano = self.criar_campo(coluna_esquerda, "Ano acadêmico")
        aviso = ctk.CTkLabel(coluna_esquerda, text="Avalie as demais categorias de 0-10", fg_color="#F7C29A", text_color=COR_TEXTO, corner_radius=5, font=("Arial", 14, "bold"), padx=8, pady=4)
        aviso.pack(anchor="w", pady=(0, 16))
        self.horas = self.criar_campo(coluna_esquerda, "Horas de estudo por dia")
        self.pressao = self.criar_campo(coluna_direita, "Pressão provas")
        self.performance = self.criar_campo(coluna_direita, "Performance acadêmica")
        self.estresse = self.criar_campo(coluna_direita, "Nível estresse")
        self.ansiedade = self.criar_campo(coluna_direita, "Nível ansiedade")
        avancar = ctk.CTkButton(conteudo, text=">", width=30, height=30, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.controlador.mostrar_caracterizacao2)
        avancar.place(relx=0.98, rely=0.97, anchor="se")

# ================== TELA CARACTERIZAÇÃO 2 ==================

class TelaCaracterizacao2(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=40, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_campo(self, parent, texto):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 16))
        label = ctk.CTkLabel(frame, text=texto, font=("Arial", 16), text_color=COR_TEXTO)
        label.pack(anchor="w")
        entry = ctk.CTkEntry(frame, width=285, height=42, corner_radius=10, border_width=0, fg_color=COR_CAMPO, text_color="white")
        entry.pack(anchor="w", pady=(3, 0))
        return entry

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=50, pady=20)
        conteudo.grid_columnconfigure((0, 1), weight=1)
        titulo = ctk.CTkLabel(conteudo, text="Sinapse", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.grid(row=0, column=0, columnspan=2)
        subtitulo = ctk.CTkLabel(conteudo, text="Vamos começar pela sua caracterização!", font=("Arial", 18), text_color=COR_TEXTO)
        subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 25))
        coluna_esquerda = ctk.CTkFrame(conteudo, fg_color="transparent")
        coluna_esquerda.grid(row=2, column=0, padx=(15, 35), sticky="n")
        coluna_direita = ctk.CTkFrame(conteudo, fg_color="transparent")
        coluna_direita.grid(row=2, column=1, padx=(35, 15), sticky="n")
        self.depressao = self.criar_campo(coluna_esquerda, "Nível depressão")
        self.sono = self.criar_campo(coluna_esquerda, "Horas de sono")
        self.atividade = self.criar_campo(coluna_esquerda, "Atividade física")
        self.suporte = self.criar_campo(coluna_esquerda, "Suporte social")
        self.tela = self.criar_campo(coluna_direita, "Tempo tela")
        self.internet = self.criar_campo(coluna_direita, "Uso de internet")
        self.financeiro = self.criar_campo(coluna_direita, "Estresse financeiro")
        self.familia = self.criar_campo(coluna_direita, "Expectativa familiar")
        avancar = ctk.CTkButton(conteudo, text=">", width=30, height=30, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.controlador.mostrar_principal)
        avancar.place(relx=0.98, rely=0.97, anchor="se")

# ================== TELA BURNOUT ==================

class TelaBurnout(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=(25, 40), pady=25)
        conteudo.grid_columnconfigure(0, weight=1)
        conteudo.grid_columnconfigure(1, weight=0)
        
        titulo = ctk.CTkLabel(conteudo, text="Síndrome de Burnout", font=("Arial", 30, "bold"), text_color=COR_TITULO)
        titulo.grid(row=0, column=0, sticky="w", pady=(5, 20))
        
        texto = "Síndrome de Burnout ou Síndrome do Esgotamento Profissional é um distúrbio\nemocional com sintomas de exaustão extrema, estresse e esgotamento físico\nresultante de situações de trabalho desgastante, que demandam muita\n\ncompetitividade ou responsabilidade. Traduzindo do inglês, \"burn\" quer\ndizer queima e \"out\" exterior.\n\n A Síndrome de Burnout também pode acontecer\nquando o profissional planeja ou é pautado para objetivos de trabalho muito\ndifíceis, situações em que a pessoa possa achar, por algum motivo, não ter\ncapacidades suficientes para os cumprir. Essa síndrome pode resultar em\nestado de depressão profunda e por isso é essencial procurar apoio\nprofissional no surgimento dos primeiros sintomas.\n\n Normalmente esses sintomas\nsurgem de forma leve, mas tendem a piorar com o passar dos dias. Por essa\nrazão, muitas pessoas acham que pode ser algo passageiro. Para evitar\nproblemas mais sérios e complicações da doença, é fundamental buscar apoio\nprofissional assim que notar qualquer sinal. Pode ser algo passageiro, como\npode ser o início da Síndrome de Burnout."
        
        texto_label = ctk.CTkLabel(conteudo, text=texto, justify="left", anchor="nw", font=("Arial", 14), text_color=COR_TEXTO)
        texto_label.grid(row=1, column=0, sticky="nw", padx=(0, 35))
        
        caixa = ctk.CTkFrame(conteudo, width=260, height=440, corner_radius=8, fg_color=COR_CAIXA)
        caixa.grid(row=0, column=1, rowspan=2, sticky="ne", padx=(10, 10))
        caixa.grid_propagate(False)
        
        titulo_sintomas = ctk.CTkLabel(caixa, text="Sintomas", font=("Arial", 20, "bold"), text_color=COR_TEXTO)
        titulo_sintomas.pack(pady=(15, 10))
        
        sintomas = ("• Cansaço excessivo,\n   físico e mental\n\n• Dificuldades de\n   concentração\n\n• Sentimentos de\n   incompetência\n\n• Dor de cabeça\n   frequente\n\n• Alterações no apetite\n\n• Sentimentos de\n   fracasso e insegurança\n\n• Alterações repentinas\n   de humor\n\n• Alteração nos\n   batimentos cardíacos")
        
        sintomas_label = ctk.CTkLabel(caixa, text=sintomas, justify="left", anchor="nw", font=("Arial", 13), text_color=COR_TEXTO)
        sintomas_label.pack(anchor="nw", padx=20, pady=(5, 15))
        
        voltar = ctk.CTkButton(conteudo, text="←", width=40, height=40, corner_radius=20, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 20, "bold"), command=self.controlador.mostrar_principal)
        voltar.place(relx=0.0, rely=1.0, anchor="sw")

# ================== TELA RESULTADO ==================
    
class TelaResultado(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=40, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=35, pady=25)
        conteudo.grid_rowconfigure(0, weight=1)
        conteudo.grid_columnconfigure(0, weight=1)
        
        painel = ctk.CTkFrame(conteudo, fg_color=COR_CAMPO, corner_radius=6)
        painel.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        
        titulo = ctk.CTkLabel(painel, text="Nível de risco:", font=("Arial", 26, "bold"), text_color=COR_TEXTO)
        titulo.pack(pady=(22, 0))
        
        risco = ctk.CTkLabel(painel, text="ALTO", font=("Arial", 46, "bold"), text_color=COR_TEXTO)
        risco.pack(pady=(0, 20))
        
        texto = ("Isso não significa necessariamente que você tenha a síndrome,\nmas é um sinal de que seu bem-estar merece atenção. O estresse constante,\na sobrecarga e o cansaço podem afetar sua saúde física e emocional\nse não forem cuidados.\n\nA boa notícia é que pequenas mudanças na rotina podem fazer uma grande\ndiferença. Desenvolver hábitos saudáveis, como dormir melhor, praticar\natividade física, reservar momentos para a leitura ou meditação e cuidar\ndo seu equilíbrio entre estudo, trabalho e descanso, pode contribuir\npara reduzir os fatores de risco.\n\nO Sinapse estará ao seu lado nessa jornada. Acompanhe seus hábitos\ndiariamente, mantenha a consistência e celebre cada pequena conquista.\nCuidar de você hoje é o primeiro passo para uma rotina mais saudável amanhã.")
        
        mensagem = ctk.CTkLabel(painel, text=texto, font=("Arial", 16), text_color=COR_TEXTO, justify="left", wraplength=730, anchor="nw")
        mensagem.pack(fill="both", expand=True, padx=28, pady=(0, 28))
        voltar = ctk.CTkButton(conteudo, text="Voltar", width=120, height=40, fg_color=COR_CAMPO,bg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO,font=("Arial", 16, "bold"),command=self.controlador.mostrar_principal)
        voltar.place(relx=0.0, rely=1.0, anchor="sw", x=640, y=-20)
    def proxima_pagina(self):
        print("Próxima página")

# ================== TELA HABITOS ==================

class TelaHabitos(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        barra.grid_columnconfigure(0, weight=1)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_opcao(self, parent, texto):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.var = ctk.BooleanVar()
        botao = ctk.CTkCheckBox(frame, text="", variable=self.var, width=30, height=30, checkbox_width=26, checkbox_height=26, corner_radius=30, fg_color=COR_CAMPO, hover_color=COR_HOVER, border_color=COR_CAMPO, checkmark_color="white")
        botao.pack(side="left", padx=(0, 15))
        label = ctk.CTkLabel(frame, text=texto, font=("Arial", 20), text_color=COR_TEXTO)
        label.pack(side="left")
        return frame, self.var

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=70, pady=35)
        titulo = ctk.CTkLabel(conteudo, text="Quais hábitos você\ndeseja adquirir?", font=("Arial", 28, "bold"), text_color=COR_TEXTO, justify="center")
        titulo.pack(pady=(20, 80))
        opcoes = ctk.CTkFrame(conteudo, fg_color="transparent")
        opcoes.pack()
        coluna1 = ctk.CTkFrame(opcoes, fg_color="transparent")
        coluna1.grid(row=0, column=0, padx=60)
        coluna2 = ctk.CTkFrame(opcoes, fg_color="transparent")
        coluna2.grid(row=0, column=1, padx=60)
        item, self.dormir = self.criar_opcao(coluna1, "Dormir cedo")
        item.pack(anchor="w", pady=25)
        item, self.atividade = self.criar_opcao(coluna1, "Praticar atividade física")
        item.pack(anchor="w", pady=25)
        item, self.leitura = self.criar_opcao(coluna2, "Leitura")
        item.pack(anchor="w", pady=25)
        item, self.meditacao = self.criar_opcao(coluna2, "Meditação")
        item.pack(anchor="w", pady=25)
        voltar = ctk.CTkButton(conteudo, text="<", width=66, height=66, corner_radius=40, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.proxima_tela)
        voltar.place(relx=1, rely=1, anchor="se", x=-10, y=-10)

    def proxima_tela(self):
        habitos = []
        if self.dormir.get():
            habitos.append("Dormir cedo")
        if self.atividade.get():
            habitos.append("Praticar atividade física")
        if self.leitura.get():
            habitos.append("Leitura")
        if self.meditacao.get():
            habitos.append("Meditação")
        print(habitos)
        self.controlador.mostrar_principal()

# ================== TELA CONQUISTAS ==================

class TelaConquistas(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=40, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=35, pady=25)
        conteudo.grid_columnconfigure(0, weight=1)
        conteudo.grid_rowconfigure(0, weight=1)
        
        painel = ctk.CTkFrame(conteudo, fg_color=COR_CAIXA, corner_radius=8)
        painel.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(1, weight=1)
        
        titulo = ctk.CTkLabel(painel, text="Conquistas", font=("Arial", 34, "bold"), text_color=COR_TITULO)
        titulo.grid(row=0, column=0, sticky="w", padx=30, pady=(25,15))
        
        caixa_texto = ctk.CTkScrollableFrame(painel, fg_color="#FFE1B0", corner_radius=5, scrollbar_button_color="#E59B90", scrollbar_button_hover_color="#D9867C")
        caixa_texto.grid(row=1, column=0, sticky="nsew", padx=28, pady=(0,30))
        caixa_texto.grid_columnconfigure(0, weight=1)
        
        texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin mattis rhoncus dapibus.\n\nNunc mi arcu, vestibulum in luctus eu, bibendum vitae felis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nProin luctus nulla a arcu dignissim ullamcorper. Aliquam sed dolor mollis, iaculis nibh eget, condimentum dui. Nunc iaculis hendrerit imperdiet.\n\nPraesent aliquam sem tellus, et condimentum nunc vulputate nec. Nam sed gravida erat, at interdum sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.\n\nCurabitur at maximus dui. Maecenas sed leo lectus. Nullam consectetur libero sem, non semper diam laoreet a. Donec a maximus tortor.\n\nNulla luctus et ligula ac eleifend. Pellentesque eu risus ac nisl sagittis luctus. Fusce rutrum nunc sem, non interdum purus scelerisque eleifend. Nulla facilisi.\n\nAliquam quis mi posuere, bibendum justo sagittis, sagittis leo. Quisque vel lacus quis arcu tincidunt efficitur ut non metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;"
        
        texto_label = ctk.CTkLabel(caixa_texto, text=texto, font=("Arial",16), text_color=COR_TEXTO, justify="left", anchor="nw", wraplength=650)
        texto_label.pack(fill="both", expand=True, padx=20, pady=15)
        
        voltar = ctk.CTkButton(conteudo, text="Voltar", width=120, height=40, fg_color=COR_CAMPO, bg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial",16,"bold"), command=self.controlador.mostrar_principal)
        voltar.place(relx=0, rely=1, anchor="sw", x=640, y=-20)

# ================== TELA ATIVIDADES ==================

class TelaAtividades(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=40, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i in range(5):
            barra.grid_rowconfigure(i, weight=1)
        for i, cor in enumerate(PALETA):
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=35, pady=25)
        conteudo.grid_columnconfigure(0, weight=1)
        conteudo.grid_rowconfigure(0, weight=1)
        
        painel = ctk.CTkFrame(conteudo, fg_color=COR_TITULO, corner_radius=8)
        painel.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(1, weight=1)
        
        titulo = ctk.CTkLabel(painel, text="Atividades", font=("Arial", 34, "bold"), text_color=COR_CAIXA)
        titulo.grid(row=0, column=0, sticky="w", padx=30, pady=(25,15))
        
        caixa_texto = ctk.CTkScrollableFrame(painel, fg_color="#FFE1B0", corner_radius=5, scrollbar_button_color="#E59B90", scrollbar_button_hover_color="#D9867C")
        caixa_texto.grid(row=1, column=0, sticky="nsew", padx=28, pady=(0,30))
        caixa_texto.grid_columnconfigure(0, weight=1)
        
        texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin mattis rhoncus dapibus.\n\nNunc mi arcu, vestibulum in luctus eu, bibendum vitae felis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nProin luctus nulla a arcu dignissim ullamcorper. Aliquam sed dolor mollis, iaculis nibh eget, condimentum dui. Nunc iaculis hendrerit imperdiet.\n\nPraesent aliquam sem tellus, et condimentum nunc vulputate nec. Nam sed gravida erat, at interdum sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.\n\nCurabitur at maximus dui. Maecenas sed leo lectus. Nullam consectetur libero sem, non semper diam laoreet a. Donec a maximus tortor.\n\nNulla luctus et ligula ac eleifend. Pellentesque eu risus ac nisl sagittis luctus. Fusce rutrum nunc sem, non interdum purus scelerisque eleifend. Nulla facilisi.\n\nAliquam quis mi posuere, bibendum justo sagittis, sagittis leo. Quisque vel lacus quis arcu tincidunt efficitur ut non metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;"
        
        texto_label = ctk.CTkLabel(caixa_texto, text=texto, font=("Arial",16), text_color=COR_TEXTO, justify="left", anchor="nw", wraplength=650)
        texto_label.pack(fill="both", expand=True, padx=20, pady=15)
        
        voltar = ctk.CTkButton(conteudo, text="Voltar", width=120, height=40, fg_color=COR_CAMPO, bg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial",16,"bold"), command=self.controlador.mostrar_principal)
        voltar.place(relx=0, rely=1, anchor="sw", x=640, y=-20)

# ================== TELA DORMIR CEDO ==================

class TelaDormirCedo(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i, cor in enumerate(PALETA):
            barra.grid_rowconfigure(i, weight=1)
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def calcular_sono(self):
        try:
            h_dormir, m_dormir = map(int, self.entrada_dormir.get().split(":"))
            h_acordar, m_acordar = map(int, self.entrada_acordar.get().split(":"))
            inicio = h_dormir * 60 + m_dormir
            fim = h_acordar * 60 + m_acordar
            if fim < inicio:
                fim += 24 * 60
            horas = (fim - inicio) / 60
            self.resultado.configure(text=f"{horas:.2f} horas")
        except:
            self.resultado.configure(text="Horário inválido")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=25, pady=20)
        
        titulo = ctk.CTkLabel(conteudo, text="Dormir cedo", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.pack(anchor="w", pady=(10, 8))
        
        frase = ctk.CTkLabel(conteudo, text="Dormir cedo hoje é investir em uma versão mais forte de você amanhã.", font=("Arial", 18, "italic"), text_color=COR_TITULO, fg_color=COR_CAIXA, corner_radius=5, height=45, anchor="w")
        frase.pack(fill="x", pady=(0, 35), ipady=10, padx=(0, 60))
        
        caixa = ctk.CTkFrame(conteudo, fg_color=COR_TITULO, corner_radius=5)
        caixa.pack(fill="x", padx=(0, 60))
        
        subtitulo = ctk.CTkLabel(caixa, text="Calcular tempo do sono", font=("Arial", 24, "bold"), text_color=COR_TEXTO_BOTAO)
        subtitulo.pack(anchor="w", padx=35, pady=(20, 20))
        
        linha = ctk.CTkFrame(caixa, fg_color="transparent")
        linha.pack(fill="x", padx=35)
        
        bloco1 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco1.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco1, text="Hora que dormi", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_dormir = ctk.CTkEntry(bloco1, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_dormir.pack(pady=(5, 0))
        
        bloco2 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco2.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco2, text="Hora que acordei", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_acordar = ctk.CTkEntry(bloco2, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_acordar.pack(pady=(5, 0))
        
        botao = ctk.CTkButton(linha, text="Enviar", width=140, height=45, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TITULO, font=("Arial", 18, "bold"), command=self.calcular_sono)
        botao.pack(side="left", pady=(25, 0))
        
        resultado_frame = ctk.CTkFrame(caixa, fg_color=COR_FUNDO, width=440, height=95, corner_radius=5)
        resultado_frame.pack(pady=30)
        resultado_frame.pack_propagate(False)
        
        ctk.CTkLabel(resultado_frame, text="Resultado:", font=("Arial", 20), text_color=COR_TITULO).place(x=10, y=10)
        
        self.resultado = ctk.CTkLabel(resultado_frame, text="00.00 horas", font=("Arial", 34, "bold"), text_color=COR_TITULO)
        self.resultado.place(relx=0.5, rely=0.55, anchor="center")
        
        sair = ctk.CTkButton(conteudo, text="Voltar", width=90, height=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 14, "bold"), command=self.controlador.mostrar_principal)
        sair.pack(anchor="e", pady=15)

# ================== TELA ATIVIDADE FISICA ==================

class TelaAtividadeFisica(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i, cor in enumerate(PALETA):
            barra.grid_rowconfigure(i, weight=1)
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def calcular_sono(self):
        try:
            h_dormir, m_dormir = map(int, self.entrada_dormir.get().split(":"))
            h_acordar, m_acordar = map(int, self.entrada_acordar.get().split(":"))
            inicio = h_dormir * 60 + m_dormir
            fim = h_acordar * 60 + m_acordar
            if fim < inicio:
                fim += 24 * 60
            horas = (fim - inicio) / 60
            self.resultado.configure(text=f"{horas:.2f} IMC bom")
        except:
            self.resultado.configure(text="Horário inválido")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=25, pady=20)
        
        titulo = ctk.CTkLabel(conteudo, text="Atidade física", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.pack(anchor="w", pady=(10, 8))
        
        frase = ctk.CTkLabel(conteudo, text="Seu corpo pode até pedir para parar, mas sua mente decide continuar.", font=("Arial", 18, "italic"), text_color=COR_TITULO, fg_color=COR_CAIXA, corner_radius=5, height=45, anchor="w")
        frase.pack(fill="x", pady=(0, 35), ipady=10, padx=(0, 60))
        
        caixa = ctk.CTkFrame(conteudo, fg_color=COR_TITULO, corner_radius=5)
        caixa.pack(fill="x", padx=(0, 60))
        
        subtitulo = ctk.CTkLabel(caixa, text="Calcular IMC", font=("Arial", 24, "bold"), text_color=COR_TEXTO_BOTAO)
        subtitulo.pack(anchor="w", padx=35, pady=(20, 20))
        
        linha = ctk.CTkFrame(caixa, fg_color="transparent")
        linha.pack(fill="x", padx=35)
        
        bloco1 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco1.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco1, text="Peso", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_dormir = ctk.CTkEntry(bloco1, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_dormir.pack(pady=(5, 0))
        
        bloco2 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco2.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco2, text="Altura", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_acordar = ctk.CTkEntry(bloco2, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_acordar.pack(pady=(5, 0))
        
        botao = ctk.CTkButton(linha, text="Enviar", width=140, height=45, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TITULO, font=("Arial", 18, "bold"), command=self.calcular_sono)
        botao.pack(side="left", pady=(25, 0))
        
        resultado_frame = ctk.CTkFrame(caixa, fg_color=COR_FUNDO, width=440, height=95, corner_radius=5)
        resultado_frame.pack(pady=30)
        resultado_frame.pack_propagate(False)
        
        ctk.CTkLabel(resultado_frame, text="Resultado:", font=("Arial", 20), text_color=COR_TITULO).place(x=10, y=10)
        
        self.resultado = ctk.CTkLabel(resultado_frame, text="--.- IMC", font=("Arial", 34, "bold"), text_color=COR_TITULO)
        self.resultado.place(relx=0.5, rely=0.55, anchor="center")
        
        sair = ctk.CTkButton(conteudo, text="Voltar", width=90, height=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 14, "bold"), command=self.controlador.mostrar_principal)
        sair.pack(anchor="e", pady=15)

# ================== TELA LEITURA ==================

class TelaLeitura(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i, cor in enumerate(PALETA):
            barra.grid_rowconfigure(i, weight=1)
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def calcular_sono(self):
        try:
            h_dormir, m_dormir = map(int, self.entrada_dormir.get().split(":"))
            h_acordar, m_acordar = map(int, self.entrada_acordar.get().split(":"))
            inicio = h_dormir * 60 + m_dormir
            fim = h_acordar * 60 + m_acordar
            if fim < inicio:
                fim += 24 * 60
            horas = (fim - inicio) / 60
            self.resultado.configure(text=f"{horas:.2f} horas")
        except:
            self.resultado.configure(text="Horário inválido")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=25, pady=20)
        
        titulo = ctk.CTkLabel(conteudo, text="Leitura", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.pack(anchor="w", pady=(10, 8))
        
        frase = ctk.CTkLabel(conteudo, text="Quem lê vive mil vidas em uma só.", font=("Arial", 18, "italic"), text_color=COR_TITULO, fg_color=COR_CAIXA, corner_radius=5, height=45, anchor="w")
        frase.pack(fill="x", pady=(0, 35), ipady=10, padx=(0, 60))
        
        caixa = ctk.CTkFrame(conteudo, fg_color=COR_TITULO, corner_radius=5)
        caixa.pack(fill="x", padx=(0, 60))
        
        subtitulo = ctk.CTkLabel(caixa, text="Calcular média de páginas lidas por dia", font=("Arial", 24, "bold"), text_color=COR_TEXTO_BOTAO)
        subtitulo.pack(anchor="w", padx=35, pady=(20, 20))
        
        linha = ctk.CTkFrame(caixa, fg_color="transparent")
        linha.pack(fill="x", padx=35)
        
        bloco1 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco1.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco1, text="Páginas", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_dormir = ctk.CTkEntry(bloco1, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_dormir.pack(pady=(5, 0))
        
        bloco2 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco2.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco2, text="Dias", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_acordar = ctk.CTkEntry(bloco2, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_acordar.pack(pady=(5, 0))
        
        botao = ctk.CTkButton(linha, text="Enviar", width=140, height=45, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TITULO, font=("Arial", 18, "bold"), command=self.calcular_sono)
        botao.pack(side="left", pady=(25, 0))
        
        resultado_frame = ctk.CTkFrame(caixa, fg_color=COR_FUNDO, width=440, height=95, corner_radius=5)
        resultado_frame.pack(pady=30)
        resultado_frame.pack_propagate(False)
        
        ctk.CTkLabel(resultado_frame, text="Resultado:", font=("Arial", 20), text_color=COR_TITULO).place(x=10, y=10)
        
        self.resultado = ctk.CTkLabel(resultado_frame, text="--.- páginas por dia", font=("Arial", 34, "bold"), text_color=COR_TITULO)
        self.resultado.place(relx=0.5, rely=0.55, anchor="center")
        
        sair = ctk.CTkButton(conteudo, text="Voltar", width=90, height=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 14, "bold"), command=self.controlador.mostrar_principal)
        sair.pack(anchor="e", pady=15)

# ================== TELA MEDITACAO ==================

class TelaMeditacao(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i, cor in enumerate(PALETA):
            barra.grid_rowconfigure(i, weight=1)
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def calcular_sono(self):
        try:
            h_dormir, m_dormir = map(int, self.entrada_dormir.get().split(":"))
            h_acordar, m_acordar = map(int, self.entrada_acordar.get().split(":"))
            inicio = h_dormir * 60 + m_dormir
            fim = h_acordar * 60 + m_acordar
            if fim < inicio:
                fim += 24 * 60
            horas = (fim - inicio) / 60
            self.resultado.configure(text=f"{horas:.2f} horas")
        except:
            self.resultado.configure(text="Horário inválido")

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=25, pady=20)
        
        titulo = ctk.CTkLabel(conteudo, text="Meditação", font=("Arial", 42, "bold"), text_color=COR_TITULO)
        titulo.pack(anchor="w", pady=(10, 8))
        
        frase = ctk.CTkLabel(conteudo, text="Respire fundo e permita que sua mente encontre a calma.", font=("Arial", 18, "italic"), text_color=COR_TITULO, fg_color=COR_CAIXA, corner_radius=5, height=45, anchor="w")
        frase.pack(fill="x", pady=(0, 35), ipady=10, padx=(0, 60))
        
        caixa = ctk.CTkFrame(conteudo, fg_color=COR_TITULO, corner_radius=5)
        caixa.pack(fill="x", padx=(0, 60))
        
        subtitulo = ctk.CTkLabel(caixa, text="Calcular tempo meditação", font=("Arial", 24, "bold"), text_color=COR_TEXTO_BOTAO)
        subtitulo.pack(anchor="w", padx=35, pady=(20, 20))
        
        linha = ctk.CTkFrame(caixa, fg_color="transparent")
        linha.pack(fill="x", padx=35)
        
        bloco1 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco1.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco1, text="Hora do inicio da meditação", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_dormir = ctk.CTkEntry(bloco1, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_dormir.pack(pady=(5, 0))
        
        bloco2 = ctk.CTkFrame(linha, fg_color="transparent")
        bloco2.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(bloco2, text="Hora do fim da meditação", font=("Arial", 16), text_color="#FFD7C5").pack(anchor="w")
        
        self.entrada_acordar = ctk.CTkEntry(bloco2, width=220, height=40, fg_color=COR_FUNDO, border_width=0, text_color=COR_TEXTO)
        self.entrada_acordar.pack(pady=(5, 0))
        
        botao = ctk.CTkButton(linha, text="Enviar", width=140, height=45, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TITULO, font=("Arial", 18, "bold"), command=self.calcular_sono)
        botao.pack(side="left", pady=(25, 0))
        
        resultado_frame = ctk.CTkFrame(caixa, fg_color=COR_FUNDO, width=440, height=95, corner_radius=5)
        resultado_frame.pack(pady=30)
        resultado_frame.pack_propagate(False)
        
        ctk.CTkLabel(resultado_frame, text="Resultado:", font=("Arial", 20), text_color=COR_TITULO).place(x=10, y=10)
        
        self.resultado = ctk.CTkLabel(resultado_frame, text="00.00 horas", font=("Arial", 34, "bold"), text_color=COR_TITULO)
        self.resultado.place(relx=0.5, rely=0.55, anchor="center")
        
        sair = ctk.CTkButton(conteudo, text="Voltar", width=90, height=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 14, "bold"), command=self.controlador.mostrar_principal)
        sair.pack(anchor="e", pady=15)

# ================== TELA PRINCIPAL ==================

class TelaPrincipal(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color=COR_FUNDO)
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.criar_barra()
        self.criar_conteudo()

    def criar_barra(self):
        barra = ctk.CTkFrame(self, width=55, fg_color="transparent", corner_radius=0)
        barra.grid(row=0, column=0, sticky="ns")
        barra.grid_propagate(False)
        for i, cor in enumerate(PALETA):
            barra.grid_rowconfigure(i, weight=1)
            faixa = ctk.CTkFrame(barra, fg_color=cor, corner_radius=0)
            faixa.grid(row=i, column=0, sticky="nsew")

    def criar_lista_habitos(self, parent):
        caixa = ctk.CTkFrame(parent, width=310, height=350, fg_color=COR_CAIXA, corner_radius=5)
        caixa.pack(pady=0, padx=10)
        caixa.pack_propagate(False)
        titulo = ctk.CTkLabel(caixa, text="Meus hábitos", font=("Arial",22), text_color=COR_TEXTO)
        titulo.pack(anchor="w", padx=40, pady=(15,10))
        habitos = ["Dormir cedo", "Atividade física", "Leitura", "Meditação"]
        for h in habitos:
            if h == 'Dormir cedo':
                comando = self.controlador.mostrar_dormir
            elif h == "Atividade física":
                comando = self.controlador.mostrar_atividade_fisica
            elif h =='Leitura':
                comando = self.controlador.mostrar_leitura
            elif h =="Meditação":
                comando = self.controlador.mostrar_meditacao
            else: 
                comando = None
            botao = ctk.CTkButton(caixa, text=h, width=240, height=45, corner_radius=8, fg_color=COR_FUNDO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial",18), command=comando)
            botao.pack(pady=6)

    def criar_botoes(self, parent):
        botoes = ["O que é o Burnout?", "Prever se estou em risco de Burnout", "Desenvolver um novo hábito", "Acessar conquistas", "Registro de atividades"]
        for texto in botoes:
            if texto == "O que é o Burnout?":
                comando = self.controlador.mostrar_burnout
            elif texto == "Prever se estou em risco de Burnout":
                comando = self.controlador.mostrar_resultado
            elif texto == 'Desenvolver um novo hábito':
                comando = self.controlador.mostrar_habitos
            elif texto == "Acessar conquistas":
                comando = self.controlador.mostrar_conquistas
            elif texto == "Registro de atividades":
                comando = self.controlador.mostrar_atividades
            else:
                comando = None
            botao = ctk.CTkButton(parent, text=texto, width=430, height=50, corner_radius=5, fg_color=COR_TITULO, hover_color=COR_HOVER, text_color="#FFD7C5", font=("Arial",20,"bold"), command=comando)
            botao.pack(pady=6)

    def criar_conteudo(self):
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.grid(row=0, column=1, sticky="nsew", padx=25, pady=15)
        conteudo.grid_columnconfigure((0,1), weight=1)
        titulo = ctk.CTkLabel(conteudo, text="Sinapse", font=("Arial",40,"bold"), text_color=COR_TITULO)
        titulo.grid(row=0, column=0, columnspan=2, sticky="w")
        subtitulo = ctk.CTkLabel(conteudo, text="Seja bem vindo!", font=("Arial",20), text_color=COR_TEXTO)
        subtitulo.grid(row=1, column=0, columnspan=2, sticky="w")
        pergunta = ctk.CTkLabel(conteudo, text="O que você deseja fazer?", font=("Arial",22,"bold"), text_color=COR_TEXTO)
        pergunta.grid(row=2, column=0, pady=15, sticky="w")
        esquerda = ctk.CTkFrame(conteudo, fg_color="transparent")
        esquerda.grid(row=3, column=0, padx=(0,20), sticky="nw")
        direita = ctk.CTkFrame(conteudo, fg_color="transparent")
        direita.grid(row=3, column=1, padx=(20,0), sticky="nw")
        self.criar_lista_habitos(esquerda)
        self.criar_botoes(direita)
        sair = ctk.CTkButton(conteudo, text="Sair", width=80, height=30, corner_radius=10, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 14, "bold"), command=self.controlador.mostrar_inicial)
        sair.place(relx=0.98, rely=1, anchor="se")
        configuracoes = ctk.CTkButton(conteudo, text="⏣", height=30,width=30, corner_radius=10, fg_color=COR_FUNDO,bg_color=COR_FUNDO,hover_color=COR_CAIXA, text_color=COR_TEXTO, font=("Arial", 40, "bold"), command=self.controlador.mostrar_inicial)
        configuracoes.place(relx=1.0, x=-10, y=10, anchor="ne")  

# ================== CONTROLADOR ==================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sinapse")
        self.geometry("900x550")
        self.resizable(False, False)
        self.tela_atual = None
        self.mostrar_inicial()

    def mostrar_tela(self, tela_classe):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = tela_classe(self, self)
        self.tela_atual.pack(fill="both", expand=True)

    def mostrar_inicial(self):
        self.mostrar_tela(TelaInicial)

    def mostrar_login(self):
        self.mostrar_tela(TelaLogin)

    def mostrar_cadastro(self):
        self.mostrar_tela(TelaCadastro)

    def mostrar_caracterizacao1(self):
        self.mostrar_tela(TelaCaracterizacao1)

    def mostrar_caracterizacao2(self):
        self.mostrar_tela(TelaCaracterizacao2)

    def mostrar_burnout(self):
        self.mostrar_tela(TelaBurnout)

    def mostrar_resultado(self):
        self.mostrar_tela(TelaResultado)
    
    def mostrar_habitos(self):
        self.mostrar_tela(TelaHabitos)
        
    def mostrar_conquistas(self):
        self.mostrar_tela(TelaConquistas)
    
    def mostrar_atividades(self):
        self.mostrar_tela(TelaAtividades)
    
    def mostrar_dormir(self):
        self.mostrar_tela(TelaDormirCedo)
    
    def mostrar_atividade_fisica(self):
        self.mostrar_tela(TelaAtividadeFisica)
    
    def mostrar_leitura(self):
        self.mostrar_tela(TelaLeitura)
    
    def mostrar_meditacao(self):
        self.mostrar_tela(TelaMeditacao)
        
    def mostrar_principal(self):
        self.mostrar_tela(TelaPrincipal)
        
# ================== EXECUÇÃO ==================

if __name__ == "__main__":
    app = App()
    app.iconbitmap("icone.ico")
    app.mainloop()