import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


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

# Using an image as background
image = Image.open('school.PNG')
image = image.resize((1225, 475), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(image)

img = Label(Entry_frame_details, image=pic).place(x=-252, y=0)

# Create text boxes
id = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
id.place(x=720, y=15)

first_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
first_name.place(x=-120, y=65)

Middle_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
Middle_name.place(x=320, y=65)

last_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
last_name.place(x=720, y=65)

Class = Entry(Entry_frame_details, font='Cambria 15 italic', width=13, borderwidth=5)
Class.place(x=-120, y=115)

age = Entry(Entry_frame_details, font='Cambria 15 italic', width=9, borderwidth=5)
age.place(x=150, y=115)

address = Entry(Entry_frame_details, font='Cambria 15 italic', width=36, borderwidth=5)
address.place(x=-120, y=170)

date_of_birth = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
date_of_birth.place(x=720, y=113)

gender = ttk.Combobox(Entry_frame_details, font='Cambria 15 italic', state="readonly", width=7)
gender['values'] = ("Male", "Female")
gender.place(x=390, y=115)

father_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
father_name.place(x=325, y=220)

mother_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
mother_name.place(x=-100, y=220)

Contact_number = Entry(Entry_frame_details, font='Cambria 15 italic', width=18, borderwidth=5)
Contact_number.place(x=763, y=220)

Email_address = Entry(Entry_frame_details, font=('Cambria 15 italic', 14,), width=40, borderwidth=5)
Email_address.place(x=522, y=170)

Date_of_admission = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5)
Date_of_admission.place(x=-80, y=270)

# create textLabels
label = Label(Entry_frame_details, text='ENTER STUDENT DETAILS', font=('Cambria 15 italic', 17, 'bold'),
              bg='Grey').place(x=-248, y=15)

id_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Student ID', bg='black', fg='white',
                 relief=SUNKEN, bd=5).place(x=600, y=15)

first_name_label = Label(Entry_frame_details, text='First Name', font='Cambria 15 italic', bg='black', fg='white',
                         relief=SUNKEN, bd=5).place(x=-248, y=65)

Middle_name_label = Label(Entry_frame_details, text='Middle Name', font='Cambria 15 italic', bg='black', fg='white',
                          relief=SUNKEN, bd=5).place(x=190, y=65)

last_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Last Name', bg='black', fg='white',
                        relief=SUNKEN, bd=5).place(x=600, y=65)

class_label = Label(Entry_frame_details, text='Class', font='Cambria 15 italic', bg='black', fg='white', relief=SUNKEN,
                    bd=5).place(x=-248, y=115)

age_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Age', bg='black', fg='white', relief=SUNKEN,
                  bd=5).place(x=90, y=115)

address_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Address', bg='black', fg='white',
                      relief=SUNKEN, bd=5).place(x=-248, y=170)

date_of_birth_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Date Of Birth(*in AD)', bg='black',
                            fg='white', relief=SUNKEN, bd=5).place(x=520, y=113)

gender_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Gender', bg='black', fg='white',
                     relief=SUNKEN, bd=5).place(x=290, y=115)

father_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text="Father's Name ", bg='black', fg='white',
                          relief=SUNKEN, bd=5).place(x=177, y=220)

mother_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text="Mother's Name ", bg='black', fg='white',
                          relief=SUNKEN, bd=5).place(x=-248, y=220)

Contact_number_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Contact Number', bg='black',
                             fg='white', relief=SUNKEN, bd=5).place(x=600, y=220)

Email_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Email address', bg='black', fg='white',
                    relief=SUNKEN, bd=5).place(x=365, y=170)

Date_of_admission_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Date Of Admission', bg='black',
                                fg='white', bd=5, relief=SUNKEN).place(x=-248, y=275)



def submit():
    """ This is the function that helps us to submit the entered data."""
    conn = sqlite3.connect('School_Management.db')

    c = conn.cursor()

    # insert into table
    c.execute(
        "INSERT INTO addresses VAlUES(:student_id,:first_name, :middle_name,:last_name,:class,:age,:gender,:date_of_birth,:address,:mother_name,:father_name,:email_address,:contact_number,:date_of_admission)",
        {
            'student_id': id.get(),
            'first_name': first_name.get(),
            'middle_name': Middle_name.get(),
            'last_name': last_name.get(),
            'class': Class.get(),
            'age': age.get(),
            'gender': gender.get(),
            'date_of_birth': date_of_birth.get(),
            'address': address.get(),
            'mother_name': mother_name.get(),
            'father_name': father_name.get(),
            'email_address': Email_address.get(),
            'contact_number': Contact_number.get(),
            'date_of_admission': Date_of_admission.get()
        })
    print('Address inserted successfully')

    conn.commit()
    conn.close()
    # Making the entries clean to enter new entries
    id.delete(0, END)
    first_name.delete(0, END)
    Middle_name.delete(0, END)
    last_name.delete(0, END)
    Class.delete(0, END)
    age.delete(0, END)
    gender.delete(0, END)
    date_of_birth.delete(0, END)
    address.delete(0, END)
    mother_name.delete(0, END)
    father_name.delete(0, END)
    Email_address.delete(0, END)
    Contact_number.delete(0, END)
    Date_of_admission.delete(0, END)
# Printing the doc string
print(submit.__doc__)

def show_records():
    """This the function built inorder to see entered function"""
    record = Toplevel()
    record.title("STUDENT RECORDS")
    record.geometry('1400x800')
    record.iconbitmap("icon.ico")
    record.configure(bg="Light Green")
    # Frame for showing records
    Record_frame = Frame(record, bg='Sky Blue', bd=10, relief=RIDGE)
    Record_frame.place(x=20, y=100, width=1300, height=500)

print(show_records.__doc__)

#Creating buttons
submit_button = Button(Entry_frame_details, text='SUBMIT', font=('Cambria 15 italic', 13, 'bold'), width=10, bd=5,command= submit)
submit_button.place(x=170, y=350)

show_button = Button(Entry_frame_details, text='SHOW RECORDS', font=('Cambria 15 italic', 13, 'bold'), width=15, bd=5,command= show_records)
show_button.place(x=450, y=350)

conn.commit()
conn.close()
mainloop()