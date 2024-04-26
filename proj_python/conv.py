from tkinter import *

janela=Tk()
janela.geometry("420x420")
janela.title("conversor de medidas")
def cenm():
 medcm=inp.get()
 rescm.config(text=(float(medcm)/100))

def mcen():
 medmc=inp.get()
 resmc.config(text=(float(medmc)*100))

inp=Entry(bg="black",fg="white",borderwidth=6)
inp.pack()
butcf=Button(bg="white",fg="black",borderwidth=6,text="centimetro->metro",command=cenm)
butcf.pack()
butfc=Button(bg="white",fg="black",borderwidth=6,text="metro->centimetro",command=mcen)
butfc.pack()
rescm=Label(janela,text="",borderwidth=6)
rescm.pack()
resmc=Label(janela,text="",borderwidth=6)
resmc.pack()
janela.config(bg="gray")
janela.mainloop()