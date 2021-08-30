import sqlite3
from tkinter import *

manage = Tk()
manage.title('Registration')
manage.geometry('1500x900')
# connect to database
conn = sqlite3.connect('School_Management.db')
# create a cursor
c = conn.cursor()
"""
c.execute(('''CREATE TABLE addresses(
          student_id integer,
        first_name  text ,
       middle_name text,
       last_name  text ,
        class text,
        age integer ,
        gender text ,
        date_of_birth integer,
        address text ,
         mother_name text ,
       father_name text,
         email_address text,
        contact_number integer,
        date_of_admission integer
     )'''))
print("Table created")
"""

conn.commit()
conn.close()
mainloop()