import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime
from tkinter import messagebox


def visit():
    user_screen.place_forget()
    root.pack()




Win = Tk ()

screen_width = Win.winfo_screenwidth()
screen_height = Win.winfo_screenheight()
Win.geometry("800x550" )
Win.title("Homepage" )


user_screen = Frame( ) 

img = Image.open("Images/logo.png")

# Resize the image
img = img.resize((100, 100), Image.ANTIALIAS)

# Create a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(img )

# Create a label to display the image
label = Label(image=photo)

# Set the label as the main widget for the window
label.pack()



user_screen.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_message = Label(user_screen, width=100,height=3, font=("Arial bold", 22), text="WELCOME TO BARATON BAKERY ORDER  SYSTEM", background="gray")
intro_message.pack()
intro_message = Label(user_screen, width=120,height=2, font=("italic ", 16), text="Your service is our utmost priority", background="violet")
intro_message.pack()

root = Frame(Win)
root.pack_forget()



play_b = Button (user_screen, width=33,height=2, text="Get started", command=visit, background="pink")
play_b.pack()




# login section


# Create a button and add it to the main window


def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        login_status.config(text="Login Successful")
  
        







     
   
    else:
     messagebox.showinfo("Notification", "Invalid username or password. Try again! if you forgot your password please reset your password.")


      

# Create the main window
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(root, text="Login", command=check_credentials)
login_button.pack()


# Create Account

username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

Email_label = tk.Label(root, text="Email address")
Email_label.pack()
Email_entry = tk.Entry(root)
Email_entry.pack()


phone_label = tk.Label(root, text="Phone Number")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()


password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Sign up", command=visit)
login_button.pack()





# Create the login status label
login_status = tk.Label(root, text="")
login_status.pack()




Win.mainloop()