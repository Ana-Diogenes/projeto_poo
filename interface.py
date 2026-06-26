'''import customtkinter as ctk

# -------------------- CORES --------------------

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_BOTAO = "#E59B90"
COR_BOTAO_HOVER = "#D9867C"
COR_TEXTO_BOTAO = "#FFF2C9"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# -------------------- TELA INICIAL --------------------

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO)
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
        entrar = ctk.CTkButton(frame_botoes, text="Entrar na conta", width=200, height=70, corner_radius=22, fg_color=COR_BOTAO, hover_color=COR_BOTAO_HOVER, text_color=COR_TEXTO_BOTAO, font=("Arial", 22, "bold"), command=self.entrar)
        entrar.grid(row=0, column=0, padx=18)
        criar = ctk.CTkButton(frame_botoes, text="Criar Conta", width=200, height=70, corner_radius=22, fg_color=COR_BOTAO, hover_color=COR_BOTAO_HOVER, text_color=COR_TEXTO_BOTAO, font=("Arial", 22, "bold"), command=self.criar_conta)
        criar.grid(row=0, column=1, padx=18)
        assinatura = ctk.CTkLabel(conteudo, text="☆ Ana-Diogenes", font=("Arial", 18), text_color=COR_TITULO)
        assinatura.place(relx=0.98, rely=0.97, anchor="se")

    def entrar(self):
        print("Entrar")

    def criar_conta(self):
        print("Criar Conta")

# -------------------- APP --------------------

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sinapse")
        self.geometry("900x550")
        self.resizable(False, False)
        tela = TelaInicial(self)
        tela.pack(fill="both", expand=True)

# -------------------- EXECUÇÃO --------------------

if __name__ == "__main__":
    app = App()
    app.mainloop()'''

'''import customtkinter as ctk

# ================== CONFIGURAÇÕES ==================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_CAMPO = "#E59B90"
COR_HOVER = "#D9867C"
COR_TEXTO = "#8B5C5C"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

# ===================================================

class TelaCaracterizacao(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO)
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

        avancar = ctk.CTkButton(conteudo, text="➤", width=30, height=30, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.proxima_pagina)
        avancar.place(relx=0.98, rely=0.97, anchor="se")

    def proxima_pagina(self):
        print("Próxima página")

# ===================================================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sinapse")
        self.geometry("900x550")
        self.resizable(False, False)
        TelaCaracterizacao(self).pack(fill="both", expand=True)

# ===================================================

if __name__ == "__main__":
    app = App()
    app.mainloop()'''
    
'''import customtkinter as ctk

# ================== CORES ==================

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_CAMPO = "#E59B90"
COR_HOVER = "#D9867C"
COR_TEXTO = "#8B5C5C"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

class TelaCaracterizacao2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO)
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
        avancar = ctk.CTkButton(conteudo, text="➤", width=30, height=30, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.proxima_pagina)
        avancar.place(relx=0.98, rely=0.97, anchor="se")

    def proxima_pagina(self):
        print("Próxima página")

# ====================== TESTE ======================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x550")
        self.title("Sinapse")
        self.resizable(False, False)
        TelaCaracterizacao2(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()'''
    
'''import customtkinter as ctk

# ================== CORES ==================

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_CAMPO = "#E59B90"
COR_HOVER = "#D9867C"
COR_TEXTO = "#8B5C5C"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO)
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
        avancar = ctk.CTkButton(conteudo, text="➤", width=65, height=65, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.proxima_pagina)
        avancar.place(relx=1, rely=1, anchor="se", x=-10, y=-5)

    def proxima_pagina(self):
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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x550")
        self.title("Sinapse")
        self.resizable(False, False)
        TelaCadastro(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()'''
    
'''import customtkinter as ctk

# ================== CORES ==================

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_CAMPO = "#E59B90"
COR_HOVER = "#D9867C"
COR_TEXTO = "#8B5C5C"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO)
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
        avancar = ctk.CTkButton(conteudo, text="➤", width=65, height=65, corner_radius=35, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial", 28, "bold"), command=self.proxima_pagina)
        avancar.place(relx=1, rely=1, anchor="se", x=-10, y=-5)

    def proxima_pagina(self):
        print("Nome:", self.nome.get())
        print("Senha:", self.senha.get())

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x550")
        self.title("Sinapse")
        self.resizable(False, False)
        TelaCadastro(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()'''
    
'''import customtkinter as ctk

# ================== CORES ==================

COR_FUNDO = "#F7E9B3"
COR_TITULO = "#8B5C5C"
COR_CAMPO = "#E59B90"
COR_HOVER = "#D9867C"
COR_TEXTO = "#8B5C5C"

PALETA = ["#8B5C5C", "#E7A49A", "#FAC1A7", "#FFE1B0", "#FFF2B7"]

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COR_FUNDO)
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
        caixa = ctk.CTkFrame(parent, width=310, height=350, fg_color="#FAC1A7", corner_radius=5)
        caixa.pack(pady=0, padx=10)
        caixa.pack_propagate(False)
        titulo = ctk.CTkLabel(caixa, text="Meus hábitos", font=("Arial",22), text_color=COR_TEXTO)
        titulo.pack(anchor="w", padx=40, pady=(15,10))
        habitos = ["Dormir cedo", "Atividade física", "Leitura", "Meditação"]
        for h in habitos:
            botao = ctk.CTkButton(caixa, text=h, width=240, height=45, corner_radius=8, fg_color=COR_CAMPO, hover_color=COR_HOVER, text_color=COR_TEXTO, font=("Arial",18))
            botao.pack(pady=6)

    def criar_botoes(self, parent):
        botoes = ["O que é o Burnout?", "Prever se estou em risco de Burnout", "Desenvolver um novo hábito", "Acessar conquistas", "Registro de atividades"]
        for texto in botoes:
            botao = ctk.CTkButton(parent, text=texto, width=430, height=50, corner_radius=5, fg_color=COR_TITULO, hover_color=COR_HOVER, text_color="#FFD7C5", font=("Arial",20,"bold"))
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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x550")
        self.title("Sinapse")
        self.resizable(False,False)
        TelaInicial(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()'''