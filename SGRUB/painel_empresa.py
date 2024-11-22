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

        try:
            self.db = pm.connect(
                user="root",
                host="localhost",
                password="Mpso_7890@",
                database="SGRUB",
                port=3307
            )
            self.cursor = self.db.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Database connection failed: {e}")


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

        self.btn_buscar = ctk.CTkButton(self.cnpj_frame, text="Buscar", command=self.buscar_empresa_por_cnpj,
                                        text_color="white", fg_color="green", font=('Arial', 16), width=100)
        self.btn_buscar.pack(side="left", padx=10)

        self.resultado_frame = ctk.CTkFrame(self.painel_empresa, fg_color="white")
        self.resultado_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_resultado = ctk.CTkLabel(self.resultado_frame, text="", text_color="#064929",
                                            font=('Arial', 16), wraplength=700)
        self.label_resultado.pack(pady=10)

    def buscar_empresa_por_cnpj(self):
        try:
            cnpj = self.input_cnpj.get()
            if not cnpj:
                messagebox.showwarning("Aviso", "Por favor, insira um CNPJ válido.")
                return

            query_empresa = """
                SELECT ideregistro_empresa, nome
                FROM registro_empresa 
                WHERE numero_cnpj = %s
            """

            self.cursor.execute(query_empresa, (cnpj,))
            empresa = self.cursor.fetchone()


            if empresa:
                id_empresa, nome_empresa = empresa

                self.exibir_relatorio(id_empresa)
            else:
                print("No company found with this CNPJ")
                self.label_resultado.configure(text="Nenhuma empresa encontrada com esse CNPJ.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar a empresa: {e}")

    def exibir_relatorio(self, id_empresa):
        try:
            query_relatorio = """
            SELECT re.nome, r.categoria, r.probabilidades, r.resultado 
            FROM relatorio r
            JOIN registro_empresa re ON re.ideregistro_empresa = r.ideregistro_empresa
            WHERE re.ideregistro_empresa = %s
            """
            self.cursor.execute(query_relatorio, (id_empresa,))
            relatorio = self.cursor.fetchone()
            if relatorio:
                nome, categoria, probabilidades, resultado = relatorio
                conteudo = f"""
Nome da empresa: {nome}
Categoria: {categoria}
Resultado: {resultado}
Probabilidades: {probabilidades}
"""

                self.label_resultado.configure(text=conteudo)
            else:
                print("No report found for this company")
                self.label_resultado.configure(text="Nenhum relatório encontrado para esta empresa.")

        except Exception as e:
            print(f"Error in exibir_relatorio: {e}")
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar o relatório: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Painel_Empresa(root)
    root.mainloop()
