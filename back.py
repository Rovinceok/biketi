import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.geometry("800x550" )

# Set background image
root.title("Homepage")
img = Image.open("Images/display.png")
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_image = ImageTk.PhotoImage(img)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# Logo
img = Image.open("Images/logo.png")
img = img.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img )
label = Label(image=photo)
label.place(x=0, y=0)
label.pack()


# Labels


user_screen = Frame() 


user_screen.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_message = Label(user_screen, width=100,height=3, font=("Arial bold", 32), text="BARATON BAKERY ORDER  SYSTEM", background="gray")
intro_message.pack()
intro_message = Label(user_screen, width=120,height=2, font=("italic ", 16), text="Your service is our utmost priority", background="violet")
intro_message.pack()

root = Frame(root)
root.pack_forget()

def visit():
    user_screen.place_forget()
    root.pack()


play_b = Button (user_screen, width=33,height=2, text="Get started", command=visit, background="pink")
play_b.pack()


# Admin



    # Create a form with input fields for username, email, and password

   



# Admin login

def Admin():
    username = user_entry.get()
    password = user_entry.get()
    if username == "a" and password == "1":
       Admin_dashboard()
    if username == "" or  password == "":
     messagebox.showerror("Error", "All fields are required. Try again!")
    else:
     messagebox.showerror("Error", "Invalid username or password. Try again!")
     
def A_register_window():
    # Create a new window
    register_window = tk.Toplevel()
    register_window.title("Register")

    # Create a form with input fields for username, email, and password
    username_label = tk.Label(register_window, text="Username", width=80,height=2)
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    password_label = tk.Label(register_window, text="Password" , width=80,height=2)
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()

    # Create a button to submit the registration form
    submit_button = tk.Button(register_window, text="Sign in" ,width=20, bg="gray", command=Admin )
    submit_button.pack()

# End registration function

# Homepage



def Admin_dashboard():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Admin page")
    header_label = tk.Label(window, text="ADMIN DASHBOARD", font=("Arial", 20) ,bg="PINK")
    header_label.pack(side="top", fill="both", padx=10, pady=10)
    window.mainloop()


# Admin dashboard



# Registration function




def Register():
    username = user_entry.get()
    Email = user_entry.get()
    phone = user_entry.get()
    password = user_entry.get()
   
    if username == "" or Email == "" or phone == "" or  password == "":
     messagebox.showerror("Error", "All fields are required. Try again!")
     


header = Label(root, text="Sign in to your account", font=("Helvetica bold", 16) ,bg="violet")
header.pack(pady=20)

def register_window():
    # Create a new window
    register_window = tk.Toplevel()
    register_window.title("Register")

    # Create a form with input fields for username, email, and password
    username_label = tk.Label(register_window, text="Username", width=80,height=2)
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    email_label = tk.Label(register_window, text="Email" , width=80,height=2)
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()

    phone_label = tk.Label(register_window, text="Phone Number" , width=80,height=2)
    phone_label.pack()
    phone_entry = tk.Entry(register_window)
    phone_entry.pack()

    location_label = tk.Label(register_window, text="Location" , width=80,height=2)
    location_label.pack()
    location_entry = tk.Entry(register_window)
    location_entry.pack()

    password_label = tk.Label(register_window, text="Password" , width=80,height=2)
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()

    # Create a button to submit the registration form
    submit_button = tk.Button(register_window, text="Submit" ,width=20, bg="gray", command=Register )
    submit_button.pack()

# End registration function

# Homepage





def homepage():
    # Create a new Tkinter window
    window = tk.Tk()

# Set the window title
    window.title("CatalogPage")
    
# Create a label widget for the header
    header_label = tk.Label(window, text="WELCOME TO OUR PRODUCT CATALOG", font=("Arial", 20) ,bg="violet")

# Place the header label at the top of the window
    header_label.pack(side="top", fill="both", padx=10, pady=10)
    window.mainloop()




# Homepage end


# Login function


def check_credentials():
    username = user_entry.get()
    password = pass_entry.get()
    if username == "u" and password == "1":
       homepage()
        
    if username == "" or password == "":
     messagebox.showerror("Error", "Please fill out all the fields. Username or password cannot be empty")
    else :
     messagebox.showerror("Error", "Invalid username or password. Try again!")





# Username
user_label = Label(root, text="Username:" , width=80,height=2)
user_label.pack(pady=5)
user_entry = Entry(root)
user_entry.pack(pady=5)

# Password
pass_label = Label(root, text="Password:")
pass_label.pack(pady=5)
pass_entry = Entry(root, show="*")
pass_entry.pack(pady=5)

# Login button
login_button = Button(root, text="Sign in", width=20 ,command=check_credentials ,bg="gray")
login_button.pack(pady=10)


# Register button

register_button = tk.Button(root, text="Sign Up", command=register_window, bg="pink" ,width=20)
register_button.pack()


register_button = tk.Button(root, text="Admin Sing in", command=A_register_window, bg="violet" ,width=30)
register_button.pack()


# End Register button



# Create the login status label
login_status = tk.Label(root, text="")
login_status.pack()



root.mainloop()

