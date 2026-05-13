from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))

root = Tk()
label = Label(root, text='Digite uma data:')
label.grid(column=0, row=0)
entry = Entry(root)
entry.grid(column=1, row=0)
button = Button(root, text='Clique', command=clicked)
button.grid(column=0, row=1, columnspan=2)
root.mainloop()