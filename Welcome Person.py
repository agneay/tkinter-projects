from tkinter import *

root = Tk()
root.title("Welcome Person")

label = Label(root,text="Enter Your Name:")
label.grid(row=0,column=0)

e = Entry(root)
e.grid(row=0,column=2)

def dostuff():
    label2 = Label(root,text="Welcome!"+e.get()).grid(row=2,column=1)
btn = Button(root,text="OK",command=dostuff).grid(row=1,column=1)

root.mainloop()