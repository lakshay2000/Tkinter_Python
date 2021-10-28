#Stating with Tkinter


# tk - widget tool 
# kinter- python interface 

from tkinter import *

root = Tk()



# GUI logic 
#creating a Label widget
myLabel= Label(root,text="Hello world!")
myLabel1= Label(root,text="MY name is")
# Showing onto the screen 
# myLabel1.pack()
myLabel.grid(row=0,column=0)
myLabel1.grid(row=1,column=0)

root.mainloop()