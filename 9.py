#Creating  new windows 

from tkinter import *

root=Tk()

def open_new():
    top=Toplevel()
    Label(top,text="Hey im in new windows").pack()
    btn2=Button(top,text="Destroy new window",command=top.destroy).pack()


Label(root,text="I m in new root window").pack()

btn=Button(root,text="Open new window",command=open_new)
btn.pack()
root.mainloop()




