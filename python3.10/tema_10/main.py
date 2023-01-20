import sys
import tkinter
from tkinter import ttk
from random import randint

def ventana_1(window):

    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=3)

    ## User
    # Etiqueta user
    user_label = ttk.Label(window, text='username: ')
    user_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    # Campo user
    user_entry = ttk.Entry(window)
    user_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

    ## Password
    # Etiqueta password
    password_label = ttk.Label(window, text='password: ')
    password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

    # Campo password
    password_entry = ttk.Entry(window, show='*')
    password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

    ## Button
    login_button = ttk.Button(window, text='Login')
    login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

def ventana_2(window):
    label1 = ttk.Label(window, text='Posicionamiento absoluto', bg='blue', fg='white')
    label1.place(x=10, y=50)

def ventana_3(window):
    colors = ['blue', 'red', 'yellow','green', 'purple', 'black', 'white']

    for x in range(0,10):
        color1 = randint(0, len(colors)-1)
        color2 = randint(0, len(colors)-1)
        label = tkinter.Label(window, text='etiqueta', bg=colors[color1],fg=colors[color2])
        label.place(x=randint(0,100),y=randint(0,100))

def frame(window):
    frame = ttk.Frame(window, 800, 600, relief='sunken')
    return frame

def main():
    window = tkinter.Tk()
    ventana_3(window)
    
    window.mainloop()
    sys.exit(0)


if __name__== "__main__":
    main()