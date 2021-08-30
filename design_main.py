import sqlite3
from tkinter import *

manage = Tk()
manage.title('Registration')
manage.geometry('1500x900')
manage.configure(bg='Light Blue')
manage.iconbitmap('icon.ico')
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
# Making title and frames
Title_frame = Frame(manage, bd=10, bg='black', width=1500, relief=RIDGE)
Title_frame.place(x=250, y=15)
Title_frame_label = Label(Title_frame, font=('Cambria 15 italic', 25, 'bold'), bg='light pink',
                          text='SOFTWARICA COLLEGE OF IT AND E-COMMERCE', padx=20)
Title_frame_label.grid()

Entry_frame_details = Frame(manage, bd=10, bg='black', width=1250, height=500, padx=250, relief=RIDGE)
Entry_frame_details.place(x=50, y=100)

conn.commit()
conn.close()
mainloop()