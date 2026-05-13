from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root= Tk()
photo = PhotoImage(file='rock.png').subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, text="Aqui é rock!")
text.pack(side=BOTTOM)
root.mainloop()