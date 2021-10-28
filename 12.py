# CHECKBOXES 

from tkinter import *


root=Tk()

def show():
    myLabel=Label(root,text=var.get()).pack()


var = StringVar()

c= Checkbutton(root,text="Check this box",variable=var,onvalue="ON",offvalue="OFF")
c.deselect()
c.pack()



myBtn=Button(root,text="Show",command=show).pack()

root.mainloop()