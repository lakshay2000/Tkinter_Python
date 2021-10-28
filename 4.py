from tkinter import *
from typing import Match

root=Tk()
root.title("Simple Calculator")

# a=Entry(root,width=50,bg="red",fg="yellow",borderwidth=10)
a=Entry(root,width=35,borderwidth=5)
a.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#will give default field 
# a.insert(0, "Enter your name")

def button_click(number):
    # a.delete(0,END)
    current = a.get()
    a.delete(0,END)
    a.insert(0,str(current) + str(number))

def button_clear():
    a.delete(0,END)

def button_add():
    first_number=a.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)

    a.delete(0,END)

def button_equal():
    second_number=a.get()   
    a.delete(0,END)

    if math=="addition":
            a.insert(0,f_num+int(second_number))
    if math=="subtraction":
            a.insert(0,f_num-int(second_number))
    if math=="multiply":
            a.insert(0,f_num*int(second_number))
    if math=="divide":
            a.insert(0,f_num/int(second_number))

    
    # a.delete(0,END)


def button_sub():
    first_number=a.get()
    global f_num
    global math
    # math="addition"
    math="subtraction"
    f_num=int(first_number)
    a.delete(0,END)
    # return

def button_mul():
    first_number=a.get()
    global f_num
    global math
    # math="addition"
    math="multiply"
    f_num=int(first_number)
    a.delete(0,END)
    # return

def button_divide():
    first_number=a.get()
    global f_num
    global math
    # math="addition"
    math="divide"
    f_num=int(first_number)
    a.delete(0,END)
    # return


# Degine buttons 

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root,text="+",padx="39",pady="20",command=button_add)
button_equal = Button(root,text="=",padx="91",pady="20",command=button_equal)
button_clear = Button(root,text="Clear",padx="80",pady="20",command=button_clear)

button_sub = Button(root,text="-",padx="39",pady="20",command=button_sub)
button_mul = Button(root,text="X",padx="39",pady="20",command=button_mul)
button_divide = Button(root,text="/",padx="39",pady="20",command=button_divide)

button_1.grid(row= 3, column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=2)

button_4.grid(row= 2, column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row= 2, column=2)

button_7.grid(row= 1, column=0)
button_8.grid(row= 1, column=1)
button_9.grid(row= 1, column=2)

button_0.grid(row= 4, column=0)

button_clear.grid(row= 4, column=1,columnspan=2)
button_add.grid(row= 5, column=0)
button_equal.grid(row= 5, column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

# put the buttons on screen 


# myBotton=Button(root,text="What is your name!!",padx=50,command=myClick,foreground="blue",background="black")
# myBotton=Button(root,text="Click me!",state=DISABLED)






root.mainloop()