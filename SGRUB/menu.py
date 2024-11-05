import customtkinter as ctk
from tkinter import messagebox
from login import Abrir_Login
from cadastro import Abrir_Cadastro
from cadastro_empresa import Abrir_Cadastro_Empresa
from painel_empresa import Abrir_Painel_Empresa
from relatorio import Abrir_Relatorio
from transporte import Abrir_Transporte
from analise import Abrir_Analise


class SGRUBMain:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x800")
        self.master.title("Menu principal SGRUB")

        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")

        self.criar_pagina()

    def criar_pagina(self):
        self.texto = ctk.CTkLabel(self.master, text="SGRUB", font=('Arial', 40), text_color="#064929")
        self.texto.pack(pady=20, fill='x')

        self.menu_frame = ctk.CTkFrame(self.master, fg_color="#064929", corner_radius=15)
        self.menu_frame.pack(pady=10, padx=20, fill="both", expand=True,anchor="center")

        buttons = [
            ("Análise de resíduos", self.abrir_analise_residuos),
            ("Login", self.abrir_login),
            ("Cadastro", self.abrir_cadastro),
            ("Cadastro de empresas", self.abrir_cadastro_empresa),
            ("Painel de empresas", self.abrir_painel_empresa),
            ("Painel de transporte", self.abrir_transporte),
            ("Relatório", self.abrir_relatorio),
            ("Encerrar", self.master.quit)
        ]

        for text, command in buttons:
            button = ctk.CTkButton(self.menu_frame, text=text, font=('Arial', 20), command=command, width=300)
            button.pack(pady=10,padx=20)

    def salvar_analise(self, analise):
        self.analise = analise  # Armazena a análise para depois abrir no relatório

    def abrir_analise_residuos(self):
        analise_tela = ctk.CTkToplevel(self.master)
        analise_app = Abrir_Analise(analise_tela)
        analise_app.on_analysis_complete = self.salvar_analise

    def abrir_relatorio(self):
        if self.analise:
            relatorio_tela = ctk.CTkToplevel(self.master)
            Abrir_Relatorio(relatorio_tela, self.analise)  # Passa a análise para a nova janela
        else:
            messagebox.showwarning("Aviso", "Nenhuma análise disponível para gerar o relatório.")

    def abrir_login(self):
        login_tela = ctk.CTkToplevel(self.master)
        Abrir_Login(login_tela)

    def abrir_cadastro(self):
        cadastro_tela = ctk.CTkToplevel(self.master)
        Abrir_Cadastro(cadastro_tela)

    def abrir_cadastro_empresa(self):
        cadastro_empresa_tela = ctk.CTkToplevel(self.master)
        Abrir_Cadastro_Empresa(cadastro_empresa_tela)

    def abrir_painel_empresa(self):
        painel_empresa_tela = ctk.CTkToplevel(self.master)
        Abrir_Painel_Empresa(painel_empresa_tela)

    def abrir_transporte(self):
        painel_transporte_tela = ctk.CTkToplevel(self.master)
        Abrir_Transporte(painel_transporte_tela)


def main():
    root = ctk.CTk()
    app = SGRUBMain(root)
    root.mainloop()


if __name__ == "__main__":
    main()
