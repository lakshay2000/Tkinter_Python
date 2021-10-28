#Creating Input Fields

from tkinter import *

root=Tk()
# a=Entry(root,width=50,bg="red",fg="yellow",borderwidth=10)
a=Entry(root,width=50)
a.pack()
#will give default field 
a.insert(0, "Enter your name")


def myClick():
    myLabel=Label(root,text=a.get())
    myLabel.pack()

myBotton=Button(root,text="What is your name!!",padx=50,command=myClick,foreground="blue",background="black")
# myBotton=Button(root,text="Click me!",state=DISABLED)
myBotton.pack()



root.mainloop()