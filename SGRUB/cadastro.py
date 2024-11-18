import customtkinter as ctk
import pymysql as pm
from tkinter import messagebox

class Abrir_Cadastro:
    def __init__(self, janela_cadastro):
        self.banco = pm.connect(
            user="root",
            host="localhost",
            password="Mpso_7890@",
            database="SGRUB",
            port=3307
        )
        self.cursor = self.banco.cursor()
        self.janela_cadastro = janela_cadastro
        self.janela_cadastro.geometry("800x500")
        self.janela_cadastro.title("Cadastro")

        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")

        self.texto = ctk.CTkLabel(self.janela_cadastro, text="SGRUB", font=('arial', 40), text_color="#064929")
        self.texto.pack(pady=10, fill="x")

        self.tela_cadastro = ctk.CTkFrame(self.janela_cadastro, corner_radius=15, fg_color="#064929")
        self.tela_cadastro.pack(pady=10, padx=10, expand=True, fill="both")

        self.nome_label = ctk.CTkLabel(self.tela_cadastro, text="Nome:", text_color="white")
        self.nome_label.pack(pady=5)
        self.nome = ctk.CTkEntry(self.tela_cadastro, width=300, placeholder_text="Digite seu nome")
        self.nome.pack(pady=5)

        self.email_label = ctk.CTkLabel(self.tela_cadastro, text="Email:", text_color="white")
        self.email_label.pack(pady=5)
        self.email = ctk.CTkEntry(self.tela_cadastro, width=300, placeholder_text="Digite seu email")
        self.email.pack(pady=5)

        self.senha_label = ctk.CTkLabel(self.tela_cadastro, text="Senha:", text_color="white")
        self.senha_label.pack(pady=5)
        self.senha = ctk.CTkEntry(self.tela_cadastro, width=300, show="*", placeholder_text="Digite sua senha")
        self.senha.pack(pady=5)

        self.confirmar = ctk.CTkButton(self.tela_cadastro, text="Confirmar", command=self.adicionar_registro)
        self.confirmar.pack(pady=20)

    def adicionar_registro(self):

        nome = self.nome.get()
        email = self.email.get()
        senha = self.senha.get()

        if nome and email and senha:
            try:

                self.cursor.execute("INSERT INTO registro (nome, email, senha) VALUES (%s, %s, %s)",
                                    (nome, email, senha))
                self.banco.commit()
                messagebox.showinfo("Registro inserido com sucesso!")
                self.janela_cadastro.destroy()
            except pm.MySQLError as e:
                messagebox.showerror("Erro ao inserir registro:", e)
        else:
            messagebox.showwarning(message="Por favor, preencha todos os campos.")


if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Cadastro(root)
    root.mainloop()
