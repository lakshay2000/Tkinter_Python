#Creating Button


from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text="Button has been made")
    myLabel.pack()

myBotton=Button(root,text="Click me!",padx=50,command=myClick,foreground="blue",background="black")
# myBotton=Button(root,text="Click me!",state=DISABLED)
myBotton.pack()


root.mainloop()