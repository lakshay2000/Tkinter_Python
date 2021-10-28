# Open File Dialogue Box 

from tkinter import *
from tkinter import filedialog

root=Tk()

root.filename = filedialog.askopenfile(initialdir="home",title="hello",filetypes=(("all file","*.*"),))



root.mainloop()