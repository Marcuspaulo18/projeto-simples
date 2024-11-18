import customtkinter as ctk
import pymysql as pm
from tkinter import messagebox
class Abrir_Login:
    def __init__(self, janela_login,verificado=None):
        self.banco = pm.connect(
            user="root",
            host="localhost",
            password="Mpso_7890@",
            database="SGRUB",
            port=3307)
        self.cursor = self.banco.cursor()
        self.janela_login = janela_login
        self.janela_login.geometry("800x500")
        self.janela_login.title("Login")
        self.verificado=verificado
        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")

        self.texto = ctk.CTkLabel(self.janela_login, text="SGRUB", font=('Arial', 40),text_color="#064929")
        self.texto.pack(pady=20, fill='x')

        self.tela_login = ctk.CTkFrame(self.janela_login, fg_color="#064929", corner_radius=15)
        self.tela_login.pack(pady=20, padx=20, fill="both", expand=True)

        self.nome = ctk.CTkLabel(self.tela_login, text="Nome:",text_color="white")
        self.nome.pack(pady=5)
        self.nome = ctk.CTkEntry(self.tela_login, width=300, placeholder_text="Digite seu nome")
        self.nome.pack(pady=5)

        self.email = ctk.CTkLabel(self.tela_login, text="Email:",text_color="white")
        self.email.pack(pady=5)
        self.email = ctk.CTkEntry(self.tela_login, width=300, placeholder_text="Digite seu email")
        self.email.pack(pady=5)

        self.senha = ctk.CTkLabel(self.tela_login, text="Senha:",text_color="white")
        self.senha.pack(pady=5)
        self.senha = ctk.CTkEntry(self.tela_login, width=300, show="*", placeholder_text="Digite sua senha")
        self.senha.pack(pady=5)

        self.confirmar = ctk.CTkButton(self.tela_login, text="Confirmar", command=self.verificar_registro)
        self.confirmar.pack(pady=20)

    def verificar_registro(self):
        nome=self.nome.get()
        senha=self.senha.get()
        email=self.email.get()
        self.cursor.execute("select * from registro where nome=%s and senha=%s and email=%s",(nome,senha,email))
        usuarios = self.cursor.fetchone()


        if usuarios:
            messagebox.showinfo(title="confirmação de login",message="acesso valido")
            self.verificado()
            self.janela_login.destroy()
        else:
            messagebox.showerror(title="erro de login",message="acesso invalido")

if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Login(root)
    root.mainloop()
