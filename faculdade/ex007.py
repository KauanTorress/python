from tkinter import Tk, Label, PhotoImage

root= Tk()
photo = PhotoImage(file="rock.png").subsample(5)
hello = Label(master=root, image=photo, height=200, width=200)
hello.pack()
root.mainloop()