import customtkinter as ctk
from tkinter import scrolledtext, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Abrir_Relatorio:
    def __init__(self, relatorio_janela, analise):
        self.analise = analise  # Armazenar a análise passada
        self.relatorio_janela = relatorio_janela
        self.relatorio_janela.title("Relatório de Análises")
        self.relatorio_janela.geometry("700x700+300+100")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.criar_interface()

    def criar_interface(self):
        self.tela_relatorio = ctk.CTkFrame(self.relatorio_janela, fg_color="#064929", corner_radius=15)
        self.tela_relatorio.pack(pady=20, padx=20, fill="both", expand=True)

        titulo = ctk.CTkLabel(self.tela_relatorio, text="SGRUB", font=('Arial', 30), text_color="lime")
        titulo.pack(pady=10)

        titulo_pag = ctk.CTkLabel(self.tela_relatorio, text="Relatório de Análises de Resíduos", font=('Arial', 20), text_color="white")
        titulo_pag.pack(pady=10)

        texto_relatorio = scrolledtext.ScrolledText(self.tela_relatorio, width=70, height=10, font=('Arial', 12), wrap='word')
        texto_relatorio.pack(padx=10, pady=10)

        conteudo = f"Imagem: {self.analise['imagem']}\nResultado: {self.analise['resultado']}\nCategorias:\n"
        for categoria, probabilidade in zip(self.analise['categorias'], self.analise['probabilidades']):
            conteudo += f"- {categoria}: {probabilidade:.2f}%\n"
        texto_relatorio.insert(ctk.END, conteudo)

        label_empresa = ctk.CTkLabel(self.tela_relatorio, text="Registrar Empresa Destinada:", font=('Arial', 12), text_color="white")
        label_empresa.pack(pady=5)

        self.entrada_empresa = ctk.CTkEntry(self.tela_relatorio, width=300, placeholder_text="Digite o nome da empresa")
        self.entrada_empresa.pack(pady=5)

        botao_salvar = ctk.CTkButton(self.tela_relatorio, text="Salvar no Relatório", command=self.salvar_empresa)
        botao_salvar.pack(pady=10)

        grafico_frame = ctk.CTkFrame(self.tela_relatorio)
        grafico_frame.pack(pady=10)

        self.exibir_grafico(self.analise['categorias'], self.analise['probabilidades'], grafico_frame)

    def salvar_empresa(self):
        empresa_destinada = self.entrada_empresa.get()
        if empresa_destinada:
            self.enviar_para_relatorio(self.analise, empresa_destinada)
            messagebox.showinfo("Sucesso", "Análise enviada para o relatório com a empresa registrada!")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira o nome da empresa.")

    def enviar_para_relatorio(self, analise, empresa_destinada):
        try:
            with open('relatorio.txt', 'a') as arquivo:
                arquivo.write("Resultado da Análise:\n")
                arquivo.write(f"Imagem: {analise['imagem']}\n")
                arquivo.write(f"Resultado: {analise['resultado']}\n")
                arquivo.write("Categorias e Probabilidades:\n")
                for categoria, probabilidade in zip(analise['categorias'], analise['probabilidades']):
                    arquivo.write(f"- {categoria}: {probabilidade:.2f}%\n")
                arquivo.write(f"Empresa Destinada: {empresa_destinada}\n")
                arquivo.write("\n-------------------------\n")
            print("Análise enviada para o relatório com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar relatório: {e}")

    def exibir_grafico(self, categorias, probabilidades, grafico_frame):
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(categorias, probabilidades, color='limegreen')
        ax.set_xlabel('Probabilidade (%)')
        ax.set_title('Categorias Preditas')

        for widget in grafico_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()


