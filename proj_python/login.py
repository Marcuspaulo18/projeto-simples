from tkinter import *

janela=Tk()
janela.title("www.nemoenterprise.com.br")
janela.geometry("500x500")
def confirmar():
 log=login.get()
 
 sen=senha.get()
 if len(sen)>6:
  bv2.config(text="por favor digite uma senha dentro de 6 caracteres")
 else:
  bv2.config(text="senha:"+sen)
 if "@" in log:
  bv1.config(text="login:"+log)
 else:
  bv1.config(text="por favor no email adicione um @")
login=Entry(bg="white",fg="black",borderwidth=6,font=("arial",12))
login.pack()
senha=Entry(bg="white",fg="black",borderwidth=6,font=("arial",12))
senha.pack()
conf=Button(command=confirmar,text="confirmar",bg="black",fg="white",font=("arial",12))
conf.pack()
bv2=Label(text="")
bv2.pack()
bv1=Label(text="")
bv1.pack()
janela.config(bg="gray")
janela.mainloop()