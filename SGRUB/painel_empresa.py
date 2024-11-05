import customtkinter as ctk
from tkinter import messagebox


class Abrir_Painel_Empresa:
    def __init__(self, painel_empresa):
        # Dados das empresas cadastradas com CNPJ e relatório
        self.empresas_cadastradas = [
            {"cnpj": "12345678000100", "nome": "Empresa A", "endereco": "Rua A, 123",
             "relatorio": "Relatório de Empresa A"},
            {"cnpj": "23456789000111", "nome": "Empresa B", "endereco": "Rua B, 456",
             "relatorio": "Relatório de Empresa B"},
            {"cnpj": "34567890000122", "nome": "Empresa C", "endereco": "Rua C, 789",
             "relatorio": "Relatório de Empresa C"}
        ]

        # Configurações da janela principal
        self.painel_empresa = painel_empresa
        self.painel_empresa.geometry("800x600")
        self.painel_empresa.title("Painel de Empresas Interessadas")
        self.painel_empresa.configure(bg="white")

        # Estilo do painel
        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")

        # Título do painel
        self.label_titulo = ctk.CTkLabel(self.painel_empresa, text="Painel de Empresas",
                                         text_color="#064929", font=('Arial', 30))
        self.label_titulo.pack(pady=20)

        # Frame de entrada do CNPJ
        self.cnpj_frame = ctk.CTkFrame(self.painel_empresa, fg_color="white")
        self.cnpj_frame.pack(pady=10, padx=20, fill="x")

        # Label e campo de entrada de CNPJ
        self.label_cnpj = ctk.CTkLabel(self.cnpj_frame, text="Digite o CNPJ da Empresa:",
                                       text_color="#064929", font=('Arial', 18))
        self.label_cnpj.pack(side="left", padx=10)

        self.input_cnpj = ctk.CTkEntry(self.cnpj_frame, placeholder_text="CNPJ", width=250)
        self.input_cnpj.pack(side="left", padx=10)

        # Botão de busca
        self.btn_buscar = ctk.CTkButton(self.cnpj_frame, text="Buscar", command=self.buscar_empresa,
                                        text_color="white", fg_color="green", font=('Arial', 16), width=100)
        self.btn_buscar.pack(side="left", padx=10)

        # Área de resultado da busca
        self.resultado_frame = ctk.CTkFrame(self.painel_empresa, fg_color="white")
        self.resultado_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_resultado = ctk.CTkLabel(self.resultado_frame, text="", text_color="#064929",
                                            font=('Arial', 16), wraplength=700)
        self.label_resultado.pack(pady=10)

    def buscar_empresa(self):
        cnpj = self.input_cnpj.get().strip()

        # Procura a empresa pelo CNPJ
        empresa = next((empresa for empresa in self.empresas_cadastradas if empresa["cnpj"] == cnpj), None)

        # Exibe os resultados ou uma mensagem de erro
        if empresa:
            detalhes = f"Nome: {empresa['nome']}\nEndereço: {empresa['endereco']}\nRelatório: {empresa['relatorio']}"
            self.label_resultado.configure(text=detalhes)
        else:
            messagebox.showwarning("Empresa não encontrada", "Nenhuma empresa encontrada com o CNPJ fornecido.")
            self.label_resultado.configure(text="")


if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Painel_Empresa(root)
    root.mainloop()
