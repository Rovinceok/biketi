import mysql.connector

import tkinter as tk

root = tk.Tk()

conn = mysql.connector.connect(host="localhost", user="root", password="", database="class_project")
cursor = conn.cursor()

query = "SELECT username, email, phone_no,location,u_password FROM users"
cursor.execute(query)

data = cursor.fetchall()

for i, row in enumerate(data):
    for j, value in enumerate(row):
        label = tk.Label(root, text=value)
        label.grid(row=i, column=j)

conn.close()

root.mainloop()
