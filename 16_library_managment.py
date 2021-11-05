# Library managment system With SQL connectivity 
from tkinter import *
from tkinter import font
from tkinter import ttk
import mysql.connector


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")

        #HEADING

        lbl_title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",background="powder blue",foreground="green",border=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP,fill=X)

        #Whole Frame

        frame=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        frame.place(x=0,y=130,width=1850,height=600)

        # Left DataFrame 

        DataFrameLeft=Label(frame,bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1100,height=550)

        #Entries in Left DataFrame

        lblMember=Label(DataFrameLeft,text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6,background="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1,padx=15)

        lblPRN_no=Label(DataFrameLeft,text="PRN No",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblPRN_no.grid(row=1,column=0,sticky=W)

        txtPRN_no=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtPRN_no.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,text="ID no: ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,text="First Name ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,text="Last Name ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,text="Address1 ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,text="Address2 ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,text="Post Code ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,text="Book ID ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblBookID.grid(row=0,column=3,sticky=W,padx=100)
        txtBookID=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtBookID.grid(row=0,column=4)

        lblTitle=Label(DataFrameLeft,text="Book Title ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblTitle.grid(row=1,column=3,sticky=W,padx=100)
        txtTitle=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtTitle.grid(row=1,column=4)

        lblAuthor=Label(DataFrameLeft,text="Author ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblAuthor.grid(row=2,column=3,sticky=W,padx=100)
        txtAuthor=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtAuthor.grid(row=2,column=4)

        lblDateBorrowed=Label(DataFrameLeft,text="Date Borrowed ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDateBorrowed.grid(row=3,column=3,sticky=W,padx=100)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtDateBorrowed.grid(row=3,column=4)

        lblDateDue=Label(DataFrameLeft,text="Date Due: ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDateDue.grid(row=4,column=3,sticky=W,padx=100)
        txtDateDue=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtDateDue.grid(row=4,column=4)

        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDaysOnBook.grid(row=5,column=3,sticky=W,padx=100)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtDaysOnBook.grid(row=5,column=4)

        lblLateReturnFine=Label(DataFrameLeft,text="Late Return FIne ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblLateReturnFine.grid(row=6,column=3,sticky=W,padx=100)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtLateReturnFine.grid(row=6,column=4)

        lblDateOverDue=Label(DataFrameLeft,text="Date Over Due ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDateOverDue.grid(row=7,column=3,sticky=W,padx=100)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtDateOverDue.grid(row=7,column=4)

        lblActualPrice=Label(DataFrameLeft,text="ActualPrice ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblActualPrice.grid(row=8,column=3,sticky=W,padx=100)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22)
        txtActualPrice.grid(row=8,column=4)

        

        


        

        # Right DataFrame 

        DataFrameRight=Label(frame,background="powder blue",foreground="green",border=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=1110,y=5,width=660,height=550)
        
        self.textBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=45,height=25)
        self.textBox.grid(row=0,column=2,padx=10,pady=6)

        ListScrollBar=Scrollbar(DataFrameRight)
        ListScrollBar.grid(row=0,column=1,sticky="ns")

        listBook=["Head Firt Book","Learn Python the Hard Way","Python Programming","Secrete Rahshy","Python CookBook","Intro to Machine LEarning","Fluent Python","Machine tecno","My Python","Joss Ellif guru","Junglu Python","Mumbai Python","Pune Python","Machine Python","Advance Python","Inton Python","RedChilli Python","Ishq Python"]

        listBox=Listbox(DataFrameRight,font=("times new roman",15,"bold"),width=20,height=24)
        listBox.grid(row=0,column=0,padx=6)
        ListScrollBar.config(command=listBox.yview)

        for item in listBook:
            listBox.insert(END,item)



        #BUTTONS FRAME 

        Frame_Button=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        Frame_Button.place(x=0,y=730,width=1850,height=70)

        btnAddData=Button(Frame_Button,text="Add Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnAddData.grid(row=0,column=0,pady=5)

        btnShowData=Button(Frame_Button,text="Show Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnShowData.grid(row=0,column=1,pady=5)

        btnUpdateData=Button(Frame_Button,text="Update Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnUpdateData.grid(row=0,column=2,pady=5)

        btnDeleteData=Button(Frame_Button,text="Delete Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnDeleteData.grid(row=0,column=3,pady=5)

        btnResetData=Button(Frame_Button,text="Reset Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnResetData.grid(row=0,column=4,pady=5)

        btnExitData=Button(Frame_Button,text="Exit Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnExitData.grid(row=0,column=5,pady=5)

        # DATABASE FRAME 

        FrameDetails=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        FrameDetails.place(x=0,y=800,width=1850,height=215)

        TableFrame=Frame(FrameDetails,border=6,relief=RIDGE,bg="powder blue")
        TableFrame.place(x=0,y=2,width=1800,height=185)

        xscroll=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(TableFrame,orient=VERTICAL)

        # These are dummy type 
        self.library_table=ttk.Treeview(TableFrame,columns=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","databorrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        # These are names which user will see
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("databorrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=120)
        self.library_table.column("prnno",width=120)
        self.library_table.column("title",width=120)
        self.library_table.column("firstname",width=120)
        self.library_table.column("lastname",width=120)
        self.library_table.column("address1",width=120)
        self.library_table.column("address2",width=120)
        self.library_table.column("postid",width=120)
        self.library_table.column("mobile",width=120)
        self.library_table.column("bookid",width=120)
        self.library_table.column("booktitle",width=120)
        self.library_table.column("author",width=120)
        self.library_table.column("databorrowed",width=120)
        self.library_table.column("datedue",width=120)
        self.library_table.column("days",width=120)
        self.library_table.column("latereturnfine",width=120)
        self.library_table.column("dateoverdue",width=120)
        self.library_table.column("finalprice",width=120)

       
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
        