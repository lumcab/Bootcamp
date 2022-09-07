from tkinter.tix import Form

from tkinter import *


def motion(event):
    print ("Mouse position : (%s %s) " % (event.x, event.y))
    return

master = Tk()
texto= "Demo de texto en un widget msg para ver el noviniento del raton"
msg = Message (master, text=texto)
msg.config (bg= 'Lightgreen', font= ('times ', 24, 'italic' ))
msg.bind ('<Motion>',motion)
msg.pack()
mainloop ()