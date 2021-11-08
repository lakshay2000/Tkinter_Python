# Library managment system With SQL connectivity 
from tkinter import *
from tkinter import font
from tkinter import ttk
import datetime
from datetime import date
import tkinter
import MySQLdb
from tkinter import messagebox

class LibraryManagementSystem:

    



    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")


        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

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

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=27,state="readonly",textvariable=self.member_var)
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1,padx=15)

        lblPRN_no=Label(DataFrameLeft,text="PRN No",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblPRN_no.grid(row=1,column=0,sticky=W)

        txtPRN_no=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.prn_var)
        txtPRN_no.grid(row=1,column=1)

        lblIdNo=Label(DataFrameLeft,text="ID no: ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblIdNo.grid(row=2,column=0,sticky=W)
        txtIdNo=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.id_var)
        txtIdNo.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,text="First Name ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.firstname_var)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,text="Last Name ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.lastname_var)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,text="Address1 ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.address1_var)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,text="Address2 ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.address2_var)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,text="Post Code ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.postcode_var)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.mobile_var)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,text="Book ID ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblBookID.grid(row=0,column=3,sticky=W,padx=100)
        txtBookID=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.bookid_var)
        txtBookID.grid(row=0,column=4)

        lblTitle=Label(DataFrameLeft,text="Book Title ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblTitle.grid(row=1,column=3,sticky=W,padx=100)
        txtTitle=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.booktitle_var)
        txtTitle.grid(row=1,column=4)

        lblAuthor=Label(DataFrameLeft,text="Author ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblAuthor.grid(row=2,column=3,sticky=W,padx=100)
        txtAuthor=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.author_var)
        txtAuthor.grid(row=2,column=4)

        lblDateBorrowed=Label(DataFrameLeft,text="Date Borrowed ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDateBorrowed.grid(row=3,column=3,sticky=W,padx=100)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3,column=4)

        lblDateDue=Label(DataFrameLeft,text="Date Due: ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDateDue.grid(row=4,column=3,sticky=W,padx=100)
        txtDateDue=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.datedue_var)
        txtDateDue.grid(row=4,column=4)

        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDaysOnBook.grid(row=5,column=3,sticky=W,padx=100)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.daysonbook_var)
        txtDaysOnBook.grid(row=5,column=4)

        lblLateReturnFine=Label(DataFrameLeft,text="Late Return FIne ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblLateReturnFine.grid(row=6,column=3,sticky=W,padx=100)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.latereturnfine_var)
        txtLateReturnFine.grid(row=6,column=4)

        lblDateOverDue=Label(DataFrameLeft,text="Date Over Due ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblDateOverDue.grid(row=7,column=3,sticky=W,padx=100)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7,column=4)

        lblActualPrice=Label(DataFrameLeft,text="ActualPrice ",font=("arial",15,"bold"),padx=2,pady=6,background="powder blue")
        lblActualPrice.grid(row=8,column=3,sticky=W,padx=100)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",15,"bold"),width=22,textvariable=self.finalprice_var)
        txtActualPrice.grid(row=8,column=4)

        

        


        

        # Right DataFrame 

        DataFrameRight=Label(frame,background="powder blue",foreground="green",border=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=1110,y=5,width=660,height=550)
        
        self.textBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=45,height=25)
        self.textBox.grid(row=0,column=2,padx=10,pady=6)

        ListScrollBar=Scrollbar(DataFrameRight)
        ListScrollBar.grid(row=0,column=1,sticky="ns")

        listBook=["Head Firt Book","Learn Python the Hard Way","Python Programming","Secrete Rahshy","Python CookBook","Intro to Machine LEarning","Fluent Python","Machine tecno","My Python","Joss Ellif guru","Junglu Python","Mumbai Python","Pune Python","Machine Python","Advance Python","Inton Python","RedChilli Python","Ishq Python"]

        def SelectBook(event=""):
            index=listBox.curselection()
            value=listBox.get(index[0])

            
            print(value)
            x=value
            if(x=="Head Firt Book"):
                self.bookid_var.set("BKID01")
                self.booktitle_var.set("Python manual")
                self.author_var.set("Paul Berry")
                
                d1=date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 780")

            elif(x=="Learn Python the Hard Way"):
                self.bookid_var.set("BKID02")
                self.booktitle_var.set("Python manual")
                self.author_var.set("Tanishq Banga")
                
                d1=date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 500")





        listBox=Listbox(DataFrameRight,font=("times new roman",15,"bold"),width=20,height=24)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=6)
        ListScrollBar.config(command=listBox.yview)

        for item in listBook:
            listBox.insert(END,item)



        #BUTTONS FRAME 

        Frame_Button=Frame(self.root,border=12,relief=RIDGE,padx=20,background="powder blue")
        Frame_Button.place(x=0,y=730,width=1850,height=70)

        btnAddData=Button(Frame_Button,text="Add Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white",command=self.add_data)
        btnAddData.grid(row=0,column=0,pady=5)

        btnShowData=Button(Frame_Button,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnShowData.grid(row=0,column=1,pady=5)

        btnUpdateData=Button(Frame_Button,text="Update Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white")
        btnUpdateData.grid(row=0,column=2,pady=5)

        btnDeleteData=Button(Frame_Button,text="Delete Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white",command=self.DeleteData)
        btnDeleteData.grid(row=0,column=3,pady=5)

        btnResetData=Button(Frame_Button,text="Reset Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white",command=self.reset)
        btnResetData.grid(row=0,column=4,pady=5)

        btnExitData=Button(Frame_Button,text="Exit Data",font=("arial",12,"bold"),width=30,background="blue",foreground="white",command=self.iExit)
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

        self.show_data()
        self.library_table.bind("<<ButtonRelease-1>>",self.get_cursor)

    def add_data(self):
        db=MySQLdb.connect(host="localhost",user="root",password="Abcd@1234",db="database_1")

        my_cursor=db.cursor()
        my_cursor.execute("insert into LibraryManagement values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()

        ))

        db.commit()
        self.show_data()
        db.close()

        messagebox.showinfo("Success","Member has been Added")

    def show_data(self):
        db=MySQLdb.connect(host="localhost",user="root",password="Abcd@1234",db="database_1")

        my_cursor=db.cursor()

        my_cursor.execute("select * from LibraryManagement")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            db.commit()
        db.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showData(self):
        self.textBox.insert(END,"Member Type \t \t"+self.member_var.get()+"\n")
        self.textBox.insert(END,"PRN no. \t \t"+self.prn_var.get()+"\n")
        self.textBox.insert(END,"ID no. \t \t"+self.id_var.get()+"\n")
        self.textBox.insert(END,"First Name \t \t"+self.firstname_var.get()+"\n")
        self.textBox.insert(END,"Last Name \t \t"+self.lastname_var.get()+"\n")
        self.textBox.insert(END,"Address 1 \t \t"+self.address1_var.get()+"\n")
        self.textBox.insert(END,"Address 2 \t \t"+self.address2_var.get()+"\n")
        self.textBox.insert(END,"Post Code \t \t"+self.postcode_var.get()+"\n")
        self.textBox.insert(END,"Mobile No. \t \t"+self.mobile_var.get()+"\n")
        self.textBox.insert(END,"Book ID \t \t"+self.bookid_var.get()+"\n")
        self.textBox.insert(END,"Book Title \t \t"+self.booktitle_var.get()+"\n")
        self.textBox.insert(END,"Author \t \t"+self.author_var.get()+"\n")
        self.textBox.insert(END,"Date Borrowed \t \t"+self.dateborrowed_var.get()+"\n")
        self.textBox.insert(END,"Date Due \t \t"+self.datedue_var.get()+"\n")
        self.textBox.insert(END,"Days on Book \t \t"+self.daysonbook_var.get()+"\n")
        self.textBox.insert(END,"Late Return Fine \t \t"+self.latereturnfine_var.get()+"\n")
        self.textBox.insert(END,"Date Over Due \t \t"+self.dateoverdue_var.get()+"\n")
        self.textBox.insert(END,"Final PRice \t \t"+self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")

# from tkinter import messagebox

    def iExit(self):
        exit=messagebox.askyesno("Library Management System ","Do you want to exit")
        if exit==True:       
            self.root.destroy()     
    
    def DeleteData(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the member")
        else:
            db=MySQLdb.connect(host="localhost",user="root",password="Abcd@1234",db="database_1")

            my_cursor=db.cursor()
            query="delete from LibraryManagement where PRN_NO=%s"
            value=(self.prn_var.get())
            my_cursor.execute(query,value)
            db.commit()
            self.show_data()
            self.reset()
            db.close()

            messagebox.showinfo("SUCCESS","Member has been deleted")





       
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
        