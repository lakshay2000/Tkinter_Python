# CRUD Operation on SQLite3 

# USING DATABASE SQLite3

from os import CLD_EXITED
from sqlite3.dbapi2 import Cursor, IntegrityError
from tkinter import *

import sqlite3

root=Tk()
root.geometry("400x600")

#Uodate function to update the record


def edit():
	conn=sqlite3.connect('address_book.db')
	c= conn.cursor()
	record_id = delete_box.get()

	c.execute("""UPDATE addresses SET 
	first_name = :first,
	last_name=:last,
	address=:address,
	city=:city,
	state=:state,
	zipcode=:zipcode
	
	WHERE oid = :oid
	""",
	{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'address': address_editor.get(),
		'city': city_editor.get(),
		'state': state_editor.get(),
		'zipcode':zipcode_editor.get(),
		'oid':record_id
	})
	
		





	conn.commit()
	conn.close()

	editor.destroy()
	


def update():
	global editor
	editor=Tk()
	editor.geometry("400x600")

	conn=sqlite3.connect('address_book.db')
	c= conn.cursor()
	
	record_id=delete_box.get()
	#Query the database
	c.execute("SELECT * FROM addresses WHERE oid = " + record_id)


	# Loop through results
	


	d=c.fetchall()
	print(d)

	# Since tkinter doesnt work well with print, we have to make label and print in it 

	# Create global variables for text box names 
	global f_name_editor
	global l_name_editor
	global address_editor
	global state_editor
	global city_editor
	global zipcode_editor
	


	f_name_editor=Entry(editor,width=30)
	f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

	l_name_editor=Entry(editor,width=30)
	l_name_editor.grid(row=1,column=1)

	address_editor=Entry(editor,width=30)
	address_editor.grid(row=2,column=1)

	city_editor=Entry(editor,width=30)
	city_editor.grid(row=3,column=1)

	state_editor=Entry(editor,width=30)
	state_editor.grid(row=4,column=1)

	zipcode_editor=Entry(editor,width=30)
	zipcode_editor.grid(row=5,column=1)

	

# Creating Label 

	f_name_label_editor=Label(editor,text="First Name")
	f_name_label_editor.grid(row=0,column=0,pady=(10,0))

	l_name_label_editor=Label(editor,text="Last Name")
	l_name_label_editor.grid(row=1,column=0)

	address_label_editor=Label(editor,text="Adress")
	address_label_editor.grid(row=2,column=0)

	city_label_editor=Label(editor,text="City")
	city_label_editor.grid(row=3,column=0)


	state_label_editor=Label(editor,text="State")
	state_label_editor.grid(row=4,column=0)

	zipcode_label_editor=Label(editor,text="Zip-Code")
	zipcode_label_editor.grid(row=5,column=0)

	# Save button to save edited record 
	for record in d:
		f_name_editor.insert(0,record[0])
		l_name_editor.insert(0,record[1])
		address_editor.insert(0,record[2])
		city_editor.insert(0,record[3])
		state_editor.insert(0,record[4])
		zipcode_editor.insert(0,record[5])
 

	save_btn=Button(editor,text="Update record",command=edit)
	save_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=140)
	






# Delete function to delete a record
def delete():
	conn=sqlite3.connect('address_book.db')
	c= conn.cursor()
	
	c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())



	conn.commit()
	conn.close()
	



def submit():
	# CREATE DATABASES OR CONNECT TO ONE
	conn=sqlite3.connect('address_book.db')
	# Cursor - when we want to execute any sort of command, the cursor does that 
	# CREATE CURSOR 
	c= conn.cursor()

	# Insert into the tables 
	c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
	
	{
		'f_name':f_name.get(),
		'l_name':l_name.get(),
		'address':address.get(),
		'city':city.get(),
		'state':state.get(),
		'zipcode':zipcode.get()
	}
	
	)

	# COMMIT CHANGES 
	conn.commit()
	conn.close()
	
	
	
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

	
	
def query():
	conn=sqlite3.connect('address_book.db')
	c= conn.cursor()

	#Query the database
	c.execute("SELECT *,oid FROM addresses")
	d=c.fetchall()
	print(d)
	# Since tkinter doesnt work well with print, we have to make label and print in it 
	#LOOP THE RESULTS
	print_records=""
	for record in d:
		print_records+=str(record[0]) + " " +str(record[1]) + " "+  str(record[6]) + "\n"
	
	query_label=Label(root,text=print_records)
	query_label.grid(row=12,column=0,columnspan=2)


	conn.commit()
	conn.close()


# data types in SQlite3- 
#   text
#   Integer 
#   Decimal number (Real)
#   NULL
#   BLOB (image file)

#CREATE TABLE
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
'''

#Create text boxes

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1)

# Creating Label 

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Adress")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)


state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zip-Code")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0)
# Creating Submit button

submit_btn=Button(root,text="Add record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#creating a Query Button

query_btn=Button(root,text="Show records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)


# Creating a delete button
dlt_btn=Button(root,text="Delete record",command=delete)
dlt_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=140)

# Creating an update button
updt_btn=Button(root,text="Update record",command=update)
updt_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=140)



# Close Connection 

root.mainloop()