from tkinter import *

root = Tk()
count = 0
def doStuff():
    global count
    newLabel = Label(root,text=f"You just clicked that Button {count} times")
    newLabel.grid(row=1,column=0)
    count+=1


myButton = Button(root,text="Press Me!",padx=90,pady=10,command=doStuff)
myButton.grid(row=0,column=0)













root.mainloop()