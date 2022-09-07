import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=4)

## Lista selecionable
lista = ['Windows','macOS','Linux','MS DOS', 'AmigaOS', 'manjaro', 'BeOS', 'OS/2']
list_items = tk.StringVar(value=lista)
listbox = tk.Listbox(window, height=10, listvariable=list_items)
listbox.grid(column=0, row=0, sticky=tk.W)


### Radio Button
seleccionado = tk.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='Quiza', value='3', variable=seleccionado)
r1.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)
r2.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)
r3.grid(column=2, row=3, sticky=tk.W, padx=5, pady=5)

### Check
def acepto():
    print('Acepto las condiciones')
Seleccion = tk.StringVar()
checkBoxAcepto = ttk.Checkbutton(window, text='acepto las condiciones', variable=Seleccion, command=acepto)
checkBoxAcepto.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

## Eventos de botones
def Salir(event):
    print('Adios')
    window.quit()

def saludarCLick(event):
    print('Han hecho cLick en saludar')


def saludarDobLeCLick(event):
    print('Han hecho DOBLE cLick en saludar')

## Botones ubicado con grid y con pack
boton = tk.Button(window, text='Haz click')
#boton.pack()
boton.grid(column=2, row=4, sticky=tk.E)
boton.bind('<Button-1>', saludarCLick)
boton. bind('<Double-1>', saludarDobLeCLick)

botonSalir = tk.Button(window, text='Salir')
#botonSalir.pack()
botonSalir.grid(column=1, row=4, sticky=tk.W)
botonSalir.bind('<Button-1>', Salir)

window. mainloop()
