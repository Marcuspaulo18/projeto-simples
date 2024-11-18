import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading
import queue
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from deep_translator import GoogleTranslator


def import_tf_modules():
    global MobileNetV2, preprocess_input, decode_predictions, image
    from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
    from tensorflow.keras.preprocessing import image


def carregar_categorias_bioplastico(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as file:
            categorias = [linha.strip() for linha in file if linha.strip()]
        return set(categorias)
    except FileNotFoundError:
        print("Arquivo de categorias não encontrado.")
        return set()


class Abrir_Analise:
    def __init__(self, master):
        self.master = master
        self.master.title('Análise de Resíduos')
        self.master.geometry('800x850+250+0')
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.model = None
        self.model_loaded = False
        self.model_queue = queue.Queue()
        self.categorias_bioplastico = carregar_categorias_bioplastico('categorias_bioplastico.txt')

        self.create_widgets()
        self.start_model_loading()

    def create_widgets(self):
        titulo = ctk.CTkLabel(self.master, text="SGRUB", font=('Arial', 30, 'bold'), text_color="#064929")
        titulo.pack(pady=20)

        self.download_button = ctk.CTkButton(self.master, text='Selecione a Imagem', command=self.load_image,
                                             fg_color="green", font=('Arial', 16))
        self.download_button.pack(pady=15)

        self.image_label = ctk.CTkLabel(self.master, text='', fg_color="gray90", width=224, height=224)
        self.image_label.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.master, text='Resultados:', font=('Arial', 20, 'bold'), text_color="black")
        self.result_label.pack(pady=(20, 10))


        self.analysis_label = ctk.CTkLabel(self.master, text="", font=('Arial', 14), fg_color="white", text_color="black",
                                           width=400, height=100, anchor="center")
        self.analysis_label.pack(pady=(0, 20))


        self.bioplastic_validation_label = ctk.CTkLabel(self.master, text="", font=('Arial', 14), fg_color="black", text_color="blue")
        self.bioplastic_validation_label.pack(pady=(10, 20))

        self.graph_frame = ctk.CTkFrame(self.master, fg_color="white", width=600, height=300)
        self.graph_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Botão de retorno
        self.return_button = ctk.CTkButton(self.master, text="Retorno", command=self.master.quit, fg_color="red",
                                           font=('Arial', 16), width=120)
        self.return_button.pack(pady=10)

    def start_model_loading(self):
        threading.Thread(target=self.load_model, daemon=True).start()
        self.master.after(100, self.check_model_loaded)

    def load_model(self):
        import_tf_modules()
        print("Carregando modelo TensorFlow...")
        model = MobileNetV2(weights='imagenet')
        self.model_queue.put(model)
        print("Modelo carregado com sucesso!")

    def check_model_loaded(self):
        try:
            self.model = self.model_queue.get_nowait()
            self.model_loaded = True
            print("Modelo pronto para uso.")
        except queue.Empty:
            self.master.after(100, self.check_model_loaded)

    def load_image(self):
        if not self.model_loaded:
            messagebox.showinfo("Aguarde", "O modelo ainda está carregando. Por favor, espere 20 segundos.")
            return

        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        try:
            img = Image.open(file_path)
            img = img.resize((224, 224))
            img_tk = ImageTk.PhotoImage(img)

            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

            self.process_image(img)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")

    def process_image(self, img):
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        preds = self.model.predict(img_array)
        top_preds = decode_predictions(preds, top=3)[0]

        self.display_results(top_preds)

    def display_results(self, top_preds):
        translator = GoogleTranslator(source="en", target="pt")

        categories = [pred[1] for pred in top_preds]
        probabilities = [pred[2] * 100 for pred in top_preds]

        results_text = f"Categoria Predita:\n{top_preds[0][1]} ({top_preds[0][2] * 100:.2f}%)"

        try:
            translated_results = translator.translate(results_text)
        except Exception as e:
            print(f"Erro durante a tradução: {e}")
            translated_results = "Falha na tradução."

        self.result_label.configure(text=translated_results)

        top_analyses_text = "\n".join([f"{pred[1]}: {pred[2] * 100:.2f}%" for pred in top_preds])
        self.analysis_label.configure(text=top_analyses_text)

        self.generate_graph(categories, probabilities)

        if self.is_suitable_for_bioplastic(top_preds):
            self.bioplastic_validation_label.configure(text="O resíduo é adequado para produção de bioplástico.", text_color="green")
        else:
            self.bioplastic_validation_label.configure(text="O resíduo não é adequado para produção de bioplástico.", text_color="red")

        self.analise = {
            'imagem': 'Imagem carregada',
            'resultado': translated_results,
            'categorias': categories,
            'probabilidades': probabilities
        }
        if hasattr(self, 'on_analysis_complete'):
            self.on_analysis_complete(self.analise)

    def is_suitable_for_bioplastic(self, predictions, prob_minima=60):
        for pred in predictions:
            categoria, probabilidade = pred[1], pred[2] * 100
            if categoria in self.categorias_bioplastico or probabilidade >= prob_minima:
                return True
        return False

    def generate_graph(self, categories, probabilities):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.barh(categories, probabilities, color='limegreen')
        ax.set_xlabel('Probabilidade (%)')
        ax.set_title('Categorias Preditas')
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    root = ctk.CTk()
    app = Abrir_Analise(root)
    root.mainloop()
