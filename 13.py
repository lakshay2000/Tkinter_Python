#DROPDOWN BOX or it is called Option Menu


from tkinter import *



root=Tk()
root.geometry("400x400")


def show():
    mylabel=Label(root,text=clicked.get()).pack()

option = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thrusday",
    "Friday"

]

clicked=StringVar()

clicked.set(option[0])

drop=OptionMenu(root,clicked, *option)
drop.pack()

my_btn=Button(root,text="Show selection",command=show)
my_btn.pack()
root.mainloop()