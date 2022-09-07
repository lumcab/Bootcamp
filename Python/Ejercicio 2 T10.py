import tkinter as tk

ventana  = tk.Tk()

#label de la ventana
label = tk.Label(text="Distribuciones Linux base Arch")
label.pack()

#lista de elementos
lista = ['Manjaro','Arco','Artix','Parabola', 'Antergos', 'EndeavourOs', 'kaOs', 'Chakra', 'Garuda']
list_items = tk.StringVar(value=lista)
list = tk.Listbox(ventana, height=10, listvariable=list_items)
list.pack()

ventana.mainloop()
