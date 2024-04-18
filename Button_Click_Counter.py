from tkinter import *

root = Tk()
root.title("Button Click Counter")
root.geometry("300x100")
count = 0
def doStuff():
    global count
    newLabel = Label(root,text=f"You just clicked that Button {count} times")
    newLabel.grid(row=1,column=0)
    count+=1


myButton = Button(root,text="Press Me!",padx=90,pady=10,command=doStuff,fg="black",bg="aqua")
myButton.grid(row=0,column=0)













root.mainloop()
