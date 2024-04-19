from tkinter import *

root = Tk()
root.title("Kilometer to Miles converter")
root.geometry("220x100")
value = StringVar()
value2 = StringVar()
Label1 = Label(root,text="Enter kilometer:").grid(row=0,column=0)
Entry1 = Entry(root,textvariable=value).grid(row=0,column=1)
Label2 = Label(root,text="Miles: ").grid(row=1,column=0)
Entry3 = Entry(root,textvariable=value2).grid(row=1,column=1)
def compute():
    val = float(value.get())
    req_val = val * 0.6214
    value2.set(str(req_val))

Btn = Button(root,text="CONVERT",fg="white",bg="red",command=compute).grid(row=3,column=1)
root.mainloop()