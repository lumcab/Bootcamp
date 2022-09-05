import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

##Usuario
#Etiqueta Usuario
username_label = ttk.Label(window, text='Username:')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

#Campo Usuario
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

##Password
#Etiqueta Password
password_label = ttk.Label(window, text='Password:')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

#Campo Password
password_entry = ttk.Entry(window)
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

##Button
#Cancel Button
cancel_button = ttk.Button(window, text='Cancel')
cancel_button.grid(column=1, row=3, sticky=tkinter.W, padx=5, pady=5)

#Login Button
login_button = ttk.Button(window, text='Login')
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()