# Library managment system With SQL connectivity 
from tkinter import *
from tkinter import font


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")

        lbl_title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",background="powder blue",foreground="green",border=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP,fill=X)

        frame=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        frame.place(x=0,y=130,width=1850,height=400)

        DataFrameLeft=Label(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),anchor ='nw')
        
        DataFrameLeft.place(x=0,y=5,width=1100,height=350)
        
        DataFrameRight=Label(frame,text="Book Details",background="powder blue",foreground="green",border=12,relief=RIDGE,font=("times new roman",12,"bold"),anchor ='nw')
        DataFrameRight.place(x=1110,y=5,width=700,height=350)

        #BUTTONS FRAME 

        Frame_Button=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        Frame_Button.place(x=0,y=530,width=1850,height=70)

        # DATABASE FRAME 

        FrameDetails=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        FrameDetails.place(x=0,y=600,width=1850,height=200)

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
        