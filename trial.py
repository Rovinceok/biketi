import mysql.connector
from tkinter import *
import mysql.connector
from tkinter import *


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="class_project"
)

mycursor = mydb.cursor()

def insert_data():
    username = name_entry.get()
    email = email_entry.get()
    phone_no = phone_entry.get()
    location = location_entry.get()
    u_password = location_entry.get()

    sql = "INSERT INTO users (username, email, phone_no,location,u_password) VALUES (%s, %s, %s,%s,%s)"
    val = (username, email, phone_no, location, u_password)

    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


root = Tk()
root.title("Insert Data into Database")

name_label = Label(root, text="Name")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

email_label = Label(root, text="Email")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

phone_label = Label(root, text="Phone")
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

location_label = Label(root, text="Location")
location_label.pack()
location_entry = Entry(root)
location_entry.pack()


u_password_label = Label(root, text="Password")
u_password_label.pack()
u_password_entry = Entry(root)
u_password_entry.pack()



insert_button = Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

root.mainloop()
