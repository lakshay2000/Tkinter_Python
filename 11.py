#Slide bar

from tkinter import *

root=Tk()

root.geometry("400x400")
def slide():
    # Label(root,text=horizontal.get()).pack()
    my_lbl=Label(root,text=vertical.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

vertical=Scale(root, from_=0, to=100)
vertical.pack()


horizontal = Scale(root, from_=0,to=100,orient=HORIZONTAL).pack()
my_lbl=Label(root,text=horizontal.get()).pack()



my_btn = Button(root,text="Click me",command=slide).pack()
# 

root.mainloop()