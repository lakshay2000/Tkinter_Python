from tkinter import *

root= Tk()

frame=LabelFrame(root,text="This is my frame",padx=5,pady=5)

frame.pack(padx=10,pady=10)

b=Button(frame, text="Dont click here")
b2=Button(frame, text="or here")

b.grid(row=0,column=0)
b2.grid(row=1,column=1)



















root.mainloop()