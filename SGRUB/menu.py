
import customtkinter as ctk
from tkinter import messagebox,PhotoImage
from login import Abrir_Login
from cadastro import Abrir_Cadastro
from cadastro_empresa import Abrir_Cadastro_Empresa
from painel_empresa import Abrir_Painel_Empresa
from relatorio import Abrir_Relatorio
from analise import Abrir_Analise
import pymysql as pm
from PIL import Image, ImageTk
class SGRUBMain:
    def __init__(self, master):
        self.db=pm.connect(
            user="root",
            host="localhost",
            password="Mpso_7890@",
            database="SGRUB",
            port=3307
        )
        self.master = master
        self.master.geometry("800x800")
        self.master.title("Menu principal SGRUB")
        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")
        self.usuario_verificado=False
        self.analise=None

        self.criar_pagina()

    def criar_pagina(self):
        self.texto = ctk.CTkLabel(self.master, text="SGRUB", font=('Arial', 40), text_color="#064929")
        self.texto.pack(pady=20, fill='x')
        self.imagem_icone = ctk.CTkImage(Image.open("icone.jpg"), size=(100, 100))
        self.campo_usuario = ctk.CTkLabel(self.master, image=self.imagem_icone,text="")
        self.campo_usuario.pack(pady=10)


        self.texto_usuario = ctk.CTkLabel(self.master, font=('Arial', 40), text_color="#064929",text=f"Bem Vindo Usuario")
        self.texto_usuario.pack(pady=20, fill='x')
        self.menu_frame = ctk.CTkFrame(self.master, fg_color="#064929", corner_radius=15)
        self.menu_frame.pack(pady=10, padx=20, fill="both", expand=True,anchor="center")

        buttons = [
            ("Análise de resíduos", self.abrir_analise_residuos),
            ("Login", self.abrir_login),
            ("Cadastro", self.abrir_cadastro),
            ("Cadastro de empresas", self.abrir_cadastro_empresa),
            ("Painel de empresas", self.abrir_painel_empresa),
            ("Relatório", self.abrir_relatorio),
            ("Encerrar", self.master.quit)
        ]

        for text, command in buttons:
            button = ctk.CTkButton(self.menu_frame, text=text, font=('Arial', 20), command=command, width=300)
            button.pack(pady=10,padx=20)




    def verificador_acesso(self):
       self.usuario_verificado=True
       messagebox.showinfo(title="acesso confirmado" ,message="bem vindo")

    def salvar_analise(self, analise):
        self.analise = analise

    def abrir_analise_residuos(self):
     if self.usuario_verificado:
        analise_tela = ctk.CTkToplevel(self.master)
        analise_app = Abrir_Analise(analise_tela)
        analise_app.on_analysis_complete = self.salvar_analise
     else:
         messagebox.showwarning(title="alerta de segurança" ,message="por favor realize o login antes de poder acessar")
    def abrir_relatorio(self):
     if self.usuario_verificado:
        if self.analise:
            relatorio_tela = ctk.CTkToplevel(self.master)
            Abrir_Relatorio(relatorio_tela, self.analise)
        else:
            messagebox.showwarning("Aviso", "Nenhuma análise disponível para gerar o relatório.")
     else:
         messagebox.showwarning(title="alerta de segurança", message="por favor realize o login antes de poder acessar")
    def abrir_login(self):
        login_tela = ctk.CTkToplevel(self.master)
        Abrir_Login(login_tela,verificado=self.verificador_acesso)

    def abrir_cadastro(self):
        cadastro_tela = ctk.CTkToplevel(self.master)
        Abrir_Cadastro(cadastro_tela)

    def abrir_cadastro_empresa(self):
     if self.usuario_verificado:
        cadastro_empresa_tela = ctk.CTkToplevel(self.master)
        Abrir_Cadastro_Empresa(cadastro_empresa_tela)
     else:
         messagebox.showwarning(title="alerta de segurança", message="por favor realize o login antes de poder acessar")
    def abrir_painel_empresa(self):
     if self.usuario_verificado:
        painel_empresa_tela = ctk.CTkToplevel(self.master)
        Abrir_Painel_Empresa(painel_empresa_tela)
     else:
         messagebox.showwarning(title="alerta de segurança", message="por favor realize o login antes de poder acessar")



def main():
    root = ctk.CTk()
    app = SGRUBMain(root)
    root.mainloop()


if __name__ == "__main__":
    main()
