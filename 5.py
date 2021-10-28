from tkinter import *
from PIL import ImageTk,Image
root=Tk()

root.title("Icons,Images")

# root.iconbitmap('/Desktop/python/Tkinter/icon.ico')

button_quit=Button(root,text="Exit program",command=root.quit)

button_quit.pack()


# USING IMAGES 

my_img = ImageTk.PhotoImage(Image.open("XOsX.gif"))



root.mainloop()