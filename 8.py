# MESSAGES BOXES 

from tkinter import *
from tkinter import messagebox
root=Tk()

def popup():
    response=messagebox.askyesno("This is my popup","Hello world")
    Label(root,text=response).pack()
    if response == 1:
        Label(root,text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked No!!").pack()




Button(root,text="Popup",command=popup).pack()


# Types of messagebox- showinfo,messagebox.showerror,messagebox.askquestion,messagebox.askokcancel,messagebox.askyesno

root.mainloop()