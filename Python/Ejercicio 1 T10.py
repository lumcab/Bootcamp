import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=4)

## Eventos de botones
def Salir(event):
    print('Adios')
    window.quit()

def Reinicio(event): #funcion de reinicio de las variables
    (seleccionado).set("")

# Lista de RadioButton
seleccionado = tk.StringVar()
r1 = ttk.Radiobutton(window, text='opcion 1', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='opcion 2', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='opcion 3', value='3', variable=seleccionado)
r4 = ttk.Radiobutton(window, text='opcion 3', value='4', variable=seleccionado)
r1.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
r2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
r3.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
r4.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)


## Botones ubicado con grid y con pack
boton = tk.Button(window, text='Reinicio')
#boton.pack()
boton.grid(column=1, row=4, sticky=tk.E)
boton.bind('<Button-1>', Reinicio)

botonSalir = tk.Button(window, text='Salir')
#botonSalir.pack()
botonSalir.grid(column=2, row=4, sticky=tk.W)
botonSalir.bind('<Button-1>', Salir)

window. mainloop()