import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=6)

## Eventos de botones
def Salir(event):
    print('Adios')
    window.quit()

def Reinicio(event): #funcion de reinicio de las variables
    (seleccionado).set("")
    opcion.config(text="")

def seleccionar():
    opcion.config(text="{}".format(seleccionado.get()))

# Lista de RadioButton
seleccionado = tk.StringVar()
r1 = ttk.Radiobutton(window, text='opcion 1', value='opcion 1', variable=seleccionado, command=seleccionar)
r2 = ttk.Radiobutton(window, text='opcion 2', value='opcion 2', variable=seleccionado, command=seleccionar)
r3 = ttk.Radiobutton(window, text='opcion 3', value='opcion 3', variable=seleccionado, command=seleccionar)
r4 = ttk.Radiobutton(window, text='opcion 4', value='opcion 4', variable=seleccionado, command=seleccionar)
r1.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
r2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
r3.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
r4.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)


## Botones ubicado con grid y con pack
boton = tk.Button(window, text='Reinicio')
#boton.pack()
boton.grid(column=1, row=6, sticky=tk.E)
boton.bind('<Button-1>', Reinicio)

botonSalir = tk.Button(window, text='Salir')
#botonSalir.pack()
botonSalir.grid(column=2, row=6 , sticky=tk.W)
botonSalir.bind('<Button-1>', Salir)

opcion = tk.Label(window)
opcion.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
window. mainloop()