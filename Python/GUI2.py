import random
import tkinter

window = tkinter.Tk()

colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black', 'orange', 'pink', 'brown', 'violet']

for x in range(0, 200):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = tkinter.Label(window, text='#####', bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0, 200), y=random.randint(0, 200))

window.mainloop()
