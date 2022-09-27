from cProfile import label
from tkinter import *
janela=Tk()
janela.title("Coins Multiplier")
texto_title= Label(janela, text="Coins Multiplier")
texto_title.grid(column=0,row=1)

button= Button(janela, text="Start")

janela.mainloop()