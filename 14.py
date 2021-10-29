# USING DATABASE SQLite3

from sqlite3.dbapi2 import Cursor, IntegrityError
from tkinter import *

import sqlite3

root=Tk()

# CREATE DATABASES OR CONNECT TO ONE

conn=sqlite3.connect('address_book.db')

# Cursor - when we want to execute any sort of command, the cursor does that 


# CREATE CURSOR 
c= conn.cursor()

#CREATE TABLE


# data types in SQlite3- 
#   text
#   Integer 
#   Decimal number (Real)
#   NULL
#   BLOB (image file)

c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
# COMMIT CHANGES 
conn.commit()

# Close Connection 
conn.close()

root.mainloop()