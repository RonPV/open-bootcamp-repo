import tkinter
from tkinter import ttk

def reiniciar():
    seleccionado.set(None)


window = tkinter.Tk()
window.title('Elige')


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

seleccionado = tkinter.IntVar()

boton1 = tkinter.Radiobutton(window, value=1, text='opcion 1', variable=seleccionado)
boton1.grid(row=0, column=0, padx=5, pady=5)

boton2 = tkinter.Radiobutton(window, value=2, text='opcion 2', variable=seleccionado)
boton2.grid(row=1, column=0, padx=5, pady=5)

boton_reiniciar = tkinter.Button(window, text='Reiniciar', command=reiniciar)
boton_reiniciar.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()