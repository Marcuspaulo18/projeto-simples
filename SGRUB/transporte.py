import customtkinter as ctk

class Abrir_Transporte:
    def __init__(self, janela_transporte):
        self.janela_transporte = janela_transporte
        self.janela_transporte.geometry("800x500")
        self.janela_transporte.title("Painel de Transporte")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Definir interface principal
        self.criar_interface()

    def criar_interface(self):
        # Cabeçalho
        titulo = ctk.CTkLabel(self.janela_transporte, text="SGRUB", font=('Arial', 30), text_color="#064929")
        titulo.pack(pady=10)

        # Frame principal
        self.tela_transporte = ctk.CTkFrame(self.janela_transporte, fg_color="#064929", corner_radius=15)
        self.tela_transporte.pack(pady=20, padx=20, fill="both", expand=True)

        # Campos de entrada e seleção
        text_destinatario = ctk.CTkLabel(self.tela_transporte, text="Digite o CEP do destinatário:", font=('Arial', 14), text_color="white")
        text_destinatario.pack(pady=10)

        self.input_destinatario = ctk.CTkEntry(self.tela_transporte, width=300, placeholder_text="CEP destinatário")
        self.input_destinatario.pack(pady=10)

        text_destinador = ctk.CTkLabel(self.tela_transporte, text="Digite o CEP do destinador:", font=('Arial', 14), text_color="white")
        text_destinador.pack(pady=10)

        self.input_destinado = ctk.CTkEntry(self.tela_transporte, width=300, placeholder_text="CEP destinador")
        self.input_destinado.pack(pady=10)

        # Menu de opções
        self.porte_var = ctk.StringVar(value="Selecione a Empresa")
        porte_menu = ctk.CTkOptionMenu(self.tela_transporte, variable=self.porte_var, values=["EmpresaA", "EmpresaB", "EmpresaC", "EmpresaD"])
        porte_menu.pack(pady=10)

        # Botão de confirmação
        self.confirmar = ctk.CTkButton(self.tela_transporte, text="Confirmar", font=('Arial', 16), fg_color="green", text_color="white", command=self.confirmar_acao)
        self.confirmar.pack(pady=20)

    def confirmar_acao(self):
        # Ação a ser executada ao confirmar (a ser preenchida com a lógica desejada)
        print("Dados confirmados")

if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Transporte(root)
    root.mainloop()
