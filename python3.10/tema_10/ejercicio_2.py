

"""
def save_selection():
    saved_list =tkinter.Label(window,text='Esta función aún no ha sido implementada. :(')
    saved_list.pack(padx=5, pady=5)
window = tkinter.Tk()
window.title('Lista de compras')
window.geometry('350x200')

frame = tkinter.LabelFrame(window, text='Falta comprar:')
frame.pack()

selected1 = tkinter.IntVar()
selected2 = tkinter.IntVar()
selected3 = tkinter.IntVar()
selected4 = tkinter.IntVar()

option1 = tkinter.Checkbutton(frame, text='Leche', variable=selected1)
option1.grid(row=0, column=0)

option2 = tkinter.Checkbutton(frame, text='Cereal', variable=selected2)
option2.grid(row=1, column=0)

option3 = tkinter.Checkbutton(frame, text='Aceite', variable=selected3)
option3.grid(row=2, column=0)

option4 = tkinter.Checkbutton(frame, text='Carne', variable=selected4)
option4.grid(row=3, column=0)

save = tkinter.Button(window, text='Guardar seleccion', command=save_selection)
save.pack()

window.mainloop()
"""

from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Pepe", "María", "Ernesto", "Ruben", "Carlos", "Laura", "Ana", "Lorena"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de nombres de personas")
label.pack()
master.mainloop()