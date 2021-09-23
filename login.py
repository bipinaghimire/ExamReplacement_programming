import sys
from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import time

root = Tk()
root.title('Login Page')
root.geometry('600x400')
root.iconbitmap('icon.ico')
root.resizable(False, False)

### Using an image as background###
# resize image
pic = Image.open("bg_pro.PNG")
resize_pic = pic.resize((603, 400), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_pic)
label1 = Label(root, image=new_pic)
label1.place(x=-3, y=0)

label2 = Label(root, text="Welcome", font=('Cambria 15 italic', 20, 'bold'), fg='purple')
label2.place(x=275, y=10)

label3 = Label(root, text="AUTHORIZED PERSONS ONLY", font='Cambria 15 italic', fg='purple')
label3.place(x=200, y=90)

# data_base
conn = sqlite3.connect('School_Login.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE addresses(
        Username text,
        Password text
    )""")
print("database created")
'''

# Creating login Space
Username = Label(root, text="Username", font='Cambria 15 italic').place(x=170, y=150)
Username_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Username_entry.place(x=270, y=150)
Password = Label(root, text="Password", font='Cambria 15 italic').place(x=170, y=200)
Password_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Password_entry.place(x=270, y=200)

# Adding time in the screen
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")
    day = time.strftime("%A")
    label4.config(text=hour + ":" + minute + ":" + seconds)
    label4.after(1000, clock)

    label5.config(text=day)


# label for time
label4 = Label(root, text="", font=("Ubuntu", 15), fg="red")
label4.place(x=0, y=0)
# label for day of week
label5 = Label(root, text=" ", font=("Ubuntu", 15), fg="red")
label5.place(x=0, y=25)

# Creating functin to login into the file
def log_in():
    user = Username_entry.get()
    passw = Password_entry.get()

    Heads = ["Amit Singh", "Shyam Khatiwada", "Shanta Raymajhi","Prerana Pandit", "Ganesh Bhusal", "Ram Timalsina"]
    Head_password = ["@mit", "$hyam", "shant@","preran@@", "g@ne$h", "*r@m"]

    try:
        if user in Heads and passw in Head_password:
            if Heads.index(user) == Head_password.index(passw):
                messagebox.showinfo("Entered", "Welcome " + Username_entry.get())
                import school_final
        else:
            messagebox.showerror("Error", "Invalid User or Password")
    except:
        messagebox.showinfo('Sorry','If you have trouble regarding login please contact administration')


login_button = Button(root, text="Login", font=('Cambria 15 italic', 17, 'bold'), command=log_in).place(x=300, y=280)

conn.commit()
conn.close()
clock()

root.mainloop()
sys.exit()
