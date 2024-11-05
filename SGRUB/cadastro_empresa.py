import customtkinter as ctk
import pymysql as pm
class Abrir_Cadastro_Empresa:
    def __init__(self,janela_cadastro_empresa):
        self.banco=pm.connect(
            user="root",
            host="127.0.0.1",
            password="7890_6543",
            database="SGRUB", )
        self.cursor=self.banco.cursor()
        self.janela_cadastro_empresa = janela_cadastro_empresa
        self.janela_cadastro_empresa.geometry("800x500")
        self.janela_cadastro_empresa.title("Cadastro de Empresas")
        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")
        self.texto = ctk.CTkLabel(self.janela_cadastro_empresa,text="Cadastro de Empresas", font=('arial', 40),text_color="#064929" )
        self.texto.pack(pady=20, fill='x')

        self.tela_cadastro_empresa = ctk.CTkFrame(self.janela_cadastro_empresa ,fg_color="#064929", corner_radius=15)
        self.tela_cadastro_empresa.pack(pady=20, padx=20, fill="both", expand=True)

        self.nome = ctk.CTkLabel(self.tela_cadastro_empresa, text="Nome:", text_color="white")
        self.nome.pack(pady=5)
        self.nome = ctk.CTkEntry(self.tela_cadastro_empresa, width=300)
        self.nome.pack(pady=5)

        self.num_cnpj = ctk.CTkLabel(self.tela_cadastro_empresa, text="Numero do cnpj:", text_color="white")
        self.num_cnpj.pack(pady=5)
        self.num_cnpj = ctk.CTkEntry(self.tela_cadastro_empresa, width=300)
        self.num_cnpj.pack(pady=5)

        self.num_cep = ctk.CTkLabel(self.tela_cadastro_empresa, text="Numero do cep:", text_color="white")
        self.num_cep.pack(pady=5)
        self.num_cep = ctk.CTkEntry(self.tela_cadastro_empresa, width=300)
        self.num_cep.pack(pady=5)

        self.confirmar = ctk.CTkButton(self.tela_cadastro_empresa, text="Confirmar", width=10,command=self.adicionar_empresa)
        self.confirmar.pack(padx=20)

    def adicionar_empresa(self):
        nome=self.nome.get()
        num_cnpj=self.num_cnpj.get()
        num_cep=self.num_cep.get()
        if nome and num_cep and num_cnpj:
         self.cursor.execute("INSERT INTO registro_empresa (nome,numero_cep,numero_cnpj) VALUES (%s,%s,%s)",(nome,num_cep,num_cnpj))
         self.banco.commit()
         print("enviado com sucesso")
         self.janela_cadastro_empresa.destroy()
        else:
         print("não enviado")

if __name__=='__main__':
    root=ctk.CTk()
    app=Abrir_Cadastro_Empresa(root)
    root.mainloop()