from tkinter import *

root=Tk()


r=IntVar()
# r.set("1")


# /r.get()
MODES=[
    ("H", "H"),
    ("O","O"),
    ("L","L"),
    ("E","E"),
]

def clicked(value):
    myLabel=Label(root,text=value) 
    myLabel.pack()    

# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: clicked(r.get()) ).pack()

# Radiobutton(root,text="Option 2",variable=r,value=2,command= lambda: clicked(r.get())).pack()

pls= StringVar()
pls.set("H")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pls,value=mode,command=lambda:clicked(pls.get())).pack()

myLabel=Label(root,text=r.get())
myLabel.pack()

# myButton=Button(root,text="Click me",command=lambda:clicked(r.get()))
myButton=Button(root,text="Click me",command=lambda:clicked(pls.get()))
myButton.pack()

root.mainloop()