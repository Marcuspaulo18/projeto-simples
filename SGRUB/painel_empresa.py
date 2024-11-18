import customtkinter as ctk
from tkinter import messagebox
import pymysql as pm


class Abrir_Painel_Empresa:
    def __init__(self, painel_empresa):
        self.painel_empresa = painel_empresa
        self.painel_empresa.geometry("800x600")
        self.painel_empresa.title("Painel de Empresas Interessadas")
        self.painel_empresa.configure(bg="white")

        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")


        self.db = pm.connect(
            user="root",
            host="localhost",
            password="Mpso_7890@",
            database="SGRUB",
            port=3307
        )
        self.cursor = self.db.cursor()

        self.label_titulo = ctk.CTkLabel(self.painel_empresa, text="Painel de Empresas",
                                         text_color="#064929", font=('Arial', 30))
        self.label_titulo.pack(pady=20)

        self.cnpj_frame = ctk.CTkFrame(self.painel_empresa, fg_color="white")
        self.cnpj_frame.pack(pady=10, padx=20, fill="x")


        self.label_cnpj = ctk.CTkLabel(self.cnpj_frame, text="Digite o CNPJ da Empresa:",
                                       text_color="#064929", font=('Arial', 18))
        self.label_cnpj.pack(side="left", padx=10)

        self.input_cnpj = ctk.CTkEntry(self.cnpj_frame, placeholder_text="CNPJ da Empresa", width=250)
        self.input_cnpj.pack(side="left", padx=10)

        # Search button
        self.btn_buscar = ctk.CTkButton(self.cnpj_frame, text="Buscar", command=self.buscar_empresa_por_cnpj,
                                        text_color="white", fg_color="green", font=('Arial', 16), width=100)
        self.btn_buscar.pack(side="left", padx=10)

        self.resultado_frame = ctk.CTkFrame(self.painel_empresa, fg_color="white")
        self.resultado_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_resultado = ctk.CTkLabel(self.resultado_frame, text="", text_color="#064929",
                                            font=('Arial', 16), wraplength=700)
        self.label_resultado.pack(pady=10)

    def buscar_empresa_por_cnpj(self):
        cnpj = self.input_cnpj.get().strip()
        if not cnpj.isdigit():
            messagebox.showwarning("Aviso", "Por favor, insira um CNPJ válido.")
            return

        try:

            query_empresa = """
                SELECT re.ideregistro_empresa, r.nome, r.ideregistro 
                FROM registro_empresa re
                JOIN registro r ON r.ideregistro = re.ideregistro_empresa
                WHERE re.numero_cnpj = %s
            """
            self.cursor.execute(query_empresa, (cnpj,))
            empresa = self.cursor.fetchone()

            if empresa:
                id_empresa, nome_empresa, id_relatorio = empresa
                self.exibir_relatorio(id_relatorio)
            else:
                self.label_resultado.configure(text="Nenhuma empresa encontrada com esse CNPJ.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar a empresa: {e}")

    def exibir_relatorio(self, id_relatorio):
        try:

            query_relatorio = """
            select distinct registro_empresa.nome,categoria,probabilidades,resultado from relatorio join registro_empresa on registro_empresa.ideregistro_empresa=relatorio.iderelatorio where iderelatorio= %s;
            """
            self.cursor.execute(query_relatorio, (id_relatorio,))
            relatorio = self.cursor.fetchone()

            if relatorio:
                nome, categoria, probabilidades, resultado = relatorio
                conteudo = f"Nome da empresa: {nome}\n Categoria: {categoria}\nResultado: {resultado}\nProbabilidades: {probabilidades}"
                self.label_resultado.configure(text=conteudo)
            else:
                self.label_resultado.configure(text="Nenhum relatório associado encontrado.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar o relatório: {e}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Painel_Empresa(root)
    root.mainloop()
